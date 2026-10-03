# Bench results

Generated 2026-10-03 02:19 UTC from 428 e2e jobs.

Per project, platform and flavour: ours (maestro-runner) against upstream (Maestro, or agent-device for React Navigation). Times are the e2e test step only (no builds, no queue). First-attempt failures count flows that failed at least once before passing or failing for good; job retry rounds are React Native's retry_1/retry_2 jobs.

| Project | Platform | Flavour | Side | Runs | Median e2e (min) | Green runs | Runs with no first-attempt failure | First-attempt failures / run | Final failures / run | Runs needing a retry job | Runner |
|---|---|---|---|---|---|---|---|---|---|---|---|
| enriched-html | android | - | ours | 5 | 26.4 | 0/5 | 0/5 | 27.60 | 26.80 | 0/5 | ubuntu-latest | (builds: 49360bb, 6904d0f, ?)
| enriched-html | ios | - | ours | 7 | 33.5 | 0/7 | 0/7 | 10.57 | 8.86 | 0/7 | macos-26 | (builds: 49360bb, 6904d0f, ?)
| expo | android | - | ours | 6 | 22.4 | 3/6 | 0/6 | 3.33 | 2.67 | 0/6 | ubuntu-24.04 | (builds: 6904d0f, ?)
| expo | android | - | upstream | 6 | 14.2 | 6/6 | 3/6 | 1.33 | 0.67 | 0/6 | ubuntu-24.04 |
| expo | ios | - | ours | 6 | 11.4 | 3/6 | 1/6 | 1.50 | 1.00 | 0/6 | macos-26 | (builds: 6904d0f, ?)
| expo | ios | - | upstream | 6 | 15.7 | 5/6 | 5/6 | 0.17 | 0.00 | 0/6 | macos-26 |
| pager-view | android | - | ours | 4 | 19.1 | 0/4 | 0/3 | 9.33 | 9.00 | 0/4 | ubuntu-latest | (builds: 49360bb, 6904d0f, ?)
| pager-view | ios | - | ours | 3 | 8.2 | 0/3 | 0/3 | 4.00 | 4.00 | 0/3 | macos-26 | (builds: 6904d0f)
| react-native | android | debug | ours | 2 | 6.3 | 4/4 | 4/4 | 0.00 | 0.00 | 0/2 | ubuntu-latest | (builds: 6904d0f, ?)
| react-native | android | debug | upstream | 29 | 4.9 | 48/58 | 51/57 | 0.95 | 0.95 | 5/29 | 4-core-ubuntu |
| react-native | android | release | ours | 2 | 11.0 | 2/4 | 3/4 | 0.25 | 0.25 | 1/2 | ubuntu-latest | (builds: 6904d0f, ?)
| react-native | android | release | upstream | 29 | 15.1 | 48/58 | 51/57 | 2.63 | 2.63 | 5/29 | 4-core-ubuntu |
| react-native | ios | debug | ours | 2 | 22.5 | 3/3 | 2/3 | 0.33 | 0.00 | 0/2 | macos-26, macos-26-intel | (builds: 6904d0f, ?)
| react-native | ios | debug | upstream | 30 | 69.0 | 33/56 | 26/56 | 0.79 | 0.12 | 12/30 | macos-26-large |
| react-native | ios | release | ours | 2 | 25.1 | 3/3 | 2/3 | 0.33 | 0.00 | 0/2 | macos-26, macos-26-intel | (builds: 6904d0f, ?)
| react-native | ios | release | upstream | 30 | 63.9 | 34/57 | 42/57 | 0.32 | 0.12 | 12/30 | macos-26-large |
| react-navigation | android | - | ours | 4 | 26.1 | 4/4 | 4/4 | 0.00 | 0.00 | 0/4 | ubuntu-latest | (builds: 6904d0f, ?)
| react-navigation | android | - | upstream | 46 | 23.7 | 37/46 | 26/46 | 0.61 | 0.22 | 0/46 | ubuntu-latest |
| react-navigation | ios | - | ours | 5 | 19.5 | 5/5 | 3/5 | 0.40 | 0.00 | 0/5 | macos-latest | (builds: 6904d0f, ?)
| react-navigation | ios | - | upstream | 30 | 24.7 | 22/30 | 14/30 | 0.67 | 0.27 | 0/30 | macos-latest |

Upstream React Native runs its e2e jobs on larger runners (macos-*-large, 8-core-ubuntu); the bench fork uses the standard ones (macos-*-intel, ubuntu-latest).

