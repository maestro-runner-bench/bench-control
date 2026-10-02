# Bench results

Generated 2026-10-02 14:39 UTC from 327 e2e jobs.

Per project, platform and flavour: ours (maestro-runner) against upstream (Maestro, or agent-device for React Navigation). Times are the e2e test step only (no builds, no queue). First-attempt failures count flows that failed at least once before passing or failing for good; job retry rounds are React Native's retry_1/retry_2 jobs.

| Project | Platform | Flavour | Side | Runs | Median e2e (min) | Green runs | Runs with no first-attempt failure | First-attempt failures / run | Final failures / run | Runs needing a retry job | Runner |
|---|---|---|---|---|---|---|---|---|---|---|---|
| enriched-html | android | - | ours | 3 | 27.1 | 0/3 | 0/3 | 29.00 | 28.33 | 0/3 | ubuntu-latest |
| enriched-html | ios | - | ours | 3 | 33.5 | 0/3 | 0/3 | 18.67 | 17.33 | 0/3 | macos-26 |
| expo | android | - | ours | 4 | 27.9 | 1/4 | 0/4 | 4.50 | 3.75 | 0/4 | ubuntu-24.04 |
| expo | ios | - | ours | 4 | 11.4 | 1/4 | 1/4 | 1.75 | 1.50 | 0/4 | macos-26 |
| react-native | android | debug | ours | 1 | 6.3 | 2/2 | 2/2 | 0.00 | 0.00 | 0/1 | ubuntu-latest |
| react-native | android | debug | upstream | 29 | 4.9 | 48/58 | 51/57 | 0.95 | 0.95 | 5/29 | 4-core-ubuntu |
| react-native | android | release | ours | 1 | 11.7 | 0/2 | 1/2 | 0.50 | 0.50 | 1/1 | ubuntu-latest |
| react-native | android | release | upstream | 29 | 15.1 | 48/58 | 51/57 | 2.63 | 2.63 | 5/29 | 4-core-ubuntu |
| react-native | ios | debug | ours | 1 | 83.6 | 1/1 | 0/1 | 1.00 | 0.00 | 0/1 | macos-26-intel |
| react-native | ios | debug | upstream | 30 | 69.0 | 33/56 | 26/56 | 0.79 | 0.12 | 12/30 | macos-26-large |
| react-native | ios | release | ours | 1 | 69.5 | 1/1 | 0/1 | 1.00 | 0.00 | 0/1 | macos-26-intel |
| react-native | ios | release | upstream | 30 | 63.9 | 34/57 | 42/57 | 0.32 | 0.12 | 12/30 | macos-26-large |
| react-navigation | android | - | ours | 2 | 26.6 | 2/2 | 2/2 | 0.00 | 0.00 | 0/2 | ubuntu-latest |
| react-navigation | android | - | upstream | 16 | 23.5 | 16/16 | 8/16 | 0.56 | 0.00 | 0/16 | ubuntu-latest |
| react-navigation | ios | - | ours | 3 | 21.2 | 3/3 | 2/3 | 0.33 | 0.00 | 0/3 | macos-latest |

Upstream React Native runs its e2e jobs on larger runners (macos-*-large, 8-core-ubuntu); the bench fork uses the standard ones (macos-*-intel, ubuntu-latest).

