# pager-view

Upstream has no e2e CI to compare against.

Times in minutes. *Run* is the whole workflow run (builds included); *job* is one job; *tests* is its test step only; *queue* is the wait for a runner.

## Summary

| Project | Platform | Flavour | Side | Build | Runs | Median e2e (min) | Green runs | Runs with no first-attempt failure | First-attempt failures / run | Final failures / run | Runs needing a retry job | Runner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pager-view | android | - | ours | e8a87b5 | 15 | 19.9 | 0/15 | 0/15 | 9.93 | 9.67 | 0/15 | ubuntu-latest |
| pager-view | android | - | ours | older | 3 | 3.4 | 0/2 | - | - | - | 0/3 | ubuntu-latest |
| pager-view | android | - | ours | 6904d0f | 16 | 19.8 | 0/16 | 0/16 | 9.19 | 8.88 | 0/16 | ubuntu-latest |
| pager-view | ios | - | ours | e8a87b5 | 16 | 10.1 | 0/16 | 0/16 | 4.19 | 3.75 | 0/16 | macos-26 |
| pager-view | ios | - | ours | 6904d0f | 17 | 8.8 | 0/17 | 0/17 | 4.06 | 4.00 | 0/17 | macos-26 |

## Runs: maestro-runner (bench fork)

| Started (UTC) | Run | Build | Run time | Job | Job time | Tests | Queue | Result |
|---|---|---|---|---|---|---|---|---|
| 2026-10-07 01:15 | [37556168133](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37556168133) | e8a87b5 | 42.3 | e2e-android | 21.7 | 20.3 | 0.0 | 12/21 |
|  | | |  | e2e-ios | 42.1 | 10.2 | 0.1 | 19/21, 2 passed on retry |
| 2026-10-06 22:40 | [37542075901](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37542075901) | e8a87b5 | 41.9 | e2e-android | 7.9 | 6.6 | 0.0 | failure |
|  | | |  | e2e-ios | 41.7 | 10.7 | 0.1 | 17/21, 1 passed on retry |
| 2026-10-06 20:00 | [37523142640](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37523142640) | e8a87b5 | 40.6 | e2e-android | 19.5 | 18.3 | 0.0 | 12/21, 1 passed on retry |
|  | | |  | e2e-ios | 40.4 | 12.1 | 0.1 | 17/21 |
| 2026-10-06 17:03 | [37500587061](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37500587061) | e8a87b5 | 36.1 | e2e-android | 21.2 | 19.9 | 0.0 | 12/21 |
|  | | |  | e2e-ios | 35.9 | 10.1 | 0.1 | 17/21 |
| 2026-10-06 14:06 | [37476227210](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37476227210) | e8a87b5 | 44.2 | e2e-android | 21.7 | 20.4 | 0.0 | 12/21 |
|  | | |  | e2e-ios | 44.0 | 12.2 | 0.1 | 17/21 |
| 2026-10-06 11:20 | [37455784759](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37455784759) | e8a87b5 | 39.2 | e2e-android | 21.4 | 20.1 | 0.0 | 12/21 |
|  | | |  | e2e-ios | 39.1 | 9.8 | 0.1 | 17/21, 1 passed on retry |
| 2026-10-06 08:35 | [37437104089](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37437104089) | e8a87b5 | 38.4 | e2e-android | 21.2 | 19.9 | 0.0 | 12/21 |
|  | | |  | e2e-ios | 38.2 | 8.3 | 0.1 | 17/21 |
| 2026-10-06 06:00 | [37421376814](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37421376814) | e8a87b5 | 47.6 | e2e-android | 21.6 | 20.2 | 0.0 | 12/21 |
|  | | |  | e2e-ios | 47.5 | 9.2 | 0.1 | 17/21 |
| 2026-10-06 03:25 | [37408909369](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37408909369) | e8a87b5 | 38.8 | e2e-android | 21.1 | 19.9 | 0.6 | 12/21 |
|  | | |  | e2e-ios | 38.7 | 10.3 | 0.1 | 17/21 |
| 2026-10-06 00:55 | [37396517637](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37396517637) | e8a87b5 | 27.7 | e2e-android | 21.4 | 20.0 | 0.1 | 12/21 |
|  | | |  | e2e-ios | 27.6 | 8.0 | 0.1 | 17/21 |
| 2026-10-05 22:30 | [37382904902](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37382904902) | e8a87b5 | 29.0 | e2e-android | 17.4 | 16.4 | 0.0 | 13/21, 1 passed on retry |
|  | | |  | e2e-ios | 28.8 | 8.8 | 0.1 | 17/21, 1 passed on retry |
| 2026-10-05 20:35 | [37370728213](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37370728213) | - | 15.1 | e2e-android | 15.0 | - | 0.0 | cancelled before tests |
|  | | |  | e2e-ios | 15.0 | - | 0.0 | cancelled before tests |
| 2026-10-05 19:12 | [37361709254](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37361709254) | e8a87b5 | 39.5 | e2e-android | 21.4 | 20.0 | 0.1 | 12/21 |
|  | | |  | e2e-ios | 39.3 | 8.3 | 0.2 | 19/21, 1 passed on retry |
| 2026-10-05 16:05 | [37338102242](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37338102242) | e8a87b5 | 41.2 | e2e-android | 29.0 | 27.6 | 0.1 | 0/21 |
|  | | |  | e2e-ios | 41.0 | 10.7 | 0.1 | 17/21 |
| 2026-10-05 13:09 | [37314639012](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37314639012) | e8a87b5 | 40.7 | e2e-android | 20.9 | 19.6 | 0.0 | 12/21 |
|  | | |  | e2e-ios | 40.6 | 10.2 | 0.1 | 17/21 |
| 2026-10-05 10:03 | [37294100974](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37294100974) | e8a87b5 | 41.3 | e2e-android | 21.0 | 19.7 | 0.0 | 13/21, 2 passed on retry |
|  | | |  | e2e-ios | 41.1 | 8.2 | 0.1 | 17/21 |
| 2026-10-05 06:01 | [37270363181](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37270363181) | e8a87b5 | 30.3 | e2e-android | 21.3 | 19.9 | 0.0 | 12/21 |
|  | | |  | e2e-ios | 30.2 | 10.1 | 0.1 | 17/21, 1 passed on retry |
| 2026-10-05 05:21 | [37267388312](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37267388312) | 6904d0f | 36.3 | e2e-android | 19.1 | 17.9 | 0.0 | 12/21 |
|  | | |  | e2e-ios | 36.1 | 9.7 | 0.1 | 17/21 |
| 2026-10-05 03:18 | [37258886759](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37258886759) | 6904d0f | 31.4 | e2e-android | 21.4 | 20.1 | 0.0 | 12/21 |
|  | | |  | e2e-ios | 31.3 | 7.5 | 0.1 | 17/21 |
| 2026-10-05 01:19 | [37251013915](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37251013915) | 6904d0f | 33.9 | e2e-android | 19.4 | 18.1 | 0.0 | 12/21 |
|  | | |  | e2e-ios | 33.7 | 11.9 | 0.1 | 17/21 |
| 2026-10-04 23:11 | [37242871455](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37242871455) | 6904d0f | 32.6 | e2e-android | 17.5 | 16.4 | 0.0 | 12/21 |
|  | | |  | e2e-ios | 32.4 | 7.7 | 0.1 | 17/21 |
| 2026-10-04 21:13 | [37235208204](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37235208204) | 6904d0f | 27.0 | e2e-android | 19.9 | 18.6 | 0.0 | 12/21 |
|  | | |  | e2e-ios | 26.9 | 9.3 | 0.1 | 17/21, 1 passed on retry |
| 2026-10-04 19:14 | [37227526658](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37227526658) | 6904d0f | 29.5 | e2e-android | 22.2 | 20.8 | 0.0 | 12/21, 1 passed on retry |
|  | | |  | e2e-ios | 29.4 | 7.4 | 0.1 | 17/21 |
| 2026-10-04 17:11 | [37219557379](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37219557379) | 6904d0f | 36.0 | e2e-android | 22.1 | 20.7 | 0.0 | 12/21 |
|  | | |  | e2e-ios | 35.8 | 7.0 | 0.1 | 17/21 |
| 2026-10-04 15:08 | [37211869619](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37211869619) | 6904d0f | 32.4 | e2e-android | 19.1 | 17.9 | 0.1 | 12/21 |
|  | | |  | e2e-ios | 32.2 | 8.8 | 0.1 | 17/21 |
| 2026-10-04 13:00 | [37204069976](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37204069976) | 6904d0f | 44.0 | e2e-android | 21.6 | 20.2 | 0.0 | 13/21 |
|  | | |  | e2e-ios | 43.8 | 10.1 | 0.1 | 17/21 |
| 2026-10-04 10:21 | [37195095621](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37195095621) | 6904d0f | 33.5 | e2e-android | 21.2 | 20.0 | 0.0 | 12/21 |
|  | | |  | e2e-ios | 33.3 | 7.1 | 0.2 | 17/21 |
| 2026-10-04 07:22 | [37185579132](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37185579132) | 6904d0f | 38.2 | e2e-android | 21.0 | 19.8 | 0.0 | 12/21, 1 passed on retry |
|  | | |  | e2e-ios | 38.0 | 8.9 | 0.1 | 17/21 |
| 2026-10-04 05:30 | [37180075296](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37180075296) | 6904d0f | 41.1 | e2e-android | 20.2 | 19.1 | 0.0 | 13/21, 2 passed on retry |
|  | | |  | e2e-ios | 40.9 | 13.1 | 0.1 | 17/21 |
| 2026-10-03 18:40 | [37145063215](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37145063215) | 6904d0f | 35.6 | e2e-android | 21.2 | 19.9 | 0.0 | 12/21 |
|  | | |  | e2e-ios | 35.5 | 10.2 | 0.1 | 17/21 |
| 2026-10-03 14:53 | [37131281459](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37131281459) | 6904d0f | 29.0 | e2e-android | 18.4 | 17.3 | 0.0 | 12/21 |
|  | | |  | e2e-ios | 28.9 | 8.8 | 0.1 | 17/21 |
| 2026-10-03 10:23 | [37116242900](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37116242900) | 6904d0f | 37.4 | e2e-android | 21.3 | 20.0 | 0.0 | 12/21 |
|  | | |  | e2e-ios | 37.2 | 8.2 | 0.1 | 17/21 |
| 2026-10-02 23:53 | [37079664391](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37079664391) | 6904d0f | 51.1 | e2e-android | 21.9 | 20.6 | 0.0 | 12/21, 1 passed on retry |
|  | | |  | e2e-ios | 38.5 | 8.2 | 12.6 | 17/21 |
| 2026-10-02 20:22 | [37060147064](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37060147064) | - | 37.6 | e2e-android | 1.8 | 0.3 | 0.0 | failure |
|  | | |  | e2e-ios | 37.4 | 8.0 | 0.1 | 17/21 |

## Trend

![pager-view-android](charts/pager-view-android.svg)

![pager-view-ios](charts/pager-view-ios.svg)


## Retried test cases

Per run, from each job's log: a flow *failed at least once* if any of its attempts failed, inside its job (maestro-runner `--retries`, React Native's iOS per-flow attempts, agent-device, Expo's rounds) or in a retry job (React Native's retry_1/retry_2); it *passed on retry* if it then passed. *Extra flow runs* counts every run of a flow beyond its first, including whole-suite reruns of flows that had passed. Runs whose logs had expired are left out.

Each cell: **ours vs upstream**; the better one in bold. Ours is the newest maestro-runner build.

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing (ours / upstream) |
|---|---|---|---|---|---|---|---|---|---|
| android | e8a87b5 | 15 | 19.9 | 0% | 8.67 | 0% | 17.1 | 100% | nested_pagerView_example ×15, ensure-ltr ×15, ensure-rtl ×15 / - |
| ios | e8a87b5 | 16 | 10.1 | 0% | 3.12 | 0% | 6.0 | 100% | ensure-rtl ×16, verify-horizontal-rtl-swipe ×16, ensure-ltr ×14 / - |

Ours on earlier maestro-runner builds:

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing |
|---|---|---|---|---|---|---|---|---|---|
| android | 6904d0f | 16 | 19.8 | 0% | 8.19 | 0% | 16.1 | 100% | ensure-ltr ×16, ensure-rtl ×16, verify-horizontal-rtl-swipe ×16 |
| ios | 6904d0f | 17 | 8.8 | 0% | 3.06 | 0% | 6.1 | 100% | ensure-ltr ×17, ensure-rtl ×17, verify-horizontal-rtl-swipe ×17 |

### Per run

| Started (UTC) | Run | Platform | Side | Build | Flows | Failed at least once | Passed on retry (failed attempts) | Failed at the end | Extra flow runs | Retry jobs |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-07 01:15 | [37556168133](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37556168133) | ios | ours | e8a87b5 | 16 | 3 | on_page_selected_example (1), ensure-rtl (2) | verify-horizontal-rtl-swipe | 5 | 0 |
| 2026-10-07 01:15 | [37556168133](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37556168133) | android | ours | e8a87b5 | 16 | 8 | - | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 16 | 0 |
| 2026-10-06 22:40 | [37542075901](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37542075901) | ios | ours | e8a87b5 | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-06 20:00 | [37523142640](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37523142640) | android | ours | e8a87b5 | 16 | 9 | scrollable_pagerView_example (1) | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 17 | 0 |
| 2026-10-06 20:00 | [37523142640](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37523142640) | ios | ours | e8a87b5 | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-06 17:03 | [37500587061](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37500587061) | android | ours | e8a87b5 | 16 | 8 | - | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 16 | 0 |
| 2026-10-06 17:03 | [37500587061](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37500587061) | ios | ours | e8a87b5 | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-06 14:06 | [37476227210](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37476227210) | android | ours | e8a87b5 | 16 | 8 | - | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 16 | 0 |
| 2026-10-06 14:06 | [37476227210](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37476227210) | ios | ours | e8a87b5 | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-06 11:20 | [37455784759](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37455784759) | android | ours | e8a87b5 | 16 | 8 | - | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 16 | 0 |
| 2026-10-06 11:20 | [37455784759](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37455784759) | ios | ours | e8a87b5 | 16 | 4 | on_page_selected_example (1) | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 7 | 0 |
| 2026-10-06 08:35 | [37437104089](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37437104089) | android | ours | e8a87b5 | 16 | 8 | - | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 16 | 0 |
| 2026-10-06 08:35 | [37437104089](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37437104089) | ios | ours | e8a87b5 | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-06 06:00 | [37421376814](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37421376814) | android | ours | e8a87b5 | 16 | 8 | - | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 16 | 0 |
| 2026-10-06 06:00 | [37421376814](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37421376814) | ios | ours | e8a87b5 | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-06 03:25 | [37408909369](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37408909369) | ios | ours | e8a87b5 | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-06 03:25 | [37408909369](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37408909369) | android | ours | e8a87b5 | 16 | 8 | - | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 16 | 0 |
| 2026-10-06 00:55 | [37396517637](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37396517637) | ios | ours | e8a87b5 | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-06 00:55 | [37396517637](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37396517637) | android | ours | e8a87b5 | 16 | 8 | - | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 16 | 0 |
| 2026-10-05 22:30 | [37382904902](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37382904902) | ios | ours | e8a87b5 | 16 | 4 | on_page_selected_example (1) | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 7 | 0 |
| 2026-10-05 22:30 | [37382904902](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37382904902) | android | ours | e8a87b5 | 16 | 8 | nested_pagerView_example (2) | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 16 | 0 |
| 2026-10-05 19:12 | [37361709254](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37361709254) | ios | ours | e8a87b5 | 16 | 2 | ensure-rtl (2) | verify-horizontal-rtl-swipe | 4 | 0 |
| 2026-10-05 19:12 | [37361709254](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37361709254) | android | ours | e8a87b5 | 16 | 8 | - | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 16 | 0 |
| 2026-10-05 16:05 | [37338102242](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37338102242) | ios | ours | e8a87b5 | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-05 16:05 | [37338102242](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37338102242) | android | ours | e8a87b5 | 16 | 16 | - | material_top_bar_example, nested_pagerView_example, on_page_selected_example, ensure-ltr, open, verify-horizontal-ltr-swipe, verify-controls, ensure-rtl, verify-horizontal-rtl-swipe, verify-vertical-swipe, scrollable_pagerView_example, tab_view_inside_scroll_view_example, issue_1083_modal_set_page_repro, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 32 | 0 |
| 2026-10-05 13:09 | [37314639012](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37314639012) | ios | ours | e8a87b5 | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-05 13:09 | [37314639012](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37314639012) | android | ours | e8a87b5 | 16 | 8 | - | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 16 | 0 |
| 2026-10-05 10:03 | [37294100974](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37294100974) | ios | ours | e8a87b5 | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-05 10:03 | [37294100974](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37294100974) | android | ours | e8a87b5 | 16 | 9 | nested_pagerView_example (1), scrollable_pagerView_example (1) | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 16 | 0 |
| 2026-10-05 06:01 | [37270363181](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37270363181) | ios | ours | e8a87b5 | 16 | 4 | on_page_selected_example (1) | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 7 | 0 |
| 2026-10-05 06:01 | [37270363181](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37270363181) | android | ours | e8a87b5 | 16 | 8 | - | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 16 | 0 |
| 2026-10-05 05:21 | [37267388312](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37267388312) | ios | ours | 6904d0f | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-05 05:21 | [37267388312](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37267388312) | android | ours | 6904d0f | 16 | 8 | - | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 16 | 0 |
| 2026-10-05 03:18 | [37258886759](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37258886759) | android | ours | 6904d0f | 16 | 8 | - | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 16 | 0 |
| 2026-10-05 03:18 | [37258886759](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37258886759) | ios | ours | 6904d0f | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-05 01:19 | [37251013915](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37251013915) | android | ours | 6904d0f | 16 | 8 | - | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 16 | 0 |
| 2026-10-05 01:19 | [37251013915](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37251013915) | ios | ours | 6904d0f | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-04 23:11 | [37242871455](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37242871455) | android | ours | 6904d0f | 16 | 8 | - | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 16 | 0 |
| 2026-10-04 23:11 | [37242871455](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37242871455) | ios | ours | 6904d0f | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-04 21:13 | [37235208204](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37235208204) | android | ours | 6904d0f | 16 | 8 | - | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 16 | 0 |
| 2026-10-04 21:13 | [37235208204](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37235208204) | ios | ours | 6904d0f | 16 | 4 | on_page_selected_example (1) | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 7 | 0 |
| 2026-10-04 19:14 | [37227526658](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37227526658) | ios | ours | 6904d0f | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-04 19:14 | [37227526658](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37227526658) | android | ours | 6904d0f | 16 | 9 | scrollable_pagerView_example (1) | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 17 | 0 |
| 2026-10-04 17:11 | [37219557379](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37219557379) | ios | ours | 6904d0f | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-04 17:11 | [37219557379](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37219557379) | android | ours | 6904d0f | 16 | 8 | - | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 16 | 0 |
| 2026-10-04 15:08 | [37211869619](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37211869619) | ios | ours | 6904d0f | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-04 15:08 | [37211869619](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37211869619) | android | ours | 6904d0f | 16 | 8 | - | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 16 | 0 |
| 2026-10-04 13:00 | [37204069976](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37204069976) | ios | ours | 6904d0f | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-04 13:00 | [37204069976](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37204069976) | android | ours | 6904d0f | 16 | 7 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 14 | 0 |
| 2026-10-04 10:21 | [37195095621](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37195095621) | ios | ours | 6904d0f | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-04 10:21 | [37195095621](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37195095621) | android | ours | 6904d0f | 16 | 8 | - | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 16 | 0 |
| 2026-10-04 07:22 | [37185579132](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37185579132) | android | ours | 6904d0f | 16 | 9 | scrollable_pagerView_example (1) | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 17 | 0 |
| 2026-10-04 07:22 | [37185579132](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37185579132) | ios | ours | 6904d0f | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-04 05:30 | [37180075296](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37180075296) | android | ours | 6904d0f | 16 | 9 | nested_pagerView_example (2), issue_1083_modal_set_page_repro (1) | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 17 | 0 |
| 2026-10-04 05:30 | [37180075296](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37180075296) | ios | ours | 6904d0f | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-03 18:40 | [37145063215](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37145063215) | android | ours | 6904d0f | 16 | 8 | - | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 16 | 0 |
| 2026-10-03 18:40 | [37145063215](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37145063215) | ios | ours | 6904d0f | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-03 14:53 | [37131281459](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37131281459) | android | ours | 6904d0f | 16 | 8 | - | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 16 | 0 |
| 2026-10-03 14:53 | [37131281459](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37131281459) | ios | ours | 6904d0f | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-03 10:23 | [37116242900](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37116242900) | ios | ours | 6904d0f | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-03 10:23 | [37116242900](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37116242900) | android | ours | 6904d0f | 16 | 8 | - | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 16 | 0 |
| 2026-10-02 23:53 | [37079664391](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37079664391) | ios | ours | 6904d0f | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-02 23:53 | [37079664391](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37079664391) | android | ours | 6904d0f | 16 | 9 | scrollable_pagerView_example (1) | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 17 | 0 |
| 2026-10-02 20:22 | [37060147064](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37060147064) | ios | ours | 6904d0f | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
