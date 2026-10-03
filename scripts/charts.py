"""Daily trend charts, ours against upstream, from the collected history.

Per day and per repo/platform/flavour (React Native's RNTester only), over
the runs started that day:
  - test time: the median of each run's total test-step time, retry jobs
    included (the time a run took to go green or give up),
  - runs where every flow passed first time (%),
  - flows that failed at least once, per run (average).
Writes results/daily.csv and one SVG per line of the chart list into
results/charts/. Standard library only: the SVGs are drawn by hand.
"""
import collections
import csv
import os
import statistics
from datetime import date

import retries

OURS, UPSTREAM = "#2563eb", "#9ca3af"
METRICS = [
    ("test_min", "Test time per run (min, median)"),
    ("first_time_pct", "Runs where every flow passed first time (%)"),
    ("failed_once", "Flows that failed at least once, per run"),
]


def _key(r):
    return (r["project"], r["platform"], r["flavor"], retries._app(r["job"]))


def daily(records, run_rows):
    """One row per day, repo/platform/flavour and side."""
    minutes = collections.defaultdict(float)
    for r in records:
        if r.get("e2e_seconds") and r.get("stage", "tests") == "tests":
            minutes[(r["run_id"],) + _key(r)] += r["e2e_seconds"] / 60
    days = collections.defaultdict(list)
    for row in run_rows:
        if not row["complete"] or row["app"] == "templateapp":
            continue
        k = (row["run_id"], row["project"], row["platform"], row["flavor"], row["app"])
        days[(row["created_at"][:10], row["project"], row["platform"], row["flavor"], row["side"])].append(
            (minutes.get(k), row["failed_once"]))
    out = []
    for (day, project, platform, flavor, side), runs in sorted(days.items()):
        times = [m for m, _ in runs if m]
        out.append(dict(
            day=day, project=project, platform=platform, flavor=flavor, side=side, runs=len(runs),
            test_min=round(statistics.median(times), 1) if times else None,
            first_time_pct=round(100 * sum(1 for _, f in runs if f == 0) / len(runs)),
            failed_once=round(sum(f for _, f in runs) / len(runs), 2)))
    return out


def write(results_dir, records, run_rows):
    rows = daily(records, run_rows)
    with open(os.path.join(results_dir, "daily.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["day", "project", "platform", "flavor", "side", "runs",
                                          "test_min", "first_time_pct", "failed_once"])
        w.writeheader()
        w.writerows(rows)
    charts_dir = os.path.join(results_dir, "charts")
    os.makedirs(charts_dir, exist_ok=True)
    groups = collections.defaultdict(list)
    for r in rows:
        groups[(r["project"], r["platform"], r["flavor"])].append(r)
    made = collections.defaultdict(list)
    for (project, platform, flavor), rs in sorted(groups.items()):
        name = "-".join(x for x in (project, platform, flavor) if x) + ".svg"
        title = " ".join(x for x in (project, platform, flavor) if x)
        with open(os.path.join(charts_dir, name), "w") as f:
            f.write(svg(title, rs))
        made[project].append(name)
    return made


def markdown(project, names):
    return "".join(f"![{n[:-4]}](charts/{n})\n\n" for n in names)


# --- drawing -------------------------------------------------------------

W, PANEL_H, PAD_L, PAD_R, PAD_T, GAP = 720, 150, 56, 16, 40, 34


def svg(title, rows):
    days = sorted({r["day"] for r in rows})
    d0 = date.fromisoformat(days[0])
    span = max((date.fromisoformat(days[-1]) - d0).days, 1)
    height = PAD_T + len(METRICS) * (PANEL_H + GAP) + 10
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{height}" '
             f'font-family="-apple-system,Segoe UI,Helvetica,Arial,sans-serif" font-size="11">',
             f'<rect width="100%" height="100%" fill="#ffffff"/>',
             f'<text x="{PAD_L}" y="18" font-size="14" font-weight="600" fill="#111827">{_esc(title)}</text>',
             f'<circle cx="{W - 230}" cy="14" r="4" fill="{OURS}"/>'
             f'<text x="{W - 222}" y="18" fill="#374151">ours (maestro-runner)</text>'
             f'<circle cx="{W - 95}" cy="14" r="4" fill="{UPSTREAM}"/>'
             f'<text x="{W - 87}" y="18" fill="#374151">upstream</text>']
    x = lambda d: PAD_L + (W - PAD_L - PAD_R) * ((date.fromisoformat(d) - d0).days / span if len(days) > 1 else 0.5)
    for i, (metric, label) in enumerate(METRICS):
        top = PAD_T + i * (PANEL_H + GAP)
        vals = [r[metric] for r in rows if r[metric] is not None]
        hi = 100 if metric == "first_time_pct" else _nice(max(vals) if vals else 1)
        y = lambda v: top + PANEL_H - PANEL_H * (v / hi if hi else 0)
        parts.append(f'<text x="{PAD_L}" y="{top - 6}" fill="#374151" font-weight="600">{_esc(label)}</text>')
        for t in range(5):
            v = hi * t / 4
            parts.append(f'<line x1="{PAD_L}" x2="{W - PAD_R}" y1="{y(v):.1f}" y2="{y(v):.1f}" '
                         f'stroke="#e5e7eb"/><text x="{PAD_L - 6}" y="{y(v) + 4:.1f}" text-anchor="end" '
                         f'fill="#6b7280">{_fmt(v)}</text>')
        for side, color in (("upstream", UPSTREAM), ("ours", OURS)):
            pts = [(x(r["day"]), y(r[metric]), r) for r in rows if r["side"] == side and r[metric] is not None]
            if len(pts) > 1:
                parts.append(f'<polyline fill="none" stroke="{color}" stroke-width="2" points="'
                             + " ".join(f"{px:.1f},{py:.1f}" for px, py, _ in pts) + '"/>')
            for px, py, r in pts:
                parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3.5" fill="{color}">'
                             f'<title>{r["day"]} {side}: {_fmt(r[metric])} ({r["runs"]} runs)</title></circle>')
    bottom = PAD_T + len(METRICS) * (PANEL_H + GAP) - GAP + 16
    for d in (days if len(days) <= 10 else days[:: max(len(days) // 8, 1)]):
        parts.append(f'<text x="{x(d):.1f}" y="{bottom}" text-anchor="middle" fill="#6b7280">{d[5:]}</text>')
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def _nice(v):
    for step in (1, 2, 5, 10, 20, 25, 50, 100, 200, 500):
        if v <= step:
            return step
    return v


def _fmt(v):
    return f"{v:.0f}" if v >= 10 or float(v).is_integer() else f"{v:.1f}"


def _esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;")
