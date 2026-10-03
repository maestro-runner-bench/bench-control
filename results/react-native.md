# react-native

Upstream runs Maestro on larger runners (macos-*-large, 8-core-ubuntu); the bench fork uses the standard ones.

Times in minutes. *Run* is the whole workflow run (builds included); *job* is one job; *tests* is its test step only; *queue* is the wait for a runner.

## Summary

| Project | Platform | Flavour | Side | Build | Runs | Median e2e (min) | Green runs | Runs with no first-attempt failure | First-attempt failures / run | Final failures / run | Runs needing a retry job | Runner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| react-native | android | debug | ours | 6904d0f | 2 | 12.0 | 2/2 | 2/2 | 0.00 | 0.00 | 0/2 | ubuntu-latest |
| react-native | android | debug | ours | older | 1 | 9.7 | 1/1 | 1/1 | 0.00 | 0.00 | 0/1 | ubuntu-latest |
| react-native | android | debug | ours | 86ed2d7 | 1 | 11.7 | 1/1 | 1/1 | 0.00 | 0.00 | 0/1 | ubuntu-latest |
| react-native | android | debug | ours | d51beed | 1 | 13.4 | 0/1 | 0/1 | 1.00 | 1.00 | 1/1 | ubuntu-latest |
| react-native | android | debug | upstream | - | 86 | 18.4 | 75/86 | 54/58 | 1.72 | 1.72 | 11/86 | 4-core-ubuntu |
| react-native | android | debug (template app) | ours | 6904d0f | 2 | 2.8 | 2/2 | 2/2 | 0.00 | 0.00 | 0/2 | ubuntu-latest |
| react-native | android | debug (template app) | ours | older | 1 | 2.8 | 0/1 | 1/1 | 0.00 | 0.00 | 1/1 | ubuntu-latest |
| react-native | android | debug (template app) | ours | 86ed2d7 | 1 | 2.5 | 1/1 | 1/1 | 0.00 | 0.00 | 0/1 | ubuntu-latest |
| react-native | android | debug (template app) | ours | d51beed | 1 | 3.1 | 1/1 | 1/1 | 0.00 | 0.00 | 0/1 | ubuntu-latest |
| react-native | android | debug (template app) | upstream | - | 85 | 3.2 | 78/85 | 53/59 | 0.10 | 0.10 | 7/85 | 4-core-ubuntu |
| react-native | android | release | ours | 6904d0f | 2 | 15.5 | 2/2 | 2/2 | 0.00 | 0.00 | 0/2 | ubuntu-latest |
| react-native | android | release | ours | older | 1 | 16.1 | 1/1 | 1/1 | 0.00 | 0.00 | 0/1 | ubuntu-latest |
| react-native | android | release | ours | 86ed2d7 | 1 | 15.9 | 1/1 | 1/1 | 0.00 | 0.00 | 0/1 | ubuntu-latest |
| react-native | android | release | ours | d51beed | 1 | 14.4 | 0/1 | 0/1 | 22.00 | 22.00 | 1/1 | ubuntu-latest |
| react-native | android | release | upstream | - | 86 | 27.5 | 76/86 | 55/59 | 3.32 | 3.32 | 10/86 | 4-core-ubuntu |
| react-native | android | release (template app) | ours | 6904d0f | 2 | 2.2 | 2/2 | 2/2 | 0.00 | 0.00 | 0/2 | ubuntu-latest |
| react-native | android | release (template app) | ours | older | 1 | 7.3 | 0/1 | 0/1 | 1.00 | 1.00 | 1/1 | ubuntu-latest |
| react-native | android | release (template app) | ours | 86ed2d7 | 1 | 2.2 | 1/1 | 1/1 | 0.00 | 0.00 | 0/1 | ubuntu-latest |
| react-native | android | release (template app) | ours | d51beed | 1 | 2.3 | 1/1 | 1/1 | 0.00 | 0.00 | 0/1 | ubuntu-latest |
| react-native | android | release (template app) | upstream | - | 85 | 2.5 | 78/85 | 53/58 | 0.09 | 0.09 | 7/85 | 4-core-ubuntu |
| react-native | ios | debug | ours | 6904d0f | 2 | 21.0 | 2/2 | 2/2 | 0.00 | 0.00 | 0/2 | macos-26 |
| react-native | ios | debug | ours | older | 1 | 83.6 | 1/1 | 0/1 | 1.00 | 0.00 | 0/1 | macos-26-intel |
| react-native | ios | debug | ours | 86ed2d7 | 1 | - | 0/1 | 0/1 | 33.00 | 33.00 | 0/1 | macos-26-intel |
| react-native | ios | debug | ours | d51beed | 1 | - | 0/1 | 0/1 | 1.00 | 1.00 | 0/1 | macos-26-intel |
| react-native | ios | debug | upstream | - | 88 | 75.1 | 67/87 | 10/59 | 1.15 | 0.14 | 21/88 | macos-15-large, macos-26-large |
| react-native | ios | debug (template app) | ours | 6904d0f | 2 | 14.7 | 2/2 | 2/2 | 0.00 | 0.00 | 0/2 | macos-26-intel |
| react-native | ios | debug (template app) | ours | 86ed2d7 | 1 | 13.2 | 1/1 | 1/1 | 0.00 | 0.00 | 0/1 | macos-26-intel |
| react-native | ios | debug (template app) | ours | d51beed | 1 | 1.9 | 0/1 | - | - | - | 1/1 | macos-26-intel |
| react-native | ios | debug (template app) | upstream | - | 81 | 10.1 | 80/81 | 49/56 | 0.12 | 0.00 | 1/81 | macos-15-large, macos-26-large |
| react-native | ios | release | ours | 6904d0f | 2 | 21.9 | 2/2 | 2/2 | 0.00 | 0.00 | 0/2 | macos-26 |
| react-native | ios | release | ours | older | 1 | 69.5 | 1/1 | 0/1 | 1.00 | 0.00 | 0/1 | macos-26-intel |
| react-native | ios | release | ours | 86ed2d7 | 1 | - | 0/1 | 0/1 | 32.00 | 32.00 | 0/1 | macos-26-intel |
| react-native | ios | release | ours | d51beed | 1 | - | 0/1 | 0/1 | 1.00 | 1.00 | 0/1 | macos-26-intel |
| react-native | ios | release | upstream | - | 88 | 72.6 | 67/88 | 32/59 | 0.53 | 0.24 | 21/88 | macos-15-large, macos-26-large |
| react-native | ios | release (template app) | ours | 6904d0f | 2 | 10.8 | 2/2 | 2/2 | 0.00 | 0.00 | 0/2 | macos-26-intel |
| react-native | ios | release (template app) | ours | 86ed2d7 | 1 | 8.4 | 1/1 | 1/1 | 0.00 | 0.00 | 0/1 | macos-26-intel |
| react-native | ios | release (template app) | ours | d51beed | 1 | 10.5 | 0/1 | 1/1 | 0.00 | 0.00 | 1/1 | macos-26-intel |
| react-native | ios | release (template app) | upstream | - | 80 | 9.2 | 79/80 | 56/56 | 0.00 | 0.00 | 1/80 | macos-15-large, macos-26-large |

## Runs: maestro-runner (bench fork)

| Started (UTC) | Run | Build | Run time | Job | Job time | Tests | Queue | Result |
|---|---|---|---|---|---|---|---|---|
| 2026-10-03 03:23 | [37093048002](https://github.com/maestro-runner-bench/react-native/actions/runs/37093048002) | 6904d0f | 130.9 | android_rntester (debug) | 12.3 | 11.6 | 0.0 | 27/27 |
|  | | |  | android_rntester (release) | 17.1 | 16.3 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.0 | 3.0 | 0.0 | 1/1 |
|  | | |  | android_templateapp (release) | 3.0 | 2.2 | 0.0 | 1/1 |
|  | | |  | ios_rntester (Debug) | 20.6 | 19.4 | 0.1 | 48/48 |
|  | | |  | ios_rntester (Release) | 19.6 | 18.8 | 0.1 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 27.6 | 19.3 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 10.0 | 6.1 | 0.1 | 1/1 |
| 2026-10-02 21:58 | [37069938487](https://github.com/maestro-runner-bench/react-native/actions/runs/37069938487) | 6904d0f | 144.4 | android_rntester (debug) | 13.1 | 12.4 | 0.0 | 27/27 |
|  | | |  | android_rntester (release) | 15.6 | 14.8 | 0.0 | 51/51 |
|  | | |  | android_templateapp (debug) | 4.8 | 2.7 | 0.0 | 1/1 |
|  | | |  | android_templateapp (release) | 3.0 | 2.2 | 0.0 | 1/1 |
|  | | |  | ios_rntester (Debug) | 23.8 | 22.5 | 17.2 | 48/48 |
|  | | |  | ios_rntester (Release) | 26.6 | 25.1 | 1.2 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 17.5 | 10.0 | 12.6 | 1/1 |
|  | | |  | ios_templateapp (Release) | 23.5 | 15.5 | 7.6 | 1/1 |
| 2026-10-02 09:51 | [36992149427](https://github.com/maestro-runner-bench/react-native/actions/runs/36992149427) | maestro-runner 1.1.28.1 | 214.1 | android_rntester (debug) | 10.8 | 9.7 | 0.0 | 27/27 |
|  | | |  | android_rntester (release) | 17.4 | 16.1 | 0.0 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.0 | 2.8 | 0.0 | 1/1 |
|  | | |  | android_templateapp (release) | 8.1 | 7.3 | 0.0 | 0/1 |
|  | | |  | android_templateapp_retry_1 (debug) | 2.1 | - | 0.0 | failed before tests |
|  | | |  | android_templateapp_retry_1 (release) | 3.2 | 2.3 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 87.9 | 83.6 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 72.7 | 69.5 | 0.1 | 48/48, 1 passed on retry |
| 2026-10-01 19:51 | [36917319965](https://github.com/maestro-runner-bench/react-native/actions/runs/36917319965) | 86ed2d7 | 577.4 | android_rntester (debug) | 12.4 | 11.7 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 16.7 | 15.9 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 4.5 | 2.5 | 0.0 | 1/1 |
|  | | |  | android_templateapp (release) | 3.0 | 2.2 | 0.0 | 1/1 |
|  | | |  | ios_rntester (Debug) | 318.0 | 314.4 | 24.5 | cancelled during tests (time limit or by hand) |
|  | | |  | ios_rntester (Release) | 320.6 | 318.0 | 20.9 | cancelled during tests (time limit or by hand) |
|  | | |  | ios_templateapp (Debug) | 20.3 | 13.2 | 30.5 | 1/1 |
|  | | |  | ios_templateapp (Release) | 12.4 | 8.4 | 18.0 | 1/1 |
| 2026-10-01 17:17 | [36898270680](https://github.com/maestro-runner-bench/react-native/actions/runs/36898270680) | d51beed | 171.2 | android_rntester (debug) | 14.7 | 13.4 | 0.0 | 26/27 |
|  | | |  | android_rntester (release) | 15.8 | 14.4 | 0.1 | 29/51 |
|  | | |  | android_rntester_retry_1 (debug) | 4.4 | 3.6 | 0.0 | 0/1 |
|  | | |  | android_rntester_retry_1 (release) | 8.4 | 7.6 | 0.0 | 2/22 |
|  | | |  | android_rntester_retry_2 (debug) | 4.9 | 3.9 | 0.1 | 0/1 |
|  | | |  | android_rntester_retry_2 (release) | 8.3 | 7.5 | 0.0 | 2/20 |
|  | | |  | android_templateapp (debug) | 5.3 | 3.1 | 0.0 | 1/1 |
|  | | |  | android_templateapp (release) | 3.2 | 2.3 | 0.0 | 1/1 |
|  | | |  | ios_rntester (Debug) | 28.8 | 26.4 | 0.1 | cancelled during tests (time limit or by hand) |
|  | | |  | ios_rntester (Release) | 29.3 | 25.7 | 0.1 | cancelled during tests (time limit or by hand) |
|  | | |  | ios_templateapp (Debug) | 13.3 | 1.9 | 0.1 | success |
|  | | |  | ios_templateapp (Release) | 15.8 | 10.5 | 0.1 | 1/1 |
|  | | |  | ios_templateapp_retry_1 (Debug) | 21.9 | 14.2 | 0.1 | 1/1 |
|  | | |  | ios_templateapp_retry_1 (Release) | 15.2 | 10.0 | 0.1 | 1/1 |

## Runs: upstream

| Started (UTC) | Run | Build | Run time | Job | Job time | Tests | Queue | Result |
|---|---|---|---|---|---|---|---|---|
| 2026-10-03 00:39 | [37082951955](https://github.com/react/react-native/actions/runs/37082951955) | maestro | 128.3 | android_rntester (debug) | 19.8 | 18.8 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 28.7 | 27.6 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.6 | 3.1 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.5 | 2.4 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 88.8 | 87.4 | 0.1 | 48/48, 2 passed on retry |
|  | | |  | ios_rntester (Release) | 85.9 | 84.6 | 0.1 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 19.5 | 14.0 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 15.4 | 12.7 | 0.1 | 1/1 |
| 2026-10-02 19:41 | [37055799075](https://github.com/react/react-native/actions/runs/37055799075) | maestro | 135.5 | android_rntester (debug) | 20.8 | 19.2 | 0.3 | 27/27 |
|  | | |  | android_rntester (release) | 28.4 | 27.5 | 0.3 | 51/51 |
|  | | |  | android_templateapp (debug) | 6.7 | 4.2 | 0.1 | 0/1 |
|  | | |  | android_templateapp (release) | 3.7 | 2.5 | 0.1 | 1/1 |
|  | | |  | android_templateapp_retry_1 (debug) | 5.5 | 3.2 | 0.2 | 1/1 |
|  | | |  | ios_rntester (Debug) | 78.5 | 77.5 | 0.2 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 88.0 | 86.6 | 0.2 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 15.4 | 9.8 | 0.4 | 1/1 |
|  | | |  | ios_templateapp (Release) | 13.4 | 9.6 | 0.4 | 1/1 |
| 2026-10-02 18:13 | [37045943779](https://github.com/react/react-native/actions/runs/37045943779) | maestro | 137.4 | android_rntester (debug) | 43.4 | 42.4 | 0.3 | 2/27 |
|  | | |  | android_rntester (release) | 29.2 | 28.3 | 0.3 | 51/51 |
|  | | |  | android_rntester_retry_1 (debug) | 19.1 | 18.1 | 0.3 | 27/27 |
|  | | |  | android_templateapp (debug) | 6.0 | 3.5 | 0.3 | 1/1 |
|  | | |  | android_templateapp (release) | 3.7 | 2.8 | 0.3 | 1/1 |
|  | | |  | ios_rntester (Debug) | 84.5 | 83.1 | 0.2 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 73.5 | 72.3 | 0.2 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 15.2 | 10.6 | 0.6 | 1/1 |
|  | | |  | ios_templateapp (Release) | 12.2 | 10.0 | 0.6 | 1/1 |
| 2026-10-02 16:57 | [37037432937](https://github.com/react/react-native/actions/runs/37037432937) | maestro | 125.1 | android_rntester (debug) | 20.2 | 19.1 | 0.6 | 27/27 |
|  | | |  | android_rntester (release) | 27.7 | 26.7 | 0.9 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.6 | 3.2 | 0.2 | 1/1 |
|  | | |  | android_templateapp (release) | 3.5 | 2.5 | 0.2 | 1/1 |
|  | | |  | ios_rntester (Debug) | 74.7 | 73.4 | 0.3 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 80.7 | 79.0 | 0.3 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 15.3 | 9.2 | 0.2 | 1/1 |
|  | | |  | ios_templateapp (Release) | 11.6 | 8.4 | 0.2 | 1/1 |
| 2026-10-02 16:50 | [37036694926](https://github.com/react/react-native/actions/runs/37036694926) | maestro | 130.3 | android_rntester (debug) | 19.9 | 18.8 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 28.2 | 27.2 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.8 | 3.3 | 0.2 | 1/1 |
|  | | |  | android_templateapp (release) | 3.5 | 2.5 | 0.2 | 1/1 |
|  | | |  | ios_rntester (Debug) | 80.6 | 79.2 | 0.2 | 48/48 |
|  | | |  | ios_rntester (Release) | 87.0 | 85.7 | 0.2 | 48/48, 1 passed on retry |
|  | | |  | ios_templateapp (Debug) | 14.3 | 8.7 | 0.3 | 1/1 |
|  | | |  | ios_templateapp (Release) | 11.2 | 8.4 | 0.3 | 1/1 |
| 2026-10-02 16:46 | [37036180664](https://github.com/react/react-native/actions/runs/37036180664) | maestro | 144.0 | android_rntester (debug) | 19.3 | 18.3 | 0.2 | 27/27 |
|  | | |  | android_rntester (release) | 28.2 | 27.2 | 0.2 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.5 | 3.0 | 0.3 | 1/1 |
|  | | |  | android_templateapp (release) | 3.4 | 2.5 | 0.3 | 1/1 |
|  | | |  | ios_rntester (Debug) | 96.8 | 95.4 | 0.3 | 48/48, 2 passed on retry |
|  | | |  | ios_rntester (Release) | 76.0 | 74.7 | 0.3 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 16.6 | 10.6 | 0.3 | 1/1 |
|  | | |  | ios_templateapp (Release) | 12.3 | 9.2 | 0.3 | 1/1 |
| 2026-10-02 15:44 | [37029138076](https://github.com/react/react-native/actions/runs/37029138076) | maestro | 126.2 | android_rntester (debug) | 19.1 | 18.1 | 0.2 | 27/27 |
|  | | |  | android_rntester (release) | 27.7 | 26.6 | 0.2 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.9 | 3.4 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.2 | 2.2 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 79.5 | 78.3 | 0.2 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 73.7 | 72.3 | 0.2 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 15.7 | 11.2 | 0.2 | 1/1 |
| 2026-10-02 15:41 | [37028747659](https://github.com/react/react-native/actions/runs/37028747659) | maestro | 126.2 | android_rntester (debug) | 18.5 | 17.5 | 0.2 | 27/27 |
|  | | |  | android_rntester (release) | 29.6 | 28.6 | 0.2 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.8 | 3.4 | 0.2 | 1/1 |
|  | | |  | android_templateapp (release) | 3.5 | 2.5 | 0.2 | 1/1 |
|  | | |  | ios_rntester (Debug) | 79.5 | 78.2 | 0.2 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 80.8 | 79.6 | 0.2 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 16.3 | 11.6 | 0.3 | 1/1 |
|  | | |  | ios_templateapp (Release) | 14.5 | 11.7 | 0.3 | 1/1 |
| 2026-10-02 15:33 | [37027808769](https://github.com/react/react-native/actions/runs/37027808769) | maestro | 236.9 | android_rntester (debug) | 23.3 | 22.2 | 0.2 | 27/27 |
|  | | |  | android_rntester (release) | 29.4 | 28.4 | 0.2 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.5 | 3.2 | 0.2 | 1/1 |
|  | | |  | android_templateapp (release) | 3.6 | 2.5 | 0.2 | 1/1 |
|  | | |  | ios_rntester (Debug) | 102.6 | 101.2 | 0.2 | 43/44 |
|  | | |  | ios_rntester (Release) | 68.7 | 67.5 | 0.2 | 48/48 |
|  | | |  | ios_rntester_retry_1 (Debug) | 83.9 | 82.4 | 0.4 | 48/48, 2 passed on retry |
|  | | |  | ios_rntester_retry_1 (Release) | 76.5 | 75.2 | 0.3 | 48/48, 1 passed on retry |
|  | | |  | ios_templateapp (Debug) | 20.2 | 14.2 | 0.2 | 1/1 |
|  | | |  | ios_templateapp (Release) | 12.0 | 9.8 | 0.2 | 1/1 |
| 2026-10-02 14:31 | [37020483607](https://github.com/react/react-native/actions/runs/37020483607) | maestro | 354.3 | android_rntester (debug) | 20.5 | 19.6 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 54.1 | 53.0 | 0.1 | 2/51 |
|  | | |  | android_rntester_retry_1 (release) | 28.6 | 27.6 | 0.2 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.6 | 3.2 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.4 | 2.4 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Release) | 77.8 | 76.6 | 0.2 | 48/48 |
|  | | |  | ios_rntester_retry_1 (Debug) | 111.6 | 110.2 | 0.1 | 24/25 |
|  | | |  | ios_rntester_retry_1 (Release) | 96.2 | 94.9 | 0.1 | 43/44 |
|  | | |  | ios_rntester_retry_2 (Debug) | 80.8 | 79.6 | 0.3 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester_retry_2 (Release) | 84.1 | 82.8 | 0.3 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 18.1 | 11.3 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 11.2 | 8.0 | 0.1 | 1/1 |
| 2026-10-02 11:55 | [37003745333](https://github.com/react/react-native/actions/runs/37003745333) | maestro | 306.4 | android_rntester (debug) | 21.6 | 20.6 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 29.4 | 28.4 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.8 | 3.3 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.6 | 2.6 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 69.3 | 68.2 | 0.2 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 84.0 | 82.7 | 0.2 | 43/44 |
|  | | |  | ios_rntester_retry_1 (Debug) | 98.1 | 96.5 | 0.2 | 43/44 |
|  | | |  | ios_rntester_retry_1 (Release) | 93.1 | 91.5 | 0.2 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester_retry_2 (Debug) | 77.5 | 76.2 | 0.2 | 48/48 |
|  | | |  | ios_rntester_retry_2 (Release) | 73.8 | 72.5 | 0.2 | 48/48, 1 passed on retry |
|  | | |  | ios_templateapp (Debug) | 18.4 | 13.7 | 0.1 | 1/1, 1 passed on retry |
|  | | |  | ios_templateapp (Release) | 11.5 | 9.5 | 0.1 | 1/1 |
| 2026-10-02 11:09 | [36999455988](https://github.com/react/react-native/actions/runs/36999455988) | maestro | 141.2 | android_rntester (debug) | 22.0 | 20.9 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 30.5 | 29.5 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 6.1 | 3.6 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.7 | 2.7 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 94.9 | 93.5 | 0.1 | 48/48, 2 passed on retry |
|  | | |  | ios_rntester (Release) | 71.0 | 69.8 | 0.1 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 14.5 | 10.0 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 13.5 | 10.8 | 0.1 | 1/1 |
| 2026-10-02 10:46 | [36997293926](https://github.com/react/react-native/actions/runs/36997293926) | maestro | 129.4 | android_rntester (debug) | 19.3 | 18.3 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 30.4 | 29.4 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.6 | 3.3 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.6 | 2.6 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 75.5 | 74.2 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 69.6 | 68.5 | 0.1 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 16.8 | 11.9 | 0.1 | 1/1, 1 passed on retry |
|  | | |  | ios_templateapp (Release) | 11.8 | 9.6 | 0.1 | 1/1 |
| 2026-10-02 10:33 | [36996153294](https://github.com/react/react-native/actions/runs/36996153294) | maestro | 390.5 | android_rntester (debug) | 19.9 | 18.8 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 28.4 | 27.4 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.7 | 3.3 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.8 | 2.7 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 74.2 | 73.0 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 94.3 | 93.0 | 0.1 | 43/44 |
|  | | |  | ios_rntester_retry_1 (Debug) | 73.0 | 71.8 | 0.2 | 48/48 |
|  | | |  | ios_rntester_retry_1 (Release) | 140.9 | 138.8 | 0.2 | 43/44, 1 passed on retry |
|  | | |  | ios_rntester_retry_2 (Debug) | 107.0 | 105.6 | 0.1 | 43/44 |
|  | | |  | ios_rntester_retry_2 (Release) | 67.1 | 65.9 | 0.1 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 14.1 | 10.0 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 11.2 | 9.1 | 0.1 | 1/1 |
| 2026-10-02 10:09 | [36993916028](https://github.com/react/react-native/actions/runs/36993916028) | maestro | 141.8 | android_rntester (debug) | 19.4 | 18.4 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 27.2 | 26.3 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.6 | 3.2 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.7 | 2.6 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 76.3 | 75.1 | 0.1 | 48/48 |
|  | | |  | ios_rntester (Release) | 93.4 | 92.2 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_templateapp (Debug) | 17.6 | 12.6 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 12.3 | 9.8 | 0.1 | 1/1 |
| 2026-10-02 09:36 | [36990729679](https://github.com/react/react-native/actions/runs/36990729679) | maestro | 136.1 | android_rntester (debug) | 19.4 | 18.4 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 30.4 | 29.3 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.8 | 3.4 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.4 | 2.4 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 89.2 | 87.8 | 0.1 | 48/48 |
|  | | |  | ios_rntester (Release) | 79.9 | 78.7 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_templateapp (Debug) | 13.2 | 9.1 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 11.4 | 9.3 | 0.1 | 1/1 |
| 2026-10-02 09:19 | [36989076382](https://github.com/react/react-native/actions/runs/36989076382) | maestro | 220.0 | android_rntester (debug) | 19.3 | 18.3 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 29.1 | 28.1 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.7 | 3.3 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 4.3 | 3.4 | 0.1 | 0/1 |
|  | | |  | android_templateapp_retry_1 (release) | 4.5 | 3.5 | 0.1 | 0/1 |
|  | | |  | android_templateapp_retry_2 (release) | 3.5 | 2.5 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 97.3 | 95.9 | 0.1 | 48/48, 2 passed on retry |
|  | | |  | ios_rntester (Release) | 90.7 | 89.3 | 0.1 | 43/44 |
|  | | |  | ios_rntester_retry_1 (Debug) | 76.0 | 74.8 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester_retry_1 (Release) | 75.5 | 74.3 | 0.1 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 14.6 | 9.2 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 12.5 | 9.0 | 0.1 | 1/1 |
| 2026-10-01 20:02 | [36918732275](https://github.com/react/react-native/actions/runs/36918732275) | maestro | 157.4 | android_rntester (debug) | 19.3 | 18.5 | 0.5 | 27/27 |
|  | | |  | android_rntester (release) | 26.9 | 26.2 | 0.2 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.5 | 3.3 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.4 | 2.6 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 81.6 | 79.8 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_templateapp (Debug) | 15.3 | 10.4 | 0.2 | 1/1 |
|  | | |  | ios_templateapp (Release) | 14.8 | 11.9 | 0.2 | 1/1 |
| 2026-10-01 19:22 | [36913783613](https://github.com/react/react-native/actions/runs/36913783613) | maestro | 145.1 | android_rntester (debug) | 18.9 | 18.1 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 28.1 | 27.3 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.8 | 3.2 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.7 | 2.4 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 80.1 | 78.1 | 0.2 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 90.3 | 88.2 | 0.2 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 14.0 | 7.8 | 0.2 | 1/1 |
|  | | |  | ios_templateapp (Release) | 13.2 | 9.2 | 0.2 | 1/1 |
| 2026-10-01 18:26 | [36906859420](https://github.com/react/react-native/actions/runs/36906859420) | maestro | 140.4 | android_rntester (debug) | 41.5 | 40.4 | 0.2 | 2/27 |
|  | | |  | android_rntester (release) | 28.7 | 27.9 | 0.2 | 51/51 |
|  | | |  | android_rntester_retry_1 (debug) | 18.8 | 18.1 | 0.3 | 27/27 |
|  | | |  | android_templateapp (debug) | 5.7 | 3.6 | 0.2 | 1/1 |
|  | | |  | android_templateapp (release) | 3.4 | 2.7 | 0.2 | 1/1 |
|  | | |  | ios_rntester (Debug) | 88.3 | 87.0 | 0.2 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 79.9 | 78.6 | 0.2 | 48/48, 1 passed on retry |
|  | | |  | ios_templateapp (Debug) | 17.1 | 10.1 | 0.3 | 1/1 |
|  | | |  | ios_templateapp (Release) | 12.2 | 8.7 | 0.3 | 1/1 |
| 2026-10-01 17:45 | [36901698066](https://github.com/react/react-native/actions/runs/36901698066) | maestro | 224.4 | android_rntester (debug) | 18.9 | 17.8 | 0.2 | 27/27 |
|  | | |  | android_rntester (release) | 31.4 | 30.2 | 0.2 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.7 | 3.4 | 0.3 | 1/1 |
|  | | |  | android_templateapp (release) | 3.2 | 2.4 | 0.3 | 1/1 |
|  | | |  | ios_rntester (Debug) | 78.9 | 77.4 | 0.2 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 96.3 | 94.8 | 0.3 | 43/44 |
|  | | |  | ios_rntester_retry_1 (Debug) | 78.9 | 77.7 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester_retry_1 (Release) | 65.7 | 64.7 | 0.1 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 18.3 | 12.5 | 0.2 | 1/1 |
|  | | |  | ios_templateapp (Release) | 13.4 | 11.2 | 0.2 | 1/1 |
| 2026-10-01 17:32 | [36900091671](https://github.com/react/react-native/actions/runs/36900091671) | maestro | 213.7 | android_rntester (debug) | 20.6 | 19.7 | 0.2 | 27/27 |
|  | | |  | android_rntester (release) | 28.6 | 27.9 | 0.2 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.9 | 3.4 | 0.3 | 1/1 |
|  | | |  | android_templateapp (release) | 3.6 | 2.5 | 0.3 | 1/1 |
|  | | |  | ios_rntester (Debug) | 79.9 | 78.1 | 0.2 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 84.8 | 83.4 | 0.2 | 43/44 |
|  | | |  | ios_rntester_retry_1 (Debug) | 81.0 | 79.7 | 0.2 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester_retry_1 (Release) | 66.2 | 64.9 | 0.2 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 16.0 | 9.9 | 0.2 | 1/1 |
|  | | |  | ios_templateapp (Release) | 11.3 | 8.1 | 0.2 | 1/1 |
| 2026-10-01 17:47 | [36882464491](https://github.com/react/react-native/actions/runs/36882464491) | maestro | 8.3 | android_rntester (debug) | 19.1 | 18.3 | -136.7 | 27/27 |
|  | | |  | android_rntester (release) | 27.8 | 27.0 | -136.7 | 51/51 |
|  | | |  | android_templateapp (debug) | 9.0 | 3.5 | -95.2 | 0/1 |
|  | | |  | android_templateapp (release) | 4.9 | 3.5 | -95.2 | 0/1 |
|  | | |  | android_templateapp_retry_1 (debug) | 6.3 | 3.4 | -85.8 | 1/1 |
|  | | |  | android_templateapp_retry_1 (release) | 3.2 | 2.4 | -85.8 | 1/1 |
|  | | |  | ios_rntester (Debug) | 77.3 | 75.6 | -94.5 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 82.4 | 80.6 | -94.5 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 15.4 | 9.5 | -91.9 | 1/1 |
|  | | |  | ios_templateapp (Release) | 12.8 | 8.5 | -91.9 | 1/1 |
| 2026-10-01 14:27 | [36876534417](https://github.com/react/react-native/actions/runs/36876534417) | maestro | 135.5 | android_rntester (debug) | 19.2 | 18.4 | 0.2 | 27/27 |
|  | | |  | android_rntester (release) | 27.0 | 26.3 | 0.2 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.8 | 3.6 | 0.2 | 1/1 |
|  | | |  | android_templateapp (release) | 3.2 | 2.5 | 0.2 | 1/1 |
|  | | |  | ios_rntester (Debug) | 72.5 | 71.3 | 0.2 | 48/48 |
|  | | |  | ios_rntester (Release) | 91.1 | 89.8 | 0.2 | 48/48, 1 passed on retry |
|  | | |  | ios_templateapp (Debug) | 15.7 | 11.2 | 0.2 | 1/1 |
|  | | |  | ios_templateapp (Release) | 11.9 | 9.8 | 0.2 | 1/1 |
| 2026-10-01 14:17 | [36875235571](https://github.com/react/react-native/actions/runs/36875235571) | maestro | 316.5 | android_rntester (debug) | 19.9 | 19.1 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 28.6 | 27.9 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.5 | 3.4 | 0.2 | 1/1 |
|  | | |  | android_templateapp (release) | 3.4 | 2.6 | 0.2 | 1/1 |
|  | | |  | ios_rntester (Debug) | 76.3 | 75.1 | 0.4 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 93.6 | 92.2 | 0.4 | 43/44, 1 passed on retry |
|  | | |  | ios_rntester_retry_1 (Debug) | 79.7 | 77.7 | 0.2 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester_retry_1 (Release) | 84.6 | 82.9 | 0.2 | 43/44, 1 passed on retry |
|  | | |  | ios_rntester_retry_2 (Debug) | 72.6 | 71.3 | 0.2 | 48/48 |
|  | | |  | ios_rntester_retry_2 (Release) | 86.3 | 85.1 | 0.2 | 48/48, 1 passed on retry |
|  | | |  | ios_templateapp (Debug) | 20.1 | 14.0 | 0.2 | 1/1 |
|  | | |  | ios_templateapp (Release) | 11.7 | 9.5 | 0.2 | 1/1 |
| 2026-10-01 13:14 | [36867264862](https://github.com/react/react-native/actions/runs/36867264862) | maestro | 124.3 | android_rntester (debug) | 21.2 | 20.4 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 28.9 | 28.1 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 9.5 | 3.1 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.1 | 2.4 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 78.0 | 76.5 | 0.2 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 76.9 | 75.5 | 0.2 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 17.0 | 10.6 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 11.8 | 9.4 | 0.1 | 1/1 |
| 2026-10-01 13:06 | [36866271124](https://github.com/react/react-native/actions/runs/36866271124) | maestro | 247.7 | android_rntester (debug) | 21.0 | 19.7 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 32.6 | 31.8 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.4 | 3.2 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.2 | 2.4 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 81.9 | 80.7 | 0.1 | 48/48, 2 passed on retry |
|  | | |  | ios_rntester (Release) | 119.4 | 118.2 | 0.1 | 38/39 |
|  | | |  | ios_rntester_retry_1 (Debug) | 77.2 | 75.9 | 0.2 | 48/48 |
|  | | |  | ios_rntester_retry_1 (Release) | 65.6 | 64.5 | 0.2 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 14.3 | 10.2 | 0.2 | 1/1 |
|  | | |  | ios_templateapp (Release) | 11.8 | 9.7 | 0.2 | 1/1 |
| 2026-10-01 12:47 | [36864159166](https://github.com/react/react-native/actions/runs/36864159166) | maestro | 120.7 | android_rntester (debug) | 20.9 | 20.1 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 30.4 | 29.7 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.5 | 3.2 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.3 | 2.5 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 74.6 | 73.3 | 0.2 | 48/48 |
|  | | |  | ios_rntester (Release) | 74.2 | 73.0 | 0.1 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 15.9 | 10.1 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 11.9 | 8.4 | 0.1 | 1/1 |
| 2026-10-01 12:42 | [36863586697](https://github.com/react/react-native/actions/runs/36863586697) | maestro | 136.1 | android_rntester (debug) | 18.9 | 18.1 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 31.1 | 30.4 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.3 | 3.2 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.6 | 2.8 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 86.5 | 85.0 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 76.0 | 74.7 | 0.1 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 13.9 | 8.6 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 12.9 | 9.6 | 0.1 | 1/1 |
| 2026-10-01 09:56 | [36845916549](https://github.com/react/react-native/actions/runs/36845916549) | maestro | 139.3 | android_rntester (debug) | 19.7 | 18.7 | 0.6 | 27/27 |
|  | | |  | android_rntester (release) | 28.3 | 27.2 | 0.5 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.6 | 3.3 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.8 | 2.8 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 86.8 | 85.5 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 80.4 | 79.2 | 0.1 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 14.8 | 10.0 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 11.4 | 9.5 | 0.1 | 1/1 |
| 2026-09-30 23:35 | [36791912465](https://github.com/react/react-native/actions/runs/36791912465) | maestro | 117.9 | android_rntester (debug) | 19.4 | 18.4 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 29.2 | 28.3 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.5 | 3.1 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.4 | 2.5 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 75.0 | 73.7 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 74.2 | 72.8 | 0.1 | 48/48 |
| 2026-09-30 21:24 | [36779183435](https://github.com/react/react-native/actions/runs/36779183435) | maestro | 117.4 | android_rntester (debug) | 19.2 | 18.2 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 29.4 | 28.3 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.6 | 3.3 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 1.5 | 0.5 | 0.1 | success |
|  | | |  | android_templateapp_retry_1 (release) | 3.4 | 2.4 | 0.2 | 1/1 |
|  | | |  | ios_rntester (Debug) | 71.7 | 69.9 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 72.8 | 71.3 | 0.1 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 18.3 | 11.9 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 12.9 | 9.2 | 0.1 | 1/1 |
| 2026-09-30 20:56 | [36776081983](https://github.com/react/react-native/actions/runs/36776081983) | maestro | 210.4 | android_rntester (debug) | 19.5 | 18.6 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 29.9 | 28.8 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.8 | 3.3 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.8 | 2.7 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 70.8 | 69.6 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 56.9 | 55.5 | 0.1 | 0/1 |
|  | | |  | ios_rntester_retry_1 (Debug) | 92.8 | 91.3 | 0.1 | 48/48 |
|  | | |  | ios_rntester_retry_1 (Release) | 83.3 | 82.2 | 0.1 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 15.1 | 10.3 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 12.9 | 10.5 | 0.1 | 1/1 |
| 2026-09-30 19:41 | [36767364423](https://github.com/react/react-native/actions/runs/36767364423) | maestro | 116.8 | android_rntester (debug) | 19.3 | 18.4 | 0.2 | 27/27 |
|  | | |  | android_rntester (release) | 27.7 | 26.7 | 0.2 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.7 | 3.3 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.3 | 2.3 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 72.6 | 71.4 | 0.1 | 48/48, 2 passed on retry |
|  | | |  | ios_rntester (Release) | 70.6 | 69.0 | 0.1 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 15.2 | 9.6 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 13.1 | 9.2 | 0.1 | 1/1 |
| 2026-09-30 17:12 | [36749789163](https://github.com/react/react-native/actions/runs/36749789163) | maestro | 153.9 | android_rntester (debug) | 19.7 | 18.7 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 29.6 | 28.4 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 8.3 | 6.0 | 0.1 | 0/1 |
|  | | |  | android_templateapp (release) | 3.6 | 2.5 | 0.1 | 1/1 |
|  | | |  | android_templateapp_retry_1 (debug) | 5.7 | 3.2 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 104.8 | 103.5 | 0.1 | 48/48, 2 passed on retry |
|  | | |  | ios_rntester (Release) | 85.0 | 83.6 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_templateapp (Debug) | 15.6 | 9.7 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 13.4 | 10.8 | 0.1 | 1/1 |
| 2026-09-30 14:59 | [36733364499](https://github.com/react/react-native/actions/runs/36733364499) | maestro | 327.7 | android_rntester (debug) | 19.6 | 18.7 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 28.5 | 27.5 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.7 | 3.3 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.7 | 2.6 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 105.4 | 103.8 | 0.1 | 43/44, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 67.1 | 66.1 | 0.1 | 48/48 |
|  | | |  | ios_rntester_retry_1 (Debug) | 78.0 | 76.7 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester_retry_1 (Release) | 98.8 | 97.4 | 0.1 | 43/44 |
|  | | |  | ios_rntester_retry_2 (Debug) | 76.7 | 75.0 | 0.2 | 48/48 |
|  | | |  | ios_rntester_retry_2 (Release) | 72.7 | 71.1 | 0.2 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 19.9 | 12.1 | 0.0 | 1/1 |
|  | | |  | ios_templateapp (Release) | 11.1 | 8.3 | 0.1 | 1/1 |
| 2026-09-30 02:09 | [36658520210](https://github.com/react/react-native/actions/runs/36658520210) | maestro | 233.5 | android_rntester (debug) | 19.5 | 18.4 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 30.3 | 29.3 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.6 | 3.3 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.8 | 2.7 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 98.5 | 97.1 | 0.0 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 101.3 | 99.7 | 0.0 | 43/44 |
|  | | |  | ios_rntester_retry_1 (Debug) | 89.1 | 87.7 | 0.1 | 48/48, 2 passed on retry |
|  | | |  | ios_rntester_retry_1 (Release) | 66.1 | 64.9 | 0.1 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 18.7 | 12.8 | 0.1 | 1/1, 1 passed on retry |
|  | | |  | ios_templateapp (Release) | 12.7 | 8.7 | 0.1 | 1/1 |
| 2026-09-29 18:54 | [36615400018](https://github.com/react/react-native/actions/runs/36615400018) | maestro | 130.4 | android_rntester (debug) | 21.7 | 20.6 | 0.2 | 27/27 |
|  | | |  | android_rntester (release) | 30.0 | 28.9 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.6 | 3.2 | 0.2 | 1/1 |
|  | | |  | android_templateapp (release) | 3.6 | 2.6 | 0.2 | 1/1 |
|  | | |  | ios_rntester (Debug) | 69.7 | 68.5 | 0.2 | 48/48 |
|  | | |  | ios_rntester (Release) | 80.1 | 78.7 | 0.2 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 16.6 | 11.2 | 0.1 | 1/1, 1 passed on retry |
|  | | |  | ios_templateapp (Release) | 12.5 | 9.4 | 0.1 | 1/1 |
| 2026-09-29 17:07 | [36602659426](https://github.com/react/react-native/actions/runs/36602659426) | maestro | 336.6 | android_rntester (debug) | 20.0 | 18.9 | 0.2 | 27/27 |
|  | | |  | android_rntester (release) | 31.6 | 30.6 | 0.2 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.6 | 3.2 | 0.6 | 1/1 |
|  | | |  | android_templateapp (release) | 3.5 | 2.5 | 0.5 | 1/1 |
|  | | |  | ios_rntester (Debug) | 107.3 | 106.0 | 0.1 | 43/44, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 81.3 | 79.9 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester_retry_1 (Debug) | 101.8 | 100.4 | 0.1 | 43/44, 3 passed on retry |
|  | | |  | ios_rntester_retry_1 (Release) | 74.7 | 73.5 | 0.1 | 48/48 |
|  | | |  | ios_rntester_retry_2 (Debug) | 83.7 | 82.3 | 0.1 | 48/48 |
|  | | |  | ios_rntester_retry_2 (Release) | 73.1 | 71.8 | 0.2 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 15.5 | 11.3 | 0.1 | 1/1, 1 passed on retry |
|  | | |  | ios_templateapp (Release) | 12.3 | 9.8 | 0.1 | 1/1 |
| 2026-09-29 16:53 | [36601037859](https://github.com/react/react-native/actions/runs/36601037859) | maestro | 130.8 | android_rntester (debug) | 26.7 | 25.6 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 29.7 | 28.7 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 6.3 | 3.9 | 0.1 | 0/1 |
|  | | |  | android_templateapp (release) | 3.6 | 2.6 | 0.1 | 1/1 |
|  | | |  | android_templateapp_retry_1 (debug) | 5.7 | 3.1 | 0.6 | 1/1 |
|  | | |  | ios_rntester (Debug) | 84.2 | 82.8 | 0.1 | 48/48, 2 passed on retry |
|  | | |  | ios_rntester (Release) | 79.7 | 78.5 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_templateapp (Debug) | 18.1 | 11.2 | 0.0 | 1/1 |
|  | | |  | ios_templateapp (Release) | 14.9 | 10.9 | 0.1 | 1/1 |
| 2026-09-29 16:47 | [36600300559](https://github.com/react/react-native/actions/runs/36600300559) | maestro | 128.7 | android_rntester (debug) | 20.2 | 19.1 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 29.0 | 28.1 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.9 | 3.4 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.5 | 2.5 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 82.6 | 81.3 | 0.2 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 71.6 | 70.4 | 0.2 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 14.8 | 8.9 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 13.0 | 9.6 | 0.1 | 1/1 |
| 2026-09-29 16:43 | [36599816010](https://github.com/react/react-native/actions/runs/36599816010) | maestro | 247.1 | android_rntester (debug) | 21.2 | 20.1 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 29.2 | 28.1 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.8 | 3.3 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.7 | 2.6 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 82.5 | 81.2 | 0.2 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 109.0 | 107.5 | 0.2 | 43/44, 2 passed on retry |
|  | | |  | ios_rntester_retry_1 (Debug) | 74.7 | 72.8 | 0.2 | 48/48 |
|  | | |  | ios_rntester_retry_1 (Release) | 92.8 | 90.3 | 0.2 | 48/48, 1 passed on retry |
|  | | |  | ios_templateapp (Debug) | 16.9 | 10.5 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 16.9 | 12.2 | 0.1 | 1/1 |
| 2026-09-29 15:15 | [36588841649](https://github.com/react/react-native/actions/runs/36588841649) | maestro | 135.4 | android_rntester (debug) | 20.8 | 19.8 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 30.5 | 29.5 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.8 | 3.2 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.7 | 2.7 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 85.6 | 84.5 | 0.2 | 48/48, 2 passed on retry |
|  | | |  | ios_rntester (Release) | 73.5 | 72.4 | 0.2 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 16.0 | 9.7 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 13.6 | 9.1 | 0.1 | 1/1 |
| 2026-09-29 13:58 | [36579064202](https://github.com/react/react-native/actions/runs/36579064202) | maestro | 127.9 | android_rntester (debug) | 19.4 | 18.4 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 28.9 | 28.0 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.9 | 3.5 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.6 | 2.6 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 79.7 | 78.4 | 0.1 | 48/48 |
|  | | |  | ios_rntester (Release) | 64.9 | 63.9 | 0.1 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 14.5 | 10.1 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 14.3 | 11.7 | 0.1 | 1/1 |
| 2026-09-29 13:48 | [36577830851](https://github.com/react/react-native/actions/runs/36577830851) | maestro | 232.5 | android_rntester (debug) | 19.6 | 18.6 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 28.7 | 27.7 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.6 | 3.2 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.5 | 2.4 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 110.4 | 108.9 | 0.1 | 43/44, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 88.8 | 87.5 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester_retry_1 (Debug) | 78.5 | 77.0 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester_retry_1 (Release) | 70.3 | 68.7 | 0.1 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 14.0 | 8.8 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 12.8 | 9.0 | 0.1 | 1/1 |
| 2026-09-29 13:39 | [36576766847](https://github.com/react/react-native/actions/runs/36576766847) | maestro | 233.1 | android_rntester (debug) | 3.9 | 2.9 | 0.1 | success |
|  | | |  | android_rntester (release) | 30.6 | 29.6 | 0.1 | 51/51 |
|  | | |  | android_rntester_retry_1 (debug) | 20.6 | 19.5 | 0.1 | 27/27 |
|  | | |  | android_templateapp (debug) | 5.8 | 3.3 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 4.5 | 3.5 | 0.2 | 0/1 |
|  | | |  | android_templateapp_retry_1 (release) | 3.6 | 2.6 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 56.8 | 55.6 | 0.1 | 0/1 |
|  | | |  | ios_rntester (Release) | 100.0 | 98.6 | 5.1 | 43/44 |
|  | | |  | ios_rntester_retry_1 (Debug) | 80.6 | 79.0 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester_retry_1 (Release) | 74.0 | 72.5 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_templateapp (Debug) | 14.5 | 9.1 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 12.8 | 9.5 | 0.1 | 1/1 |
| 2026-09-29 11:36 | [36562762399](https://github.com/react/react-native/actions/runs/36562762399) | maestro | 332.1 | android_rntester (debug) | 22.2 | 21.1 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 50.3 | 49.2 | 0.1 | 2/51 |
|  | | |  | android_rntester_retry_1 (release) | 27.5 | 26.6 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.8 | 3.2 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.8 | 2.8 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 104.8 | 103.1 | 0.1 | 41/42, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 69.3 | 68.1 | 0.1 | 48/48 |
|  | | |  | ios_rntester_retry_1 (Debug) | 105.2 | 102.8 | 0.1 | 43/44 |
|  | | |  | ios_rntester_retry_1 (Release) | 88.3 | 86.6 | 0.1 | 43/44 |
|  | | |  | ios_rntester_retry_2 (Debug) | 72.4 | 71.2 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester_retry_2 (Release) | 71.0 | 69.8 | 0.1 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 25.5 | 15.7 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 12.7 | 8.9 | 0.1 | 1/1 |
| 2026-09-29 10:08 | [36553670490](https://github.com/react/react-native/actions/runs/36553670490) | maestro | 133.4 | android_rntester (debug) | 19.9 | 18.9 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 30.6 | 29.5 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.7 | 3.3 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.5 | 2.5 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 87.4 | 86.0 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 68.6 | 67.4 | 0.1 | 48/48 |
| 2026-09-29 09:06 | [36547007634](https://github.com/react/react-native/actions/runs/36547007634) | maestro | 240.8 | ios_rntester (Debug) | 88.0 | 86.7 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 118.3 | 116.6 | 0.1 | 43/44, 1 passed on retry |
|  | | |  | ios_rntester_retry_1 (Debug) | 70.3 | 69.1 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester_retry_1 (Release) | 74.3 | 73.0 | 0.1 | 48/48 |
| 2026-09-28 18:43 | [36467232773](https://github.com/react/react-native/actions/runs/36467232773) | maestro | 133.4 | android_rntester (debug) | 20.5 | 19.5 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 28.1 | 27.2 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 6.1 | 3.4 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.4 | 2.4 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 81.5 | 80.2 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 89.0 | 87.5 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_templateapp (Release) | 13.0 | 10.6 | 0.1 | 1/1 |
| 2026-09-28 18:25 | [36465034563](https://github.com/react/react-native/actions/runs/36465034563) | maestro | 121.2 | android_rntester (debug) | 20.4 | 19.4 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 28.3 | 27.4 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.6 | 3.2 | 0.0 | 1/1 |
|  | | |  | android_templateapp (release) | 3.7 | 2.7 | 0.0 | 1/1 |
|  | | |  | ios_rntester (Debug) | 75.6 | 74.4 | 0.1 | 48/48, 2 passed on retry |
|  | | |  | ios_rntester (Release) | 65.8 | 64.7 | 0.1 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 15.6 | 10.8 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 10.7 | 8.7 | 0.1 | 1/1 |
| 2026-09-28 17:43 | [36460151200](https://github.com/react/react-native/actions/runs/36460151200) | maestro | 136.7 | android_rntester (debug) | 21.9 | 20.9 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 28.8 | 27.8 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 6.2 | 3.5 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.5 | 2.5 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 88.3 | 86.9 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 92.3 | 90.9 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_templateapp (Debug) | 18.1 | 11.1 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 13.0 | 9.3 | 0.1 | 1/1 |
| 2026-09-28 17:01 | [36455174116](https://github.com/react/react-native/actions/runs/36455174116) | maestro | 136.2 | android_rntester (debug) | 19.3 | 18.2 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 28.4 | 27.4 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.5 | 3.0 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.6 | 2.5 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 83.2 | 81.8 | 0.1 | 48/48 |
|  | | |  | ios_rntester (Release) | 83.9 | 82.5 | 0.1 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 16.6 | 11.4 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 11.1 | 9.2 | 0.1 | 1/1 |
| 2026-09-28 16:55 | [36454478119](https://github.com/react/react-native/actions/runs/36454478119) | maestro | 127.5 | android_rntester (debug) | 19.8 | 18.8 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 28.4 | 27.5 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.6 | 3.2 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.4 | 2.5 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 84.5 | 83.2 | 0.1 | 48/48, 3 passed on retry |
|  | | |  | ios_rntester (Release) | 84.1 | 82.7 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_templateapp (Debug) | 15.3 | 9.6 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 13.3 | 9.1 | 0.1 | 1/1 |
| 2026-09-28 13:47 | [36431079493](https://github.com/react/react-native/actions/runs/36431079493) | maestro | 333.3 | android_rntester (debug) | 21.7 | 20.6 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 29.9 | 29.0 | 0.0 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.5 | 3.1 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.6 | 2.6 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 92.5 | 91.0 | 0.1 | 41/42, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 99.4 | 97.7 | 0.1 | 43/44 |
|  | | |  | ios_rntester_retry_1 (Debug) | 106.8 | 105.2 | 0.1 | 43/44, 1 passed on retry |
|  | | |  | ios_rntester_retry_1 (Release) | 93.6 | 92.5 | 0.1 | 36/37 |
|  | | |  | ios_rntester_retry_2 (Debug) | 40.5 | 39.5 | 0.1 | 22/23 |
|  | | |  | ios_rntester_retry_2 (Release) | 83.6 | 82.2 | 0.1 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 21.8 | 14.6 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 11.6 | 9.4 | 0.1 | 1/1 |
| 2026-09-28 13:42 | [36430546119](https://github.com/react/react-native/actions/runs/36430546119) | maestro | 140.4 | android_rntester (debug) | 20.1 | 19.1 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 28.0 | 27.1 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.9 | 3.4 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 4.0 | 2.9 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 83.0 | 81.6 | 0.1 | 48/48, 2 passed on retry |
|  | | |  | ios_rntester (Release) | 95.5 | 94.1 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_templateapp (Debug) | 15.3 | 10.6 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 14.9 | 12.2 | 0.1 | 1/1 |
| 2026-09-28 12:37 | [36422996335](https://github.com/react/react-native/actions/runs/36422996335) | maestro | 125.2 | android_rntester (debug) | 21.7 | 20.6 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 29.3 | 28.4 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.6 | 3.1 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.5 | 2.5 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 79.2 | 77.8 | 0.1 | 48/48 |
|  | | |  | ios_rntester (Release) | 81.0 | 79.7 | 0.1 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 13.9 | 8.9 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 13.7 | 10.1 | 0.1 | 1/1 |
| 2026-09-28 12:29 | [36422135990](https://github.com/react/react-native/actions/runs/36422135990) | maestro | 131.5 | android_rntester (debug) | 22.2 | 21.2 | 0.1 | 27/27 |
|  | | |  | android_rntester (release) | 30.4 | 29.4 | 0.1 | 51/51 |
|  | | |  | android_templateapp (debug) | 5.5 | 3.2 | 0.1 | 1/1 |
|  | | |  | android_templateapp (release) | 3.6 | 2.5 | 0.1 | 1/1 |
|  | | |  | ios_rntester (Debug) | 74.4 | 73.2 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 81.1 | 79.8 | 0.1 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 13.9 | 8.8 | 0.1 | 1/1 |
|  | | |  | ios_templateapp (Release) | 12.1 | 8.8 | 0.1 | 1/1 |
| 2026-09-28 10:53 | [36412375996](https://github.com/react/react-native/actions/runs/36412375996) | maestro | 297.8 | android_rntester (debug) | 38.4 | 37.3 | 0.0 | 2/27 |
|  | | |  | android_rntester (release) | 52.9 | 51.8 | 0.0 | 2/51 |
|  | | |  | android_rntester_retry_1 (debug) | 39.2 | 38.1 | 0.1 | 2/27 |
|  | | |  | android_rntester_retry_1 (release) | 51.2 | 50.3 | 0.1 | 2/51 |
|  | | |  | android_rntester_retry_2 (debug) | 38.1 | 37.1 | 0.1 | 2/27 |
|  | | |  | android_rntester_retry_2 (release) | 51.0 | 50.0 | 0.1 | 2/51 |
|  | | |  | android_templateapp (debug) | 6.2 | 3.9 | 0.1 | 0/1 |
|  | | |  | android_templateapp (release) | 4.4 | 3.5 | 0.1 | 0/1 |
|  | | |  | android_templateapp_retry_1 (debug) | 6.3 | 4.0 | 0.1 | 0/1 |
|  | | |  | android_templateapp_retry_1 (release) | 4.6 | 3.5 | 0.1 | 0/1 |
|  | | |  | android_templateapp_retry_2 (debug) | 6.0 | 3.8 | 0.1 | 0/1 |
|  | | |  | android_templateapp_retry_2 (release) | 4.6 | 3.7 | 0.1 | 0/1 |
|  | | |  | ios_rntester (Debug) | 94.2 | 92.8 | 0.1 | 43/44, 1 passed on retry |
|  | | |  | ios_rntester (Release) | 74.4 | 73.1 | 0.1 | 48/48 |
|  | | |  | ios_rntester_retry_1 (Debug) | 64.4 | 63.2 | 0.1 | 48/48 |
|  | | |  | ios_rntester_retry_1 (Release) | 80.1 | 78.8 | 0.6 | 43/44 |
|  | | |  | ios_rntester_retry_2 (Debug) | 79.4 | 78.1 | 0.1 | 48/48, 2 passed on retry |
|  | | |  | ios_rntester_retry_2 (Release) | 68.4 | 67.0 | 0.1 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 15.3 | 10.2 | 0.1 | 1/1, 1 passed on retry |
|  | | |  | ios_templateapp (Release) | 12.1 | 8.4 | 0.1 | 1/1 |
| 2026-09-28 09:52 | [36406213503](https://github.com/react/react-native/actions/runs/36406213503) | maestro | 216.8 | android_rntester (debug) | 38.4 | 37.4 | 0.1 | 2/27 |
|  | | |  | android_rntester (release) | 52.0 | 51.0 | 0.1 | 2/51 |
|  | | |  | android_rntester_retry_1 (debug) | 39.1 | 38.1 | 0.0 | 2/27 |
|  | | |  | android_rntester_retry_1 (release) | 50.9 | 49.9 | 0.0 | 2/51 |
|  | | |  | android_rntester_retry_2 (debug) | 39.8 | 38.8 | 0.1 | 2/27 |
|  | | |  | android_rntester_retry_2 (release) | 51.1 | 50.0 | 0.1 | 2/51 |
|  | | |  | android_templateapp (debug) | 6.4 | 3.9 | 0.0 | 0/1 |
|  | | |  | android_templateapp (release) | 4.5 | 3.5 | 0.0 | 0/1 |
|  | | |  | android_templateapp_retry_1 (debug) | 6.2 | 3.9 | 0.0 | 0/1 |
|  | | |  | android_templateapp_retry_1 (release) | 4.5 | 3.5 | 0.0 | 0/1 |
|  | | |  | android_templateapp_retry_2 (debug) | 6.4 | 4.0 | 0.1 | 0/1 |
|  | | |  | android_templateapp_retry_2 (release) | 4.5 | 3.5 | 0.1 | 0/1 |
|  | | |  | ios_rntester (Debug) | 82.3 | 80.9 | 0.1 | 48/48 |
|  | | |  | ios_rntester (Release) | 92.3 | 90.8 | 0.1 | 43/44 |
|  | | |  | ios_rntester_retry_1 (Debug) | 82.4 | 81.1 | 0.1 | 48/48, 1 passed on retry |
|  | | |  | ios_rntester_retry_1 (Release) | 74.2 | 73.0 | 0.1 | 48/48 |
|  | | |  | ios_templateapp (Debug) | 14.9 | 9.9 | 0.1 | 1/1, 1 passed on retry |
|  | | |  | ios_templateapp (Release) | 11.3 | 8.2 | 0.1 | 1/1 |
| 2026-05-08 17:01 | [25568509122](https://github.com/react/react-native/actions/runs/25568509122) | - | 92.2 | android_rntester (debug) | 61.0 | 60.0 | 0.1 | success |
|  | | |  | android_rntester (release) | 7.1 | 6.1 | 0.1 | success |
|  | | |  | android_rntester_retry_1 (debug) | 7.7 | 6.8 | 0.1 | success |
|  | | |  | android_rntester_retry_1 (release) | 7.0 | 6.0 | 0.1 | success |
|  | | |  | android_templateapp (debug) | 8.1 | 1.8 | 0.1 | success |
|  | | |  | android_templateapp (release) | 8.1 | 1.4 | 0.1 | success |
|  | | |  | ios_rntester (Debug) | 31.7 | 30.7 | 0.1 | success |
|  | | |  | ios_rntester (Release) | 24.5 | 23.3 | 0.1 | success |
|  | | |  | ios_templateapp (Debug) | 19.4 | 8.3 | 0.1 | success |
| 2026-05-08 14:32 | [25561364468](https://github.com/react/react-native/actions/runs/25561364468) | - | 94.4 | android_rntester (debug) | 8.0 | 7.0 | 0.1 | success |
|  | | |  | android_rntester (release) | 6.8 | 6.0 | 0.1 | success |
|  | | |  | android_templateapp (debug) | 8.2 | 1.9 | 0.1 | success |
|  | | |  | android_templateapp (release) | 8.2 | 1.4 | 0.1 | success |
|  | | |  | ios_rntester (Debug) | 28.6 | 27.4 | 0.1 | success |
|  | | |  | ios_rntester (Release) | 16.2 | 15.0 | 0.1 | success |
|  | | |  | ios_templateapp (Debug) | 20.1 | 9.8 | 0.1 | success |
|  | | |  | ios_templateapp (Release) | 16.9 | 7.9 | 0.1 | success |
| 2026-05-08 13:56 | [25559597589](https://github.com/react/react-native/actions/runs/25559597589) | - | 85.0 | android_rntester (debug) | 8.2 | 7.2 | 0.6 | success |
|  | | |  | android_rntester (release) | 6.3 | 5.5 | 0.8 | success |
|  | | |  | android_templateapp (debug) | 7.6 | 1.7 | 0.1 | success |
|  | | |  | android_templateapp (release) | 7.7 | 1.2 | 0.1 | success |
|  | | |  | ios_rntester (Debug) | 26.8 | 25.0 | 0.1 | success |
|  | | |  | ios_rntester (Release) | 27.1 | 25.3 | 0.1 | success |
|  | | |  | ios_templateapp (Debug) | 18.0 | 8.2 | 0.1 | success |
|  | | |  | ios_templateapp (Release) | 17.1 | 7.3 | 0.1 | success |
| 2026-05-08 13:07 | [25557283612](https://github.com/react/react-native/actions/runs/25557283612) | - | 91.7 | android_rntester (debug) | 7.8 | 6.9 | 0.1 | success |
|  | | |  | android_rntester (release) | 6.9 | 6.0 | 0.1 | success |
|  | | |  | android_templateapp (debug) | 7.8 | 1.7 | 0.1 | success |
|  | | |  | android_templateapp (release) | 7.6 | 1.2 | 0.1 | success |
|  | | |  | ios_rntester (Debug) | 24.1 | 23.1 | 0.1 | success |
|  | | |  | ios_rntester (Release) | 25.2 | 23.9 | 0.1 | success |
|  | | |  | ios_templateapp (Debug) | 19.7 | 10.3 | 0.1 | success |
|  | | |  | ios_templateapp (Release) | 17.6 | 8.7 | 0.1 | success |
| 2026-05-08 11:42 | [25553686004](https://github.com/react/react-native/actions/runs/25553686004) | - | 87.5 | android_rntester (debug) | 7.9 | 7.0 | 0.1 | success |
|  | | |  | android_rntester (release) | 7.2 | 6.2 | 0.1 | success |
|  | | |  | android_templateapp (debug) | 7.5 | 1.6 | 0.1 | success |
|  | | |  | android_templateapp (release) | 8.2 | 1.4 | 0.1 | success |
|  | | |  | ios_rntester (Debug) | 26.6 | 25.0 | 0.1 | success |
|  | | |  | ios_rntester (Release) | 24.4 | 22.5 | 0.1 | success |
|  | | |  | ios_templateapp (Debug) | 19.1 | 9.7 | 0.1 | success |
| 2026-05-07 21:20 | [25522742359](https://github.com/react/react-native/actions/runs/25522742359) | - | 111.2 | android_rntester (debug) | 7.7 | 7.1 | 0.1 | success |
|  | | |  | android_rntester (release) | 7.0 | 6.3 | 0.1 | success |
|  | | |  | android_templateapp (debug) | 7.8 | 1.8 | 0.1 | success |
|  | | |  | android_templateapp (release) | 66.5 | 60.0 | 0.1 | success |
|  | | |  | android_templateapp_retry_1 (debug) | 8.2 | 1.8 | 0.1 | success |
|  | | |  | android_templateapp_retry_1 (release) | 8.2 | 1.3 | 0.1 | success |
|  | | |  | ios_rntester (Debug) | 16.8 | 15.6 | 0.1 | success |
|  | | |  | ios_rntester (Release) | 16.1 | 14.9 | 0.1 | success |
|  | | |  | ios_templateapp (Release) | 19.4 | 8.4 | 0.1 | success |
| 2026-05-07 18:28 | [25514519188](https://github.com/react/react-native/actions/runs/25514519188) | - | 84.9 | android_rntester (debug) | 7.6 | 6.9 | 0.1 | success |
|  | | |  | android_rntester (release) | 6.4 | 5.7 | 0.1 | success |
|  | | |  | android_templateapp (debug) | 7.7 | 1.7 | 0.1 | success |
|  | | |  | android_templateapp (release) | 7.8 | 1.3 | 0.1 | success |
|  | | |  | ios_rntester (Debug) | 27.1 | 25.8 | 0.1 | success |
|  | | |  | ios_rntester (Release) | 15.2 | 14.0 | 0.1 | success |
|  | | |  | ios_templateapp (Debug) | 20.1 | 10.3 | 0.1 | success |
|  | | |  | ios_templateapp (Release) | 20.6 | 10.7 | 0.1 | success |
| 2026-05-07 17:58 | [25513085044](https://github.com/react/react-native/actions/runs/25513085044) | - | 83.8 | android_rntester (debug) | 7.9 | 7.1 | 0.1 | success |
|  | | |  | android_rntester (release) | 6.8 | 6.1 | 0.1 | success |
|  | | |  | android_templateapp (debug) | 8.3 | 1.7 | 0.1 | success |
|  | | |  | android_templateapp (release) | 8.4 | 1.3 | 0.1 | success |
|  | | |  | ios_rntester (Debug) | 22.9 | 21.7 | 0.1 | success |
|  | | |  | ios_rntester (Release) | 15.0 | 13.8 | 0.1 | success |
|  | | |  | ios_templateapp (Debug) | 21.1 | 9.7 | 0.1 | success |
|  | | |  | ios_templateapp (Release) | 22.8 | 9.5 | 0.1 | success |
| 2026-05-07 16:50 | [25509760450](https://github.com/react/react-native/actions/runs/25509760450) | - | 83.1 | android_rntester (debug) | 7.6 | 6.9 | 0.1 | success |
|  | | |  | android_rntester (release) | 19.7 | 19.1 | 0.1 | success |
|  | | |  | android_rntester_retry_1 (debug) | 7.5 | 6.9 | 0.1 | success |
|  | | |  | android_rntester_retry_1 (release) | 6.8 | 6.1 | 0.2 | success |
|  | | |  | android_templateapp (debug) | 8.1 | 2.0 | 0.1 | success |
|  | | |  | android_templateapp (release) | 7.4 | 1.2 | 0.1 | success |
|  | | |  | ios_rntester (Debug) | 26.2 | 25.0 | 0.1 | success |
|  | | |  | ios_rntester (Release) | 26.7 | 25.4 | 0.1 | success |
|  | | |  | ios_templateapp (Debug) | 19.0 | 10.1 | 0.1 | success |
|  | | |  | ios_templateapp (Release) | 19.7 | 9.8 | 0.1 | success |
| 2026-05-07 16:46 | [25509543095](https://github.com/react/react-native/actions/runs/25509543095) | - | 26.5 | android_rntester (debug) | 7.8 | 7.1 | 0.1 | success |
|  | | |  | android_rntester (release) | 7.0 | 6.3 | 0.1 | success |
| 2026-05-07 16:21 | [25508284489](https://github.com/react/react-native/actions/runs/25508284489) | - | 89.4 | android_rntester (debug) | 61.1 | 60.0 | 0.1 | success |
|  | | |  | android_rntester (release) | 7.1 | 6.1 | 0.1 | success |
|  | | |  | android_rntester_retry_1 (debug) | 7.7 | 7.0 | 0.1 | success |
|  | | |  | android_rntester_retry_1 (release) | 6.7 | 6.0 | 1.2 | success |
|  | | |  | android_templateapp (debug) | 7.7 | 1.8 | 0.0 | success |
|  | | |  | android_templateapp (release) | 7.4 | 1.3 | 0.0 | success |
|  | | |  | ios_rntester (Debug) | 25.8 | 24.3 | 0.1 | success |
|  | | |  | ios_rntester (Release) | 23.5 | 22.1 | 0.1 | success |
|  | | |  | ios_templateapp (Debug) | 18.8 | 7.5 | 0.1 | success |
|  | | |  | ios_templateapp (Release) | 19.1 | 7.7 | 0.1 | success |
| 2026-05-07 16:14 | [25507926645](https://github.com/react/react-native/actions/runs/25507926645) | - | 92.3 | android_rntester (debug) | 8.1 | 7.1 | 0.1 | success |
|  | | |  | android_rntester (release) | 7.5 | 6.1 | 0.1 | success |
|  | | |  | android_templateapp (debug) | 7.5 | 1.7 | 0.1 | success |
|  | | |  | android_templateapp (release) | 7.8 | 1.4 | 0.1 | success |
|  | | |  | ios_rntester (Debug) | 24.6 | 23.4 | 0.1 | success |
|  | | |  | ios_rntester (Release) | 23.6 | 22.4 | 0.1 | success |
|  | | |  | ios_templateapp (Debug) | 22.4 | 10.9 | 0.1 | success |
|  | | |  | ios_templateapp (Release) | 22.1 | 9.2 | 0.1 | success |
| 2026-05-07 14:26 | [25501997603](https://github.com/react/react-native/actions/runs/25501997603) | - | 78.2 | android_rntester (debug) | 7.7 | 7.0 | 1.7 | success |
|  | | |  | android_rntester (release) | 6.2 | 5.5 | 1.7 | success |
|  | | |  | android_templateapp (debug) | 7.2 | 1.5 | 0.1 | success |
|  | | |  | android_templateapp (release) | 7.4 | 1.3 | 0.1 | success |
|  | | |  | ios_rntester (Debug) | 26.0 | 24.2 | 0.1 | success |
|  | | |  | ios_rntester (Release) | 25.4 | 23.9 | 0.1 | success |
|  | | |  | ios_templateapp (Debug) | 19.4 | 8.3 | 0.1 | success |
|  | | |  | ios_templateapp (Release) | 7.7 | 0.1 | 0.1 | success |
|  | | |  | ios_templateapp_retry_1 (Debug) | 24.8 | 12.3 | 0.1 | success |
|  | | |  | ios_templateapp_retry_1 (Release) | 19.8 | 9.4 | 0.1 | success |
| 2026-05-07 14:14 | [25501333011](https://github.com/react/react-native/actions/runs/25501333011) | - | 84.0 | android_rntester (debug) | 7.8 | 7.0 | 0.4 | success |
|  | | |  | android_rntester (release) | 7.1 | 6.3 | 0.2 | success |
|  | | |  | android_templateapp (debug) | 7.9 | 1.9 | 1.9 | success |
|  | | |  | android_templateapp (release) | 7.4 | 1.2 | 1.4 | success |
|  | | |  | ios_rntester (Debug) | 26.2 | 24.4 | 0.1 | success |
|  | | |  | ios_rntester (Release) | 24.0 | 22.4 | 0.1 | success |
|  | | |  | ios_templateapp (Debug) | 18.8 | 8.5 | 0.1 | success |
|  | | |  | ios_templateapp (Release) | 16.2 | 7.0 | 0.1 | success |
| 2026-05-07 13:27 | [25498729432](https://github.com/react/react-native/actions/runs/25498729432) | - | 78.8 | ios_rntester (Debug) | 24.3 | 23.1 | 0.1 | success |
|  | | |  | ios_rntester (Release) | 24.4 | 23.3 | 0.1 | success |
| 2026-05-07 08:57 | [25486173782](https://github.com/react/react-native/actions/runs/25486173782) | - | 82.8 | ios_rntester (Debug) | 16.6 | 15.5 | 0.1 | success |
|  | | |  | ios_rntester (Release) | 25.9 | 24.6 | 0.1 | success |
| 2026-05-07 02:25 | [25472541355](https://github.com/react/react-native/actions/runs/25472541355) | - | 78.6 | android_rntester (debug) | 7.6 | 7.0 | 0.0 | success |
|  | | |  | android_rntester (release) | 6.8 | 6.1 | 0.1 | success |
|  | | |  | android_templateapp (debug) | 7.8 | 1.8 | 0.1 | success |
|  | | |  | android_templateapp (release) | 7.5 | 1.3 | 0.1 | success |
|  | | |  | ios_rntester (Debug) | 26.0 | 24.2 | 0.1 | success |
|  | | |  | ios_rntester (Release) | 17.1 | 15.4 | 0.1 | success |
|  | | |  | ios_templateapp (Debug) | 18.1 | 8.4 | 0.1 | success |
|  | | |  | ios_templateapp (Release) | 16.4 | 6.9 | 0.1 | success |
| 2026-05-07 01:58 | [25471695673](https://github.com/react/react-native/actions/runs/25471695673) | - | 79.8 | ios_rntester (Release) | 23.0 | 21.8 | 0.1 | success |
| 2026-05-07 00:11 | [25468337147](https://github.com/react/react-native/actions/runs/25468337147) | - | 86.1 | android_rntester (debug) | 7.8 | 7.1 | 0.1 | success |
|  | | |  | android_rntester (release) | 6.9 | 6.2 | 0.1 | success |
|  | | |  | android_templateapp (debug) | 7.5 | 1.7 | 0.1 | success |
|  | | |  | android_templateapp (release) | 8.2 | 1.6 | 0.1 | success |
|  | | |  | ios_rntester (Debug) | 24.2 | 22.9 | 0.1 | success |
|  | | |  | ios_rntester (Release) | 24.3 | 23.1 | 0.1 | success |
|  | | |  | ios_templateapp (Debug) | 23.1 | 11.2 | 0.1 | success |
|  | | |  | ios_templateapp (Release) | 17.4 | 7.2 | 0.1 | success |
| 2026-05-06 17:30 | [25450838864](https://github.com/react/react-native/actions/runs/25450838864) | - | 83.7 | android_rntester (debug) | 6.7 | 6.1 | 0.5 | success |
|  | | |  | android_rntester (release) | 18.7 | 18.1 | 0.5 | success |
|  | | |  | android_rntester_retry_1 (debug) | 7.8 | 7.1 | 0.7 | success |
|  | | |  | android_rntester_retry_1 (release) | 6.0 | 5.4 | 0.4 | success |
|  | | |  | android_templateapp (debug) | 7.3 | 1.6 | 0.1 | success |
|  | | |  | android_templateapp (release) | 7.3 | 1.2 | 0.1 | success |
|  | | |  | ios_rntester (Debug) | 25.9 | 24.8 | 0.1 | success |
|  | | |  | ios_rntester (Release) | 25.8 | 24.6 | 0.1 | success |
|  | | |  | ios_templateapp (Debug) | 18.7 | 9.6 | 0.1 | success |
|  | | |  | ios_templateapp (Release) | 18.2 | 9.0 | 0.1 | success |
| 2026-05-06 15:43 | [25445565271](https://github.com/react/react-native/actions/runs/25445565271) | - | 108.6 | android_rntester (debug) | 7.8 | 7.0 | 0.1 | success |
|  | | |  | android_rntester (release) | 6.9 | 6.1 | 0.1 | success |
|  | | |  | android_templateapp (debug) | 7.8 | 1.8 | 0.1 | success |
|  | | |  | android_templateapp (release) | 7.7 | 1.4 | 0.1 | success |
|  | | |  | ios_rntester (Debug) | 49.6 | 48.0 | 0.3 | success |
|  | | |  | ios_rntester (Release) | 16.2 | 14.6 | 1.4 | success |
|  | | |  | ios_templateapp (Debug) | 18.6 | 7.2 | 0.1 | success |
|  | | |  | ios_templateapp (Release) | 16.9 | 7.2 | 0.1 | success |
| 2026-05-06 13:44 | [25439112168](https://github.com/react/react-native/actions/runs/25439112168) | - | 88.8 | android_rntester (debug) | 6.8 | 6.1 | 0.1 | success |
|  | | |  | android_rntester (release) | 6.0 | 5.3 | 0.1 | success |
|  | | |  | android_templateapp (debug) | 7.0 | 1.6 | 0.1 | success |
|  | | |  | android_templateapp (release) | 7.0 | 1.1 | 0.1 | success |
|  | | |  | ios_rntester (Debug) | 25.3 | 24.1 | 0.1 | success |
|  | | |  | ios_rntester (Release) | 17.8 | 16.6 | 0.1 | success |
|  | | |  | ios_templateapp (Debug) | 18.2 | 8.9 | 0.1 | success |
|  | | |  | ios_templateapp (Release) | 15.4 | 7.4 | 0.1 | success |
| 2026-05-06 13:36 | [25438691383](https://github.com/react/react-native/actions/runs/25438691383) | - | 78.8 | android_rntester (debug) | 7.8 | 7.0 | 0.1 | success |
|  | | |  | android_rntester (release) | 6.0 | 5.4 | 0.1 | success |
|  | | |  | android_templateapp (debug) | 7.3 | 1.6 | 0.1 | success |
|  | | |  | android_templateapp (release) | 7.0 | 1.1 | 0.1 | success |
|  | | |  | ios_rntester (Debug) | 25.5 | 24.4 | 0.1 | success |
|  | | |  | ios_rntester (Release) | 24.0 | 22.8 | 0.1 | success |
|  | | |  | ios_templateapp (Debug) | 20.4 | 11.3 | 0.1 | success |
|  | | |  | ios_templateapp (Release) | 24.4 | 12.5 | 0.1 | success |
| 2026-05-06 12:37 | [25435658661](https://github.com/react/react-native/actions/runs/25435658661) | - | 82.2 | android_rntester (debug) | 7.8 | 7.0 | 0.8 | success |
|  | | |  | android_rntester (release) | 6.8 | 6.1 | 0.8 | success |
|  | | |  | android_templateapp (debug) | 7.8 | 1.8 | 0.1 | success |
|  | | |  | android_templateapp (release) | 8.1 | 1.4 | 0.1 | success |
|  | | |  | ios_rntester (Debug) | 24.5 | 23.4 | 0.1 | success |
|  | | |  | ios_rntester (Release) | 23.6 | 22.5 | 0.1 | success |
|  | | |  | ios_templateapp (Debug) | 26.5 | 14.3 | 0.1 | success |
|  | | |  | ios_templateapp (Release) | 20.8 | 10.6 | 0.1 | success |
| 2026-05-06 12:24 | [25435038838](https://github.com/react/react-native/actions/runs/25435038838) | - | 87.8 | android_rntester (debug) | 8.0 | 7.2 | 0.1 | success |
|  | | |  | android_rntester (release) | 60.7 | 60.0 | 0.1 | success |
|  | | |  | android_rntester_retry_1 (debug) | 7.7 | 7.0 | 0.1 | success |
|  | | |  | android_rntester_retry_1 (release) | 6.3 | 5.7 | 0.1 | success |
|  | | |  | android_templateapp (debug) | 9.5 | 1.7 | 0.1 | success |
|  | | |  | android_templateapp (release) | 7.8 | 1.4 | 0.1 | success |
|  | | |  | ios_rntester (Debug) | 23.9 | 22.8 | 0.1 | success |
|  | | |  | ios_rntester (Release) | 24.6 | 23.6 | 0.1 | success |
|  | | |  | ios_templateapp (Debug) | 19.7 | 8.9 | 0.1 | success |
|  | | |  | ios_templateapp (Release) | 18.7 | 8.2 | 0.1 | success |
| 2026-05-06 00:48 | [25410472346](https://github.com/react/react-native/actions/runs/25410472346) | - | 77.0 | android_rntester (debug) | 7.5 | 6.8 | 0.1 | success |
|  | | |  | android_rntester (release) | 6.8 | 6.1 | 0.1 | success |
|  | | |  | android_templateapp (debug) | 7.6 | 1.7 | 0.1 | success |
|  | | |  | android_templateapp (release) | 7.6 | 1.2 | 0.1 | success |
|  | | |  | ios_rntester (Debug) | 25.3 | 24.1 | 0.1 | success |
|  | | |  | ios_rntester (Release) | 25.0 | 23.9 | 0.1 | success |
|  | | |  | ios_templateapp (Debug) | 19.8 | 8.8 | 0.1 | success |
|  | | |  | ios_templateapp (Release) | 22.0 | 10.0 | 0.1 | success |
| 2026-05-05 22:03 | [25404782601](https://github.com/react/react-native/actions/runs/25404782601) | - | 87.6 | android_rntester (debug) | 8.1 | 7.1 | 0.1 | success |
|  | | |  | android_rntester (release) | 61.0 | 60.0 | 0.1 | success |
|  | | |  | android_rntester_retry_1 (debug) | 7.7 | 7.0 | 0.1 | success |
|  | | |  | android_rntester_retry_1 (release) | 6.8 | 6.1 | 0.1 | success |
|  | | |  | android_templateapp (debug) | 7.7 | 1.7 | 0.1 | success |
|  | | |  | android_templateapp (release) | 7.8 | 1.4 | 0.1 | success |
|  | | |  | ios_rntester (Debug) | 26.2 | 25.0 | 0.1 | success |
|  | | |  | ios_rntester (Release) | 25.4 | 24.3 | 0.1 | success |
|  | | |  | ios_templateapp (Debug) | 17.1 | 7.7 | 0.1 | success |
|  | | |  | ios_templateapp (Release) | 17.0 | 7.3 | 0.1 | success |
| 2026-05-05 17:26 | [25391720870](https://github.com/react/react-native/actions/runs/25391720870) | - | 88.3 | android_rntester (debug) | 6.9 | 6.3 | 0.1 | success |
|  | | |  | android_rntester (release) | 6.9 | 6.2 | 0.1 | success |
|  | | |  | android_templateapp (debug) | 7.8 | 1.8 | 3.9 | success |
|  | | |  | android_templateapp (release) | 7.4 | 1.2 | 4.2 | success |
|  | | |  | ios_rntester (Debug) | 26.6 | 25.4 | 0.1 | success |
|  | | |  | ios_rntester (Release) | 25.7 | 24.5 | 0.1 | success |
|  | | |  | ios_templateapp (Debug) | 18.4 | 8.2 | 0.1 | success |
|  | | |  | ios_templateapp (Release) | 18.1 | 7.9 | 0.1 | success |
| 2026-05-05 14:09 | [25381497730](https://github.com/react/react-native/actions/runs/25381497730) | - | 81.6 | android_rntester (debug) | 7.8 | 7.1 | 0.1 | success |
|  | | |  | android_rntester (release) | 6.9 | 6.2 | 0.1 | success |
|  | | |  | android_templateapp (debug) | 7.6 | 1.6 | 0.1 | success |
|  | | |  | android_templateapp (release) | 7.8 | 1.3 | 0.1 | success |
|  | | |  | ios_rntester (Debug) | 25.8 | 24.6 | 0.2 | success |
|  | | |  | ios_rntester (Release) | 23.7 | 22.5 | 0.1 | success |
|  | | |  | ios_templateapp (Debug) | 20.4 | 9.2 | 0.1 | success |
|  | | |  | ios_templateapp (Release) | 16.3 | 7.1 | 0.1 | success |
| 2026-05-04 23:31 | [25349264440](https://github.com/react/react-native/actions/runs/25349264440) | - | 79.8 | android_rntester (debug) | 7.9 | 7.0 | 0.1 | success |
|  | | |  | android_rntester (release) | 7.0 | 6.0 | 0.1 | success |
|  | | |  | android_templateapp (debug) | 7.8 | 1.7 | 0.1 | success |
|  | | |  | android_templateapp (release) | 8.1 | 1.4 | 0.1 | success |
|  | | |  | ios_rntester (Debug) | 27.7 | 26.5 | 0.1 | success |
|  | | |  | ios_rntester (Release) | 25.5 | 24.4 | 0.1 | success |
|  | | |  | ios_templateapp (Debug) | 19.1 | 9.5 | 0.1 | success |
|  | | |  | ios_templateapp (Release) | 23.6 | 11.8 | 0.1 | success |

## Retried test cases

Per run, from each job's log: a flow *failed at least once* if any of its attempts failed, inside its job (maestro-runner `--retries`, React Native's iOS per-flow attempts, agent-device, Expo's rounds) or in a retry job (React Native's retry_1/retry_2); it *passed on retry* if it then passed. *Extra flow runs* counts every run of a flow beyond its first, including whole-suite reruns of flows that had passed. Runs whose logs had expired are left out.

| Platform | Side | Build | Runs | Runs where every flow passed first time | Flows that failed at least once / run (avg, max) | Flows passed only on retry / run | Runs ending with a failed flow | Extra flow runs / run | Runs needing a retry job | Flows / run | Most often failing flows |
|---|---|---|---|---|---|---|---|---|---|---|---|
| android debug rntester | ours | - | 1 | 1/1 | 0.00, 0 | 0.00 | 0/1 | 0.00 | 0/1 | 27 | - |
| android debug rntester | ours | 6904d0f | 2 | 2/2 | 0.00, 0 | 0.00 | 0/2 | 0.00 | 0/2 | 27 | - |
| android debug rntester | ours | 86ed2d7 | 1 | 1/1 | 0.00, 0 | 0.00 | 0/1 | 0.00 | 0/1 | 27 | - |
| android debug rntester | ours | d51beed | 1 | 0/1 | 1.00, 1 | 0.00 | 1/1 | 2.00 | 1/1 | 27 | flatlist-viewability ×1 |
| android debug rntester | upstream | - | 59 | 55/59 | 1.69, 25 | 0.85 | 2/59 | 2.54 | 5/59 | 27 | alert ×4, animated-fade-in-view ×4, appearance ×4 |
| android debug templateapp | ours | - | 1 | 1/1 | 0.00, 0 | 0.00 | 0/1 | 0.00 | 0/1 | 1 | - |
| android debug templateapp | ours | 6904d0f | 2 | 2/2 | 0.00, 0 | 0.00 | 0/2 | 0.00 | 0/2 | 1 | - |
| android debug templateapp | ours | 86ed2d7 | 1 | 1/1 | 0.00, 0 | 0.00 | 0/1 | 0.00 | 0/1 | 1 | - |
| android debug templateapp | ours | d51beed | 1 | 1/1 | 0.00, 0 | 0.00 | 0/1 | 0.00 | 0/1 | 1 | - |
| android debug templateapp | upstream | - | 59 | 53/59 | 0.10, 1 | 0.07 | 2/59 | 0.14 | 6/59 | 1 | start ×6 |
| android release rntester | ours | - | 1 | 1/1 | 0.00, 0 | 0.00 | 0/1 | 0.00 | 0/1 | 51 | - |
| android release rntester | ours | 6904d0f | 2 | 2/2 | 0.00, 0 | 0.00 | 0/2 | 0.00 | 0/2 | 51 | - |
| android release rntester | ours | 86ed2d7 | 1 | 1/1 | 0.00, 0 | 0.00 | 0/1 | 0.00 | 0/1 | 51 | - |
| android release rntester | ours | d51beed | 1 | 0/1 | 22.00, 22 | 4.00 | 1/1 | 42.00 | 1/1 | 51 | flatlist-complex-mutations-maintainvisible ×1, flatlist-delete-middle-maintainvisible ×1, flatlist-empty-list-maintainvisible ×1 |
| android release rntester | upstream | - | 59 | 55/59 | 3.32, 49 | 1.66 | 2/59 | 4.98 | 4/59 | 51 | alert ×4, animated-fade-in-view ×4, appearance ×4 |
| android release templateapp | ours | - | 1 | 0/1 | 1.00, 1 | 1.00 | 0/1 | 5.00 | 1/1 | 1 | start ×1 |
| android release templateapp | ours | 6904d0f | 2 | 2/2 | 0.00, 0 | 0.00 | 0/2 | 0.00 | 0/2 | 1 | - |
| android release templateapp | ours | 86ed2d7 | 1 | 1/1 | 0.00, 0 | 0.00 | 0/1 | 0.00 | 0/1 | 1 | - |
| android release templateapp | ours | d51beed | 1 | 1/1 | 0.00, 0 | 0.00 | 0/1 | 0.00 | 0/1 | 1 | - |
| android release templateapp | upstream | - | 59 | 54/59 | 0.08, 1 | 0.05 | 2/59 | 0.14 | 6/59 | 1 | start ×5 |
| ios debug rntester | ours | - | 1 | 0/1 | 1.00, 1 | 1.00 | 0/1 | 1.00 | 0/1 | 48 | button ×1 |
| ios debug rntester | ours | 6904d0f | 2 | 2/2 | 0.00, 0 | 0.00 | 0/2 | 0.00 | 0/2 | 48 | - |
| ios debug rntester | ours | 86ed2d7 | 1 | 0/1 | 33.00, 33 | 0.00 | 1/1 | 51.00 | 0/1 | 39 | appearance ×1, button ×1, fabric-interop-add-children ×1 |
| ios debug rntester | ours | d51beed | 1 | 0/1 | 1.00, 1 | 0.00 | 1/1 | 0.00 | 0/1 | 2 | animated-fade-in-view ×1 |
| ios debug rntester | upstream | - | 59 | 9/59 | 1.47, 5 | 1.42 | 2/59 | 23.27 | 20/59 | 48 | sectionlist-viewability ×29, scrollview-minindex-maintainvisible ×6, flatlist-viewability ×4 |
| ios debug templateapp | ours | 6904d0f | 2 | 2/2 | 0.00, 0 | 0.00 | 0/2 | 0.00 | 0/2 | 1 | - |
| ios debug templateapp | ours | 86ed2d7 | 1 | 1/1 | 0.00, 0 | 0.00 | 0/1 | 0.00 | 0/1 | 1 | - |
| ios debug templateapp | ours | d51beed | 1 | 1/1 | 0.00, 0 | 0.00 | 0/1 | 0.00 | 1/1 | 1 | - |
| ios debug templateapp | upstream | - | 56 | 49/56 | 0.12, 1 | 0.12 | 0/56 | 0.12 | 0/56 | 1 | start ×7 |
| ios release rntester | ours | - | 1 | 0/1 | 1.00, 1 | 1.00 | 0/1 | 1.00 | 0/1 | 48 | animated-fade-in-view ×1 |
| ios release rntester | ours | 6904d0f | 2 | 2/2 | 0.00, 0 | 0.00 | 0/2 | 0.00 | 0/2 | 48 | - |
| ios release rntester | ours | 86ed2d7 | 1 | 0/1 | 32.00, 32 | 0.00 | 1/1 | 21.00 | 0/1 | 37 | animated-fade-in-view ×1, appearance ×1, button ×1 |
| ios release rntester | ours | d51beed | 1 | 0/1 | 1.00, 1 | 0.00 | 1/1 | 0.00 | 0/1 | 2 | animated-fade-in-view ×1 |
| ios release rntester | upstream | - | 59 | 28/59 | 0.63, 3 | 0.63 | 0/59 | 24.00 | 21/59 | 48 | sectionlist-viewability ×30, scrollview-minindex-maintainvisible ×2, modal ×1 |
| ios release templateapp | ours | 6904d0f | 2 | 2/2 | 0.00, 0 | 0.00 | 0/2 | 0.00 | 0/2 | 1 | - |
| ios release templateapp | ours | 86ed2d7 | 1 | 1/1 | 0.00, 0 | 0.00 | 0/1 | 0.00 | 0/1 | 1 | - |
| ios release templateapp | ours | d51beed | 1 | 1/1 | 0.00, 0 | 0.00 | 0/1 | 1.00 | 1/1 | 1 | - |
| ios release templateapp | upstream | - | 56 | 56/56 | 0.00, 0 | 0.00 | 0/56 | 0.00 | 0/56 | 1 | - |

### Per run

| Started (UTC) | Run | Platform | Side | Build | Flows | Failed at least once | Passed on retry (failed attempts) | Failed at the end | Extra flow runs | Retry jobs |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-03 03:23 | [37093048002](https://github.com/maestro-runner-bench/react-native/actions/runs/37093048002) | android release rntester | ours | 6904d0f | 51 | 0 | - | - | 0 | 0 |
| 2026-10-03 03:23 | [37093048002](https://github.com/maestro-runner-bench/react-native/actions/runs/37093048002) | android debug rntester | ours | 6904d0f | 27 | 0 | - | - | 0 | 0 |
| 2026-10-03 03:23 | [37093048002](https://github.com/maestro-runner-bench/react-native/actions/runs/37093048002) | android release templateapp | ours | 6904d0f | 1 | 0 | - | - | 0 | 0 |
| 2026-10-03 03:23 | [37093048002](https://github.com/maestro-runner-bench/react-native/actions/runs/37093048002) | android debug templateapp | ours | 6904d0f | 1 | 0 | - | - | 0 | 0 |
| 2026-10-03 03:23 | [37093048002](https://github.com/maestro-runner-bench/react-native/actions/runs/37093048002) | ios release rntester | ours | 6904d0f | 48 | 0 | - | - | 0 | 0 |
| 2026-10-03 03:23 | [37093048002](https://github.com/maestro-runner-bench/react-native/actions/runs/37093048002) | ios debug rntester | ours | 6904d0f | 48 | 0 | - | - | 0 | 0 |
| 2026-10-03 03:23 | [37093048002](https://github.com/maestro-runner-bench/react-native/actions/runs/37093048002) | ios debug templateapp | ours | 6904d0f | 1 | 0 | - | - | 0 | 0 |
| 2026-10-03 03:23 | [37093048002](https://github.com/maestro-runner-bench/react-native/actions/runs/37093048002) | ios release templateapp | ours | 6904d0f | 1 | 0 | - | - | 0 | 0 |
| 2026-10-03 00:39 | [37082951955](https://github.com/react/react-native/actions/runs/37082951955) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-03 00:39 | [37082951955](https://github.com/react/react-native/actions/runs/37082951955) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-03 00:39 | [37082951955](https://github.com/react/react-native/actions/runs/37082951955) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-03 00:39 | [37082951955](https://github.com/react/react-native/actions/runs/37082951955) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-03 00:39 | [37082951955](https://github.com/react/react-native/actions/runs/37082951955) | ios debug rntester | upstream | - | 48 | 2 | flatlist-horizontal-add50-reset-maintainvisible (1), sectionlist-viewability (1) | - | 2 | 0 |
| 2026-10-03 00:39 | [37082951955](https://github.com/react/react-native/actions/runs/37082951955) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-10-03 00:39 | [37082951955](https://github.com/react/react-native/actions/runs/37082951955) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-03 00:39 | [37082951955](https://github.com/react/react-native/actions/runs/37082951955) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 21:58 | [37069938487](https://github.com/maestro-runner-bench/react-native/actions/runs/37069938487) | android release rntester | ours | 6904d0f | 51 | 0 | - | - | 0 | 0 |
| 2026-10-02 21:58 | [37069938487](https://github.com/maestro-runner-bench/react-native/actions/runs/37069938487) | android debug rntester | ours | 6904d0f | 27 | 0 | - | - | 0 | 0 |
| 2026-10-02 21:58 | [37069938487](https://github.com/maestro-runner-bench/react-native/actions/runs/37069938487) | android debug templateapp | ours | 6904d0f | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 21:58 | [37069938487](https://github.com/maestro-runner-bench/react-native/actions/runs/37069938487) | android release templateapp | ours | 6904d0f | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 21:58 | [37069938487](https://github.com/maestro-runner-bench/react-native/actions/runs/37069938487) | ios release templateapp | ours | 6904d0f | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 21:58 | [37069938487](https://github.com/maestro-runner-bench/react-native/actions/runs/37069938487) | ios debug templateapp | ours | 6904d0f | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 21:58 | [37069938487](https://github.com/maestro-runner-bench/react-native/actions/runs/37069938487) | ios release rntester | ours | 6904d0f | 48 | 0 | - | - | 0 | 0 |
| 2026-10-02 21:58 | [37069938487](https://github.com/maestro-runner-bench/react-native/actions/runs/37069938487) | ios debug rntester | ours | 6904d0f | 48 | 0 | - | - | 0 | 0 |
| 2026-10-02 19:41 | [37055799075](https://github.com/react/react-native/actions/runs/37055799075) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-02 19:41 | [37055799075](https://github.com/react/react-native/actions/runs/37055799075) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-02 19:41 | [37055799075](https://github.com/react/react-native/actions/runs/37055799075) | ios debug rntester | upstream | - | 48 | 1 | sectionlist-viewability (1) | - | 1 | 0 |
| 2026-10-02 19:41 | [37055799075](https://github.com/react/react-native/actions/runs/37055799075) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-10-02 19:41 | [37055799075](https://github.com/react/react-native/actions/runs/37055799075) | android debug templateapp | upstream | - | 1 | 1 | start (1) | - | 1 | 1 |
| 2026-10-02 19:41 | [37055799075](https://github.com/react/react-native/actions/runs/37055799075) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 19:41 | [37055799075](https://github.com/react/react-native/actions/runs/37055799075) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 19:41 | [37055799075](https://github.com/react/react-native/actions/runs/37055799075) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 18:13 | [37045943779](https://github.com/react/react-native/actions/runs/37045943779) | android debug rntester | upstream | - | 27 | 25 | alert (1), animated-fade-in-view (1), appearance (1), button (1), filter-animated-blur (1), flatlist-viewability (1), flatlist (1), launch-app-and-search (1), search (1), image-blur-prefetch (1), image-getsize-local-drawables (1), image-progressive-jpeg (1), image-wide-gamut (1), image (1), legacy-native-module (1), modal (1), new-arch-examples (1), pressable (1), scrollview-minindex-maintainvisible (1), scrollview-threshold-maintainvisible (1), sectionlist-viewability (1), text-width-mode (1), text (1), textinput-uncontrolled (1), touchable (1) | - | 25 | 1 |
| 2026-10-02 18:13 | [37045943779](https://github.com/react/react-native/actions/runs/37045943779) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-02 18:13 | [37045943779](https://github.com/react/react-native/actions/runs/37045943779) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 18:13 | [37045943779](https://github.com/react/react-native/actions/runs/37045943779) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 18:13 | [37045943779](https://github.com/react/react-native/actions/runs/37045943779) | ios debug rntester | upstream | - | 48 | 1 | flatlist-viewability (1) | - | 1 | 0 |
| 2026-10-02 18:13 | [37045943779](https://github.com/react/react-native/actions/runs/37045943779) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-10-02 18:13 | [37045943779](https://github.com/react/react-native/actions/runs/37045943779) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 18:13 | [37045943779](https://github.com/react/react-native/actions/runs/37045943779) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 16:57 | [37037432937](https://github.com/react/react-native/actions/runs/37037432937) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-02 16:57 | [37037432937](https://github.com/react/react-native/actions/runs/37037432937) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-02 16:57 | [37037432937](https://github.com/react/react-native/actions/runs/37037432937) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 16:57 | [37037432937](https://github.com/react/react-native/actions/runs/37037432937) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 16:57 | [37037432937](https://github.com/react/react-native/actions/runs/37037432937) | ios debug rntester | upstream | - | 48 | 1 | flatlist-horizontal-inverted-recycle-maintainvisible (1) | - | 1 | 0 |
| 2026-10-02 16:57 | [37037432937](https://github.com/react/react-native/actions/runs/37037432937) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-10-02 16:57 | [37037432937](https://github.com/react/react-native/actions/runs/37037432937) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 16:57 | [37037432937](https://github.com/react/react-native/actions/runs/37037432937) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 16:50 | [37036694926](https://github.com/react/react-native/actions/runs/37036694926) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-02 16:50 | [37036694926](https://github.com/react/react-native/actions/runs/37036694926) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-02 16:50 | [37036694926](https://github.com/react/react-native/actions/runs/37036694926) | ios debug rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-10-02 16:50 | [37036694926](https://github.com/react/react-native/actions/runs/37036694926) | ios release rntester | upstream | - | 48 | 1 | sectionlist-viewability (1) | - | 1 | 0 |
| 2026-10-02 16:50 | [37036694926](https://github.com/react/react-native/actions/runs/37036694926) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 16:50 | [37036694926](https://github.com/react/react-native/actions/runs/37036694926) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 16:50 | [37036694926](https://github.com/react/react-native/actions/runs/37036694926) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 16:50 | [37036694926](https://github.com/react/react-native/actions/runs/37036694926) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 16:46 | [37036180664](https://github.com/react/react-native/actions/runs/37036180664) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-02 16:46 | [37036180664](https://github.com/react/react-native/actions/runs/37036180664) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-02 16:46 | [37036180664](https://github.com/react/react-native/actions/runs/37036180664) | ios debug rntester | upstream | - | 48 | 2 | flatlist-empty-list-maintainvisible (1), sectionlist-viewability (3) | - | 4 | 0 |
| 2026-10-02 16:46 | [37036180664](https://github.com/react/react-native/actions/runs/37036180664) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-10-02 16:46 | [37036180664](https://github.com/react/react-native/actions/runs/37036180664) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 16:46 | [37036180664](https://github.com/react/react-native/actions/runs/37036180664) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 16:46 | [37036180664](https://github.com/react/react-native/actions/runs/37036180664) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 16:46 | [37036180664](https://github.com/react/react-native/actions/runs/37036180664) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 15:44 | [37029138076](https://github.com/react/react-native/actions/runs/37029138076) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-02 15:44 | [37029138076](https://github.com/react/react-native/actions/runs/37029138076) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-02 15:44 | [37029138076](https://github.com/react/react-native/actions/runs/37029138076) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 15:44 | [37029138076](https://github.com/react/react-native/actions/runs/37029138076) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 15:44 | [37029138076](https://github.com/react/react-native/actions/runs/37029138076) | ios debug rntester | upstream | - | 48 | 1 | sectionlist-viewability (1) | - | 1 | 0 |
| 2026-10-02 15:44 | [37029138076](https://github.com/react/react-native/actions/runs/37029138076) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-10-02 15:44 | [37029138076](https://github.com/react/react-native/actions/runs/37029138076) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 15:41 | [37028747659](https://github.com/react/react-native/actions/runs/37028747659) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-02 15:41 | [37028747659](https://github.com/react/react-native/actions/runs/37028747659) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-02 15:41 | [37028747659](https://github.com/react/react-native/actions/runs/37028747659) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 15:41 | [37028747659](https://github.com/react/react-native/actions/runs/37028747659) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 15:41 | [37028747659](https://github.com/react/react-native/actions/runs/37028747659) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-10-02 15:41 | [37028747659](https://github.com/react/react-native/actions/runs/37028747659) | ios debug rntester | upstream | - | 48 | 1 | pressable (1) | - | 1 | 0 |
| 2026-10-02 15:41 | [37028747659](https://github.com/react/react-native/actions/runs/37028747659) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 15:41 | [37028747659](https://github.com/react/react-native/actions/runs/37028747659) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 15:33 | [37027808769](https://github.com/react/react-native/actions/runs/37027808769) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-02 15:33 | [37027808769](https://github.com/react/react-native/actions/runs/37027808769) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-02 15:33 | [37027808769](https://github.com/react/react-native/actions/runs/37027808769) | ios release rntester | upstream | - | 48 | 1 | sectionlist-viewability (1) | - | 49 | 1 |
| 2026-10-02 15:33 | [37027808769](https://github.com/react/react-native/actions/runs/37027808769) | ios debug rntester | upstream | - | 48 | 2 | alert (1), sectionlist-viewability (6) | - | 50 | 1 |
| 2026-10-02 15:33 | [37027808769](https://github.com/react/react-native/actions/runs/37027808769) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 15:33 | [37027808769](https://github.com/react/react-native/actions/runs/37027808769) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 15:33 | [37027808769](https://github.com/react/react-native/actions/runs/37027808769) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 15:33 | [37027808769](https://github.com/react/react-native/actions/runs/37027808769) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 14:31 | [37020483607](https://github.com/react/react-native/actions/runs/37020483607) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-02 14:31 | [37020483607](https://github.com/react/react-native/actions/runs/37020483607) | android release rntester | upstream | - | 51 | 49 | alert (1), animated-fade-in-view (1), appearance (1), button (1), filter-animated-blur (1), flatlist-append-maintainvisible (1), flatlist-complex-mutations-maintainvisible (1), flatlist-delete-anchor-maintainvisible (1), flatlist-delete-middle-maintainvisible (1), flatlist-empty-list-maintainvisible (1), flatlist-first-prepend-maintainvisible (1), flatlist-horizontal-add50-reset-maintainvisible (1), flatlist-horizontal-inverted-maintainvisible (1), flatlist-horizontal-inverted-recycle-maintainvisible (1), flatlist-horizontal-maintainvisible (1), flatlist-horizontal-recycle-maintainvisible (1), flatlist-inverted-maintainvisible (1), flatlist-inverted-recycle-maintainvisible (1), flatlist-maintainvisible (1), flatlist-momentum-scroll-maintainvisible (1), flatlist-orientation-maintainvisible (1), flatlist-prepend-delete-maintainvisible (1), flatlist-pull-to-refresh-maintainvisible (1), flatlist-rapid-prepends-maintainvisible (1), flatlist-recycle-maintainvisible (1), flatlist-scrolltooffset-maintainvisible (1), flatlist-throttle-maintainvisible (1), flatlist-variable-height-first-prepend-maintainvisible (1), flatlist-variable-height-maintainvisible (1), flatlist-viewability (1), flatlist (1), launch-app-and-search (1), search (1), image-blur-prefetch (1), image-getsize-local-drawables (1), image-progressive-jpeg (1), image-wide-gamut (1), image (1), legacy-native-module (1), modal (1), new-arch-examples (1), pressable (1), scrollview-minindex-maintainvisible (1), scrollview-threshold-maintainvisible (1), sectionlist-viewability (1), text-width-mode (1), text (1), textinput-uncontrolled (1), touchable (1) | - | 49 | 1 |
| 2026-10-02 14:31 | [37020483607](https://github.com/react/react-native/actions/runs/37020483607) | ios release rntester | upstream | - | 48 | 1 | sectionlist-viewability (5) | - | 96 | 2 |
| 2026-10-02 14:31 | [37020483607](https://github.com/react/react-native/actions/runs/37020483607) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 14:31 | [37020483607](https://github.com/react/react-native/actions/runs/37020483607) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 14:31 | [37020483607](https://github.com/react/react-native/actions/runs/37020483607) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 14:31 | [37020483607](https://github.com/react/react-native/actions/runs/37020483607) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 11:55 | [37003745333](https://github.com/react/react-native/actions/runs/37003745333) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-02 11:55 | [37003745333](https://github.com/react/react-native/actions/runs/37003745333) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-02 11:55 | [37003745333](https://github.com/react/react-native/actions/runs/37003745333) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 11:55 | [37003745333](https://github.com/react/react-native/actions/runs/37003745333) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 11:55 | [37003745333](https://github.com/react/react-native/actions/runs/37003745333) | ios debug rntester | upstream | - | 48 | 2 | flatlist-throttle-maintainvisible (1), sectionlist-viewability (5) | - | 97 | 2 |
| 2026-10-02 11:55 | [37003745333](https://github.com/react/react-native/actions/runs/37003745333) | ios release rntester | upstream | - | 48 | 1 | sectionlist-viewability (8) | - | 99 | 2 |
| 2026-10-02 11:55 | [37003745333](https://github.com/react/react-native/actions/runs/37003745333) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 11:55 | [37003745333](https://github.com/react/react-native/actions/runs/37003745333) | ios debug templateapp | upstream | - | 1 | 1 | start (1) | - | 1 | 0 |
| 2026-10-02 11:09 | [36999455988](https://github.com/react/react-native/actions/runs/36999455988) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-02 11:09 | [36999455988](https://github.com/react/react-native/actions/runs/36999455988) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-02 11:09 | [36999455988](https://github.com/react/react-native/actions/runs/36999455988) | ios debug rntester | upstream | - | 48 | 2 | flatlist-delete-middle-maintainvisible (1), sectionlist-viewability (1) | - | 2 | 0 |
| 2026-10-02 11:09 | [36999455988](https://github.com/react/react-native/actions/runs/36999455988) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-10-02 11:09 | [36999455988](https://github.com/react/react-native/actions/runs/36999455988) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 11:09 | [36999455988](https://github.com/react/react-native/actions/runs/36999455988) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 11:09 | [36999455988](https://github.com/react/react-native/actions/runs/36999455988) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 11:09 | [36999455988](https://github.com/react/react-native/actions/runs/36999455988) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 10:46 | [36997293926](https://github.com/react/react-native/actions/runs/36997293926) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-02 10:46 | [36997293926](https://github.com/react/react-native/actions/runs/36997293926) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-02 10:46 | [36997293926](https://github.com/react/react-native/actions/runs/36997293926) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 10:46 | [36997293926](https://github.com/react/react-native/actions/runs/36997293926) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 10:46 | [36997293926](https://github.com/react/react-native/actions/runs/36997293926) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 10:46 | [36997293926](https://github.com/react/react-native/actions/runs/36997293926) | ios debug templateapp | upstream | - | 1 | 1 | start (1) | - | 1 | 0 |
| 2026-10-02 10:46 | [36997293926](https://github.com/react/react-native/actions/runs/36997293926) | ios debug rntester | upstream | - | 48 | 1 | filter-animated-blur (1) | - | 1 | 0 |
| 2026-10-02 10:46 | [36997293926](https://github.com/react/react-native/actions/runs/36997293926) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-10-02 10:33 | [36996153294](https://github.com/react/react-native/actions/runs/36996153294) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-02 10:33 | [36996153294](https://github.com/react/react-native/actions/runs/36996153294) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-02 10:33 | [36996153294](https://github.com/react/react-native/actions/runs/36996153294) | ios debug rntester | upstream | - | 48 | 2 | flatlist-recycle-maintainvisible (1) | sectionlist-viewability | 97 | 2 |
| 2026-10-02 10:33 | [36996153294](https://github.com/react/react-native/actions/runs/36996153294) | ios release rntester | upstream | - | 48 | 1 | sectionlist-viewability (10) | - | 96 | 2 |
| 2026-10-02 10:33 | [36996153294](https://github.com/react/react-native/actions/runs/36996153294) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 10:33 | [36996153294](https://github.com/react/react-native/actions/runs/36996153294) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 10:33 | [36996153294](https://github.com/react/react-native/actions/runs/36996153294) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 10:33 | [36996153294](https://github.com/react/react-native/actions/runs/36996153294) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 10:09 | [36993916028](https://github.com/react/react-native/actions/runs/36993916028) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-02 10:09 | [36993916028](https://github.com/react/react-native/actions/runs/36993916028) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-02 10:09 | [36993916028](https://github.com/react/react-native/actions/runs/36993916028) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 10:09 | [36993916028](https://github.com/react/react-native/actions/runs/36993916028) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 10:09 | [36993916028](https://github.com/react/react-native/actions/runs/36993916028) | ios debug rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-10-02 10:09 | [36993916028](https://github.com/react/react-native/actions/runs/36993916028) | ios release rntester | upstream | - | 48 | 1 | sectionlist-viewability (3) | - | 3 | 0 |
| 2026-10-02 10:09 | [36993916028](https://github.com/react/react-native/actions/runs/36993916028) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 10:09 | [36993916028](https://github.com/react/react-native/actions/runs/36993916028) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 09:51 | [36992149427](https://github.com/maestro-runner-bench/react-native/actions/runs/36992149427) | android debug rntester | ours | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-02 09:51 | [36992149427](https://github.com/maestro-runner-bench/react-native/actions/runs/36992149427) | android release rntester | ours | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-02 09:51 | [36992149427](https://github.com/maestro-runner-bench/react-native/actions/runs/36992149427) | android release templateapp | ours | - | 1 | 1 | start (5) | - | 5 | 1 |
| 2026-10-02 09:51 | [36992149427](https://github.com/maestro-runner-bench/react-native/actions/runs/36992149427) | android debug templateapp | ours | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 09:51 | [36992149427](https://github.com/maestro-runner-bench/react-native/actions/runs/36992149427) | ios release rntester | ours | - | 48 | 1 | animated-fade-in-view (1) | - | 1 | 0 |
| 2026-10-02 09:51 | [36992149427](https://github.com/maestro-runner-bench/react-native/actions/runs/36992149427) | ios debug rntester | ours | - | 48 | 1 | button (1) | - | 1 | 0 |
| 2026-10-02 09:36 | [36990729679](https://github.com/react/react-native/actions/runs/36990729679) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-02 09:36 | [36990729679](https://github.com/react/react-native/actions/runs/36990729679) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-02 09:36 | [36990729679](https://github.com/react/react-native/actions/runs/36990729679) | ios debug rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-10-02 09:36 | [36990729679](https://github.com/react/react-native/actions/runs/36990729679) | ios release rntester | upstream | - | 48 | 1 | sectionlist-viewability (1) | - | 1 | 0 |
| 2026-10-02 09:36 | [36990729679](https://github.com/react/react-native/actions/runs/36990729679) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 09:36 | [36990729679](https://github.com/react/react-native/actions/runs/36990729679) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 09:36 | [36990729679](https://github.com/react/react-native/actions/runs/36990729679) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 09:36 | [36990729679](https://github.com/react/react-native/actions/runs/36990729679) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 09:19 | [36989076382](https://github.com/react/react-native/actions/runs/36989076382) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-02 09:19 | [36989076382](https://github.com/react/react-native/actions/runs/36989076382) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-02 09:19 | [36989076382](https://github.com/react/react-native/actions/runs/36989076382) | android release templateapp | upstream | - | 1 | 1 | start (2) | - | 2 | 2 |
| 2026-10-02 09:19 | [36989076382](https://github.com/react/react-native/actions/runs/36989076382) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 09:19 | [36989076382](https://github.com/react/react-native/actions/runs/36989076382) | ios debug rntester | upstream | - | 48 | 3 | flatlist-horizontal-maintainvisible (1), flatlist-variable-height-maintainvisible (1), sectionlist-viewability (2) | - | 52 | 1 |
| 2026-10-02 09:19 | [36989076382](https://github.com/react/react-native/actions/runs/36989076382) | ios release rntester | upstream | - | 48 | 1 | sectionlist-viewability (5) | - | 48 | 1 |
| 2026-10-02 09:19 | [36989076382](https://github.com/react/react-native/actions/runs/36989076382) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-02 09:19 | [36989076382](https://github.com/react/react-native/actions/runs/36989076382) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 20:02 | [36918732275](https://github.com/react/react-native/actions/runs/36918732275) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-01 20:02 | [36918732275](https://github.com/react/react-native/actions/runs/36918732275) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-01 20:02 | [36918732275](https://github.com/react/react-native/actions/runs/36918732275) | ios debug rntester | upstream | - | 48 | 1 | alert (1) | - | 1 | 0 |
| 2026-10-01 20:02 | [36918732275](https://github.com/react/react-native/actions/runs/36918732275) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 20:02 | [36918732275](https://github.com/react/react-native/actions/runs/36918732275) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 20:02 | [36918732275](https://github.com/react/react-native/actions/runs/36918732275) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 20:02 | [36918732275](https://github.com/react/react-native/actions/runs/36918732275) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 19:51 | [36917319965](https://github.com/maestro-runner-bench/react-native/actions/runs/36917319965) | android debug rntester | ours | 86ed2d7 | 27 | 0 | - | - | 0 | 0 |
| 2026-10-01 19:51 | [36917319965](https://github.com/maestro-runner-bench/react-native/actions/runs/36917319965) | android release rntester | ours | 86ed2d7 | 51 | 0 | - | - | 0 | 0 |
| 2026-10-01 19:51 | [36917319965](https://github.com/maestro-runner-bench/react-native/actions/runs/36917319965) | android debug templateapp | ours | 86ed2d7 | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 19:51 | [36917319965](https://github.com/maestro-runner-bench/react-native/actions/runs/36917319965) | android release templateapp | ours | 86ed2d7 | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 19:51 | [36917319965](https://github.com/maestro-runner-bench/react-native/actions/runs/36917319965) | ios release templateapp | ours | 86ed2d7 | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 19:51 | [36917319965](https://github.com/maestro-runner-bench/react-native/actions/runs/36917319965) | ios debug templateapp | ours | 86ed2d7 | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 19:51 | [36917319965](https://github.com/maestro-runner-bench/react-native/actions/runs/36917319965) | ios release rntester | ours | 86ed2d7 | 37 | 32 | - | animated-fade-in-view, appearance, button, fabric-interop-add-children, filter-animated-blur, flatlist-append-maintainvisible, flatlist-complex-mutations-maintainvisible, flatlist-delete-anchor-maintainvisible, flatlist-delete-middle-maintainvisible, flatlist-empty-list-maintainvisible, flatlist-first-prepend-maintainvisible, flatlist-horizontal-add50-reset-maintainvisible, flatlist-horizontal-inverted-maintainvisible, flatlist-horizontal-inverted-recycle-maintainvisible, flatlist-horizontal-maintainvisible, flatlist-horizontal-recycle-maintainvisible, flatlist-inverted-maintainvisible, flatlist-inverted-recycle-maintainvisible, flatlist-maintainvisible, flatlist-momentum-scroll-maintainvisible, flatlist-orientation-maintainvisible, flatlist-prepend-delete-maintainvisible, flatlist-pull-to-refresh-maintainvisible, flatlist-rapid-prepends-maintainvisible, flatlist-recycle-maintainvisible, flatlist-scrolltooffset-maintainvisible, flatlist-throttle-maintainvisible, flatlist-variable-height-first-prepend-maintainvisible, flatlist-variable-height-maintainvisible, flatlist-viewability, flatlist, image | 21 | 0 |
| 2026-10-01 19:51 | [36917319965](https://github.com/maestro-runner-bench/react-native/actions/runs/36917319965) | ios debug rntester | ours | 86ed2d7 | 39 | 33 | - | appearance, button, fabric-interop-add-children, filter-animated-blur, flatlist-append-maintainvisible, flatlist-complex-mutations-maintainvisible, flatlist-delete-anchor-maintainvisible, flatlist-delete-middle-maintainvisible, flatlist-empty-list-maintainvisible, flatlist-first-prepend-maintainvisible, flatlist-horizontal-add50-reset-maintainvisible, flatlist-horizontal-inverted-maintainvisible, flatlist-horizontal-inverted-recycle-maintainvisible, flatlist-horizontal-maintainvisible, flatlist-horizontal-recycle-maintainvisible, flatlist-inverted-maintainvisible, flatlist-inverted-recycle-maintainvisible, flatlist-maintainvisible, flatlist-momentum-scroll-maintainvisible, flatlist-orientation-maintainvisible, flatlist-prepend-delete-maintainvisible, flatlist-pull-to-refresh-maintainvisible, flatlist-rapid-prepends-maintainvisible, flatlist-recycle-maintainvisible, flatlist-scrolltooffset-maintainvisible, flatlist-throttle-maintainvisible, flatlist-variable-height-first-prepend-maintainvisible, flatlist-variable-height-maintainvisible, flatlist-viewability, flatlist, image, legacy-native-module, modal | 51 | 0 |
| 2026-10-01 19:22 | [36913783613](https://github.com/react/react-native/actions/runs/36913783613) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-01 19:22 | [36913783613](https://github.com/react/react-native/actions/runs/36913783613) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-01 19:22 | [36913783613](https://github.com/react/react-native/actions/runs/36913783613) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 19:22 | [36913783613](https://github.com/react/react-native/actions/runs/36913783613) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 19:22 | [36913783613](https://github.com/react/react-native/actions/runs/36913783613) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 19:22 | [36913783613](https://github.com/react/react-native/actions/runs/36913783613) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 19:22 | [36913783613](https://github.com/react/react-native/actions/runs/36913783613) | ios debug rntester | upstream | - | 48 | 1 | new-arch-examples (1) | - | 1 | 0 |
| 2026-10-01 19:22 | [36913783613](https://github.com/react/react-native/actions/runs/36913783613) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-10-01 18:26 | [36906859420](https://github.com/react/react-native/actions/runs/36906859420) | android debug rntester | upstream | - | 27 | 25 | alert (1), animated-fade-in-view (1), appearance (1), button (1), filter-animated-blur (1), flatlist-viewability (1), flatlist (1), launch-app-and-search (1), search (1), image-blur-prefetch (1), image-getsize-local-drawables (1), image-progressive-jpeg (1), image-wide-gamut (1), image (1), legacy-native-module (1), modal (1), new-arch-examples (1), pressable (1), scrollview-minindex-maintainvisible (1), scrollview-threshold-maintainvisible (1), sectionlist-viewability (1), text-width-mode (1), text (1), textinput-uncontrolled (1), touchable (1) | - | 25 | 1 |
| 2026-10-01 18:26 | [36906859420](https://github.com/react/react-native/actions/runs/36906859420) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-01 18:26 | [36906859420](https://github.com/react/react-native/actions/runs/36906859420) | ios release rntester | upstream | - | 48 | 1 | sectionlist-viewability (2) | - | 2 | 0 |
| 2026-10-01 18:26 | [36906859420](https://github.com/react/react-native/actions/runs/36906859420) | ios debug rntester | upstream | - | 48 | 1 | legacy-native-module (1) | - | 1 | 0 |
| 2026-10-01 18:26 | [36906859420](https://github.com/react/react-native/actions/runs/36906859420) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 18:26 | [36906859420](https://github.com/react/react-native/actions/runs/36906859420) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 18:26 | [36906859420](https://github.com/react/react-native/actions/runs/36906859420) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 18:26 | [36906859420](https://github.com/react/react-native/actions/runs/36906859420) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 17:45 | [36901698066](https://github.com/react/react-native/actions/runs/36901698066) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-01 17:45 | [36901698066](https://github.com/react/react-native/actions/runs/36901698066) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-01 17:45 | [36901698066](https://github.com/react/react-native/actions/runs/36901698066) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 17:45 | [36901698066](https://github.com/react/react-native/actions/runs/36901698066) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 17:45 | [36901698066](https://github.com/react/react-native/actions/runs/36901698066) | ios release rntester | upstream | - | 48 | 1 | sectionlist-viewability (5) | - | 48 | 1 |
| 2026-10-01 17:45 | [36901698066](https://github.com/react/react-native/actions/runs/36901698066) | ios debug rntester | upstream | - | 48 | 1 | sectionlist-viewability (2) | - | 50 | 1 |
| 2026-10-01 17:45 | [36901698066](https://github.com/react/react-native/actions/runs/36901698066) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 17:45 | [36901698066](https://github.com/react/react-native/actions/runs/36901698066) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 17:32 | [36900091671](https://github.com/react/react-native/actions/runs/36900091671) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-01 17:32 | [36900091671](https://github.com/react/react-native/actions/runs/36900091671) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-01 17:32 | [36900091671](https://github.com/react/react-native/actions/runs/36900091671) | ios release rntester | upstream | - | 48 | 1 | sectionlist-viewability (5) | - | 48 | 1 |
| 2026-10-01 17:32 | [36900091671](https://github.com/react/react-native/actions/runs/36900091671) | ios debug rntester | upstream | - | 48 | 2 | flatlist-horizontal-add50-reset-maintainvisible (1), flatlist (1) | - | 50 | 1 |
| 2026-10-01 17:32 | [36900091671](https://github.com/react/react-native/actions/runs/36900091671) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 17:32 | [36900091671](https://github.com/react/react-native/actions/runs/36900091671) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 17:32 | [36900091671](https://github.com/react/react-native/actions/runs/36900091671) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 17:32 | [36900091671](https://github.com/react/react-native/actions/runs/36900091671) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 17:17 | [36898270680](https://github.com/maestro-runner-bench/react-native/actions/runs/36898270680) | android debug rntester | ours | d51beed | 27 | 1 | - | flatlist-viewability | 2 | 2 |
| 2026-10-01 17:17 | [36898270680](https://github.com/maestro-runner-bench/react-native/actions/runs/36898270680) | android release rntester | ours | d51beed | 51 | 22 | flatlist-complex-mutations-maintainvisible (1), flatlist-delete-middle-maintainvisible (1), flatlist-empty-list-maintainvisible (2), flatlist-horizontal-add50-reset-maintainvisible (2) | flatlist-horizontal-inverted-maintainvisible, flatlist-horizontal-inverted-recycle-maintainvisible, flatlist-horizontal-maintainvisible, flatlist-horizontal-recycle-maintainvisible, flatlist-inverted-maintainvisible, flatlist-inverted-recycle-maintainvisible, flatlist-maintainvisible, flatlist-momentum-scroll-maintainvisible, flatlist-orientation-maintainvisible, flatlist-prepend-delete-maintainvisible, flatlist-pull-to-refresh-maintainvisible, flatlist-rapid-prepends-maintainvisible, flatlist-recycle-maintainvisible, flatlist-scrolltooffset-maintainvisible, flatlist-throttle-maintainvisible, flatlist-variable-height-first-prepend-maintainvisible, flatlist-variable-height-maintainvisible, flatlist-viewability | 42 | 2 |
| 2026-10-01 17:17 | [36898270680](https://github.com/maestro-runner-bench/react-native/actions/runs/36898270680) | android release templateapp | ours | d51beed | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 17:17 | [36898270680](https://github.com/maestro-runner-bench/react-native/actions/runs/36898270680) | android debug templateapp | ours | d51beed | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 17:17 | [36898270680](https://github.com/maestro-runner-bench/react-native/actions/runs/36898270680) | ios debug templateapp | ours | d51beed | 1 | 0 | - | - | 0 | 1 |
| 2026-10-01 17:17 | [36898270680](https://github.com/maestro-runner-bench/react-native/actions/runs/36898270680) | ios release templateapp | ours | d51beed | 1 | 0 | - | - | 1 | 1 |
| 2026-10-01 17:17 | [36898270680](https://github.com/maestro-runner-bench/react-native/actions/runs/36898270680) | ios debug rntester | ours | d51beed | 2 | 1 | - | animated-fade-in-view | 0 | 0 |
| 2026-10-01 17:17 | [36898270680](https://github.com/maestro-runner-bench/react-native/actions/runs/36898270680) | ios release rntester | ours | d51beed | 2 | 1 | - | animated-fade-in-view | 0 | 0 |
| 2026-10-01 15:12 | [36882464491](https://github.com/react/react-native/actions/runs/36882464491) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-01 15:12 | [36882464491](https://github.com/react/react-native/actions/runs/36882464491) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-01 15:12 | [36882464491](https://github.com/react/react-native/actions/runs/36882464491) | ios debug rntester | upstream | - | 48 | 1 | flatlist-horizontal-inverted-recycle-maintainvisible (1) | - | 1 | 0 |
| 2026-10-01 15:12 | [36882464491](https://github.com/react/react-native/actions/runs/36882464491) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-10-01 15:12 | [36882464491](https://github.com/react/react-native/actions/runs/36882464491) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 15:12 | [36882464491](https://github.com/react/react-native/actions/runs/36882464491) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 15:12 | [36882464491](https://github.com/react/react-native/actions/runs/36882464491) | android release templateapp | upstream | - | 1 | 1 | start (1) | - | 1 | 1 |
| 2026-10-01 15:12 | [36882464491](https://github.com/react/react-native/actions/runs/36882464491) | android debug templateapp | upstream | - | 1 | 1 | start (1) | - | 1 | 1 |
| 2026-10-01 14:27 | [36876534417](https://github.com/react/react-native/actions/runs/36876534417) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-01 14:27 | [36876534417](https://github.com/react/react-native/actions/runs/36876534417) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-01 14:27 | [36876534417](https://github.com/react/react-native/actions/runs/36876534417) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 14:27 | [36876534417](https://github.com/react/react-native/actions/runs/36876534417) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 14:27 | [36876534417](https://github.com/react/react-native/actions/runs/36876534417) | ios debug rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-10-01 14:27 | [36876534417](https://github.com/react/react-native/actions/runs/36876534417) | ios release rntester | upstream | - | 48 | 1 | sectionlist-viewability (4) | - | 4 | 0 |
| 2026-10-01 14:27 | [36876534417](https://github.com/react/react-native/actions/runs/36876534417) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 14:27 | [36876534417](https://github.com/react/react-native/actions/runs/36876534417) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 14:17 | [36875235571](https://github.com/react/react-native/actions/runs/36875235571) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-01 14:17 | [36875235571](https://github.com/react/react-native/actions/runs/36875235571) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-01 14:17 | [36875235571](https://github.com/react/react-native/actions/runs/36875235571) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 14:17 | [36875235571](https://github.com/react/react-native/actions/runs/36875235571) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 14:17 | [36875235571](https://github.com/react/react-native/actions/runs/36875235571) | ios release rntester | upstream | - | 48 | 2 | scrollview-minindex-maintainvisible (2), sectionlist-viewability (12) | - | 100 | 2 |
| 2026-10-01 14:17 | [36875235571](https://github.com/react/react-native/actions/runs/36875235571) | ios debug rntester | upstream | - | 48 | 2 | flatlist-delete-anchor-maintainvisible (1), flatlist-variable-height-maintainvisible (1) | - | 98 | 2 |
| 2026-10-01 14:17 | [36875235571](https://github.com/react/react-native/actions/runs/36875235571) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 14:17 | [36875235571](https://github.com/react/react-native/actions/runs/36875235571) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 13:14 | [36867264862](https://github.com/react/react-native/actions/runs/36867264862) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-01 13:14 | [36867264862](https://github.com/react/react-native/actions/runs/36867264862) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-01 13:14 | [36867264862](https://github.com/react/react-native/actions/runs/36867264862) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-10-01 13:14 | [36867264862](https://github.com/react/react-native/actions/runs/36867264862) | ios debug rntester | upstream | - | 48 | 1 | filter-animated-blur (1) | - | 1 | 0 |
| 2026-10-01 13:14 | [36867264862](https://github.com/react/react-native/actions/runs/36867264862) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 13:14 | [36867264862](https://github.com/react/react-native/actions/runs/36867264862) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 13:14 | [36867264862](https://github.com/react/react-native/actions/runs/36867264862) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 13:14 | [36867264862](https://github.com/react/react-native/actions/runs/36867264862) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 13:06 | [36866271124](https://github.com/react/react-native/actions/runs/36866271124) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-01 13:06 | [36866271124](https://github.com/react/react-native/actions/runs/36866271124) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-01 13:06 | [36866271124](https://github.com/react/react-native/actions/runs/36866271124) | ios debug rntester | upstream | - | 48 | 2 | flatlist-viewability (1), sectionlist-viewability (1) | - | 50 | 1 |
| 2026-10-01 13:06 | [36866271124](https://github.com/react/react-native/actions/runs/36866271124) | ios release rntester | upstream | - | 48 | 1 | modal (1) | - | 39 | 1 |
| 2026-10-01 13:06 | [36866271124](https://github.com/react/react-native/actions/runs/36866271124) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 13:06 | [36866271124](https://github.com/react/react-native/actions/runs/36866271124) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 13:06 | [36866271124](https://github.com/react/react-native/actions/runs/36866271124) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 13:06 | [36866271124](https://github.com/react/react-native/actions/runs/36866271124) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 12:47 | [36864159166](https://github.com/react/react-native/actions/runs/36864159166) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-01 12:47 | [36864159166](https://github.com/react/react-native/actions/runs/36864159166) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-01 12:47 | [36864159166](https://github.com/react/react-native/actions/runs/36864159166) | ios debug rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-10-01 12:47 | [36864159166](https://github.com/react/react-native/actions/runs/36864159166) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-10-01 12:47 | [36864159166](https://github.com/react/react-native/actions/runs/36864159166) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 12:47 | [36864159166](https://github.com/react/react-native/actions/runs/36864159166) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 12:47 | [36864159166](https://github.com/react/react-native/actions/runs/36864159166) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 12:47 | [36864159166](https://github.com/react/react-native/actions/runs/36864159166) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 12:42 | [36863586697](https://github.com/react/react-native/actions/runs/36863586697) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-01 12:42 | [36863586697](https://github.com/react/react-native/actions/runs/36863586697) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-01 12:42 | [36863586697](https://github.com/react/react-native/actions/runs/36863586697) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-10-01 12:42 | [36863586697](https://github.com/react/react-native/actions/runs/36863586697) | ios debug rntester | upstream | - | 48 | 1 | sectionlist-viewability (2) | - | 2 | 0 |
| 2026-10-01 12:42 | [36863586697](https://github.com/react/react-native/actions/runs/36863586697) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 12:42 | [36863586697](https://github.com/react/react-native/actions/runs/36863586697) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 12:42 | [36863586697](https://github.com/react/react-native/actions/runs/36863586697) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 12:42 | [36863586697](https://github.com/react/react-native/actions/runs/36863586697) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 09:56 | [36845916549](https://github.com/react/react-native/actions/runs/36845916549) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-10-01 09:56 | [36845916549](https://github.com/react/react-native/actions/runs/36845916549) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-10-01 09:56 | [36845916549](https://github.com/react/react-native/actions/runs/36845916549) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 09:56 | [36845916549](https://github.com/react/react-native/actions/runs/36845916549) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 09:56 | [36845916549](https://github.com/react/react-native/actions/runs/36845916549) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-10-01 09:56 | [36845916549](https://github.com/react/react-native/actions/runs/36845916549) | ios debug rntester | upstream | - | 48 | 1 | sectionlist-viewability (2) | - | 2 | 0 |
| 2026-10-01 09:56 | [36845916549](https://github.com/react/react-native/actions/runs/36845916549) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-10-01 09:56 | [36845916549](https://github.com/react/react-native/actions/runs/36845916549) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-30 23:35 | [36791912465](https://github.com/react/react-native/actions/runs/36791912465) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-09-30 23:35 | [36791912465](https://github.com/react/react-native/actions/runs/36791912465) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-09-30 23:35 | [36791912465](https://github.com/react/react-native/actions/runs/36791912465) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-30 23:35 | [36791912465](https://github.com/react/react-native/actions/runs/36791912465) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-30 23:35 | [36791912465](https://github.com/react/react-native/actions/runs/36791912465) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-09-30 23:35 | [36791912465](https://github.com/react/react-native/actions/runs/36791912465) | ios debug rntester | upstream | - | 48 | 1 | textinput-uncontrolled (1) | - | 1 | 0 |
| 2026-09-30 21:24 | [36779183435](https://github.com/react/react-native/actions/runs/36779183435) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-09-30 21:24 | [36779183435](https://github.com/react/react-native/actions/runs/36779183435) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-09-30 21:24 | [36779183435](https://github.com/react/react-native/actions/runs/36779183435) | ios debug rntester | upstream | - | 48 | 1 | flatlist-inverted-maintainvisible (1) | - | 1 | 0 |
| 2026-09-30 21:24 | [36779183435](https://github.com/react/react-native/actions/runs/36779183435) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-09-30 21:24 | [36779183435](https://github.com/react/react-native/actions/runs/36779183435) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-30 21:24 | [36779183435](https://github.com/react/react-native/actions/runs/36779183435) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 1 |
| 2026-09-30 21:24 | [36779183435](https://github.com/react/react-native/actions/runs/36779183435) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-30 21:24 | [36779183435](https://github.com/react/react-native/actions/runs/36779183435) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-30 20:56 | [36776081983](https://github.com/react/react-native/actions/runs/36776081983) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-09-30 20:56 | [36776081983](https://github.com/react/react-native/actions/runs/36776081983) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-09-30 20:56 | [36776081983](https://github.com/react/react-native/actions/runs/36776081983) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-30 20:56 | [36776081983](https://github.com/react/react-native/actions/runs/36776081983) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-30 20:56 | [36776081983](https://github.com/react/react-native/actions/runs/36776081983) | ios debug rntester | upstream | - | 48 | 1 | textinput-uncontrolled (1) | - | 49 | 1 |
| 2026-09-30 20:56 | [36776081983](https://github.com/react/react-native/actions/runs/36776081983) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 1 |
| 2026-09-30 20:56 | [36776081983](https://github.com/react/react-native/actions/runs/36776081983) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-30 20:56 | [36776081983](https://github.com/react/react-native/actions/runs/36776081983) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-30 19:41 | [36767364423](https://github.com/react/react-native/actions/runs/36767364423) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-09-30 19:41 | [36767364423](https://github.com/react/react-native/actions/runs/36767364423) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-09-30 19:41 | [36767364423](https://github.com/react/react-native/actions/runs/36767364423) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-30 19:41 | [36767364423](https://github.com/react/react-native/actions/runs/36767364423) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-30 19:41 | [36767364423](https://github.com/react/react-native/actions/runs/36767364423) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-09-30 19:41 | [36767364423](https://github.com/react/react-native/actions/runs/36767364423) | ios debug rntester | upstream | - | 48 | 2 | flatlist-inverted-recycle-maintainvisible (1), flatlist (1) | - | 2 | 0 |
| 2026-09-30 19:41 | [36767364423](https://github.com/react/react-native/actions/runs/36767364423) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-30 19:41 | [36767364423](https://github.com/react/react-native/actions/runs/36767364423) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-30 17:12 | [36749789163](https://github.com/react/react-native/actions/runs/36749789163) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-09-30 17:12 | [36749789163](https://github.com/react/react-native/actions/runs/36749789163) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-09-30 17:12 | [36749789163](https://github.com/react/react-native/actions/runs/36749789163) | android debug templateapp | upstream | - | 1 | 1 | start (1) | - | 1 | 1 |
| 2026-09-30 17:12 | [36749789163](https://github.com/react/react-native/actions/runs/36749789163) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-30 17:12 | [36749789163](https://github.com/react/react-native/actions/runs/36749789163) | ios debug rntester | upstream | - | 48 | 2 | scrollview-minindex-maintainvisible (2), sectionlist-viewability (4) | - | 6 | 0 |
| 2026-09-30 17:12 | [36749789163](https://github.com/react/react-native/actions/runs/36749789163) | ios release rntester | upstream | - | 48 | 1 | sectionlist-viewability (2) | - | 2 | 0 |
| 2026-09-30 17:12 | [36749789163](https://github.com/react/react-native/actions/runs/36749789163) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-30 17:12 | [36749789163](https://github.com/react/react-native/actions/runs/36749789163) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-30 14:59 | [36733364499](https://github.com/react/react-native/actions/runs/36733364499) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-09-30 14:59 | [36733364499](https://github.com/react/react-native/actions/runs/36733364499) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-09-30 14:59 | [36733364499](https://github.com/react/react-native/actions/runs/36733364499) | ios release rntester | upstream | - | 48 | 1 | sectionlist-viewability (5) | - | 96 | 2 |
| 2026-09-30 14:59 | [36733364499](https://github.com/react/react-native/actions/runs/36733364499) | ios debug rntester | upstream | - | 48 | 3 | flatlist-pull-to-refresh-maintainvisible (1), scrollview-minindex-maintainvisible (3), sectionlist-viewability (5) | - | 100 | 2 |
| 2026-09-30 14:59 | [36733364499](https://github.com/react/react-native/actions/runs/36733364499) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-30 14:59 | [36733364499](https://github.com/react/react-native/actions/runs/36733364499) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-30 14:59 | [36733364499](https://github.com/react/react-native/actions/runs/36733364499) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-30 14:59 | [36733364499](https://github.com/react/react-native/actions/runs/36733364499) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-30 02:09 | [36658520210](https://github.com/react/react-native/actions/runs/36658520210) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-09-30 02:09 | [36658520210](https://github.com/react/react-native/actions/runs/36658520210) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-09-30 02:09 | [36658520210](https://github.com/react/react-native/actions/runs/36658520210) | ios debug rntester | upstream | - | 48 | 2 | flatlist-complex-mutations-maintainvisible (1), sectionlist-viewability (3) | - | 52 | 1 |
| 2026-09-30 02:09 | [36658520210](https://github.com/react/react-native/actions/runs/36658520210) | ios release rntester | upstream | - | 48 | 1 | sectionlist-viewability (5) | - | 48 | 1 |
| 2026-09-30 02:09 | [36658520210](https://github.com/react/react-native/actions/runs/36658520210) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-30 02:09 | [36658520210](https://github.com/react/react-native/actions/runs/36658520210) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-30 02:09 | [36658520210](https://github.com/react/react-native/actions/runs/36658520210) | ios debug templateapp | upstream | - | 1 | 1 | start (1) | - | 1 | 0 |
| 2026-09-30 02:09 | [36658520210](https://github.com/react/react-native/actions/runs/36658520210) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 18:54 | [36615400018](https://github.com/react/react-native/actions/runs/36615400018) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-09-29 18:54 | [36615400018](https://github.com/react/react-native/actions/runs/36615400018) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-09-29 18:54 | [36615400018](https://github.com/react/react-native/actions/runs/36615400018) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 18:54 | [36615400018](https://github.com/react/react-native/actions/runs/36615400018) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 18:54 | [36615400018](https://github.com/react/react-native/actions/runs/36615400018) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-09-29 18:54 | [36615400018](https://github.com/react/react-native/actions/runs/36615400018) | ios debug rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-09-29 18:54 | [36615400018](https://github.com/react/react-native/actions/runs/36615400018) | ios debug templateapp | upstream | - | 1 | 1 | start (1) | - | 1 | 0 |
| 2026-09-29 18:54 | [36615400018](https://github.com/react/react-native/actions/runs/36615400018) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 17:07 | [36602659426](https://github.com/react/react-native/actions/runs/36602659426) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-09-29 17:07 | [36602659426](https://github.com/react/react-native/actions/runs/36602659426) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-09-29 17:07 | [36602659426](https://github.com/react/react-native/actions/runs/36602659426) | ios release rntester | upstream | - | 48 | 1 | sectionlist-viewability (1) | - | 97 | 2 |
| 2026-09-29 17:07 | [36602659426](https://github.com/react/react-native/actions/runs/36602659426) | ios debug rntester | upstream | - | 48 | 4 | new-arch-examples (1), scrollview-minindex-maintainvisible (3), scrollview-threshold-maintainvisible (7), sectionlist-viewability (10) | - | 107 | 2 |
| 2026-09-29 17:07 | [36602659426](https://github.com/react/react-native/actions/runs/36602659426) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 17:07 | [36602659426](https://github.com/react/react-native/actions/runs/36602659426) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 17:07 | [36602659426](https://github.com/react/react-native/actions/runs/36602659426) | ios debug templateapp | upstream | - | 1 | 1 | start (1) | - | 1 | 0 |
| 2026-09-29 17:07 | [36602659426](https://github.com/react/react-native/actions/runs/36602659426) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 16:53 | [36601037859](https://github.com/react/react-native/actions/runs/36601037859) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-09-29 16:53 | [36601037859](https://github.com/react/react-native/actions/runs/36601037859) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-09-29 16:53 | [36601037859](https://github.com/react/react-native/actions/runs/36601037859) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 16:53 | [36601037859](https://github.com/react/react-native/actions/runs/36601037859) | android debug templateapp | upstream | - | 1 | 1 | start (1) | - | 1 | 1 |
| 2026-09-29 16:53 | [36601037859](https://github.com/react/react-native/actions/runs/36601037859) | ios release rntester | upstream | - | 48 | 1 | sectionlist-viewability (3) | - | 3 | 0 |
| 2026-09-29 16:53 | [36601037859](https://github.com/react/react-native/actions/runs/36601037859) | ios debug rntester | upstream | - | 48 | 2 | flatlist-delete-middle-maintainvisible (1), sectionlist-viewability (1) | - | 2 | 0 |
| 2026-09-29 16:53 | [36601037859](https://github.com/react/react-native/actions/runs/36601037859) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 16:53 | [36601037859](https://github.com/react/react-native/actions/runs/36601037859) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 16:47 | [36600300559](https://github.com/react/react-native/actions/runs/36600300559) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-09-29 16:47 | [36600300559](https://github.com/react/react-native/actions/runs/36600300559) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-09-29 16:47 | [36600300559](https://github.com/react/react-native/actions/runs/36600300559) | ios debug rntester | upstream | - | 48 | 1 | sectionlist-viewability (1) | - | 1 | 0 |
| 2026-09-29 16:47 | [36600300559](https://github.com/react/react-native/actions/runs/36600300559) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-09-29 16:47 | [36600300559](https://github.com/react/react-native/actions/runs/36600300559) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 16:47 | [36600300559](https://github.com/react/react-native/actions/runs/36600300559) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 16:47 | [36600300559](https://github.com/react/react-native/actions/runs/36600300559) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 16:47 | [36600300559](https://github.com/react/react-native/actions/runs/36600300559) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 16:43 | [36599816010](https://github.com/react/react-native/actions/runs/36599816010) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-09-29 16:43 | [36599816010](https://github.com/react/react-native/actions/runs/36599816010) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-09-29 16:43 | [36599816010](https://github.com/react/react-native/actions/runs/36599816010) | ios debug rntester | upstream | - | 48 | 1 | flatlist-variable-height-first-prepend-maintainvisible (1) | - | 49 | 1 |
| 2026-09-29 16:43 | [36599816010](https://github.com/react/react-native/actions/runs/36599816010) | ios release rntester | upstream | - | 48 | 3 | flatlist-empty-list-maintainvisible (1), scrollview-threshold-maintainvisible (2), sectionlist-viewability (6) | - | 52 | 1 |
| 2026-09-29 16:43 | [36599816010](https://github.com/react/react-native/actions/runs/36599816010) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 16:43 | [36599816010](https://github.com/react/react-native/actions/runs/36599816010) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 16:43 | [36599816010](https://github.com/react/react-native/actions/runs/36599816010) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 16:43 | [36599816010](https://github.com/react/react-native/actions/runs/36599816010) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 15:15 | [36588841649](https://github.com/react/react-native/actions/runs/36588841649) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-09-29 15:15 | [36588841649](https://github.com/react/react-native/actions/runs/36588841649) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-09-29 15:15 | [36588841649](https://github.com/react/react-native/actions/runs/36588841649) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 15:15 | [36588841649](https://github.com/react/react-native/actions/runs/36588841649) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 15:15 | [36588841649](https://github.com/react/react-native/actions/runs/36588841649) | ios debug rntester | upstream | - | 48 | 2 | flatlist-orientation-maintainvisible (1), sectionlist-viewability (1) | - | 2 | 0 |
| 2026-09-29 15:15 | [36588841649](https://github.com/react/react-native/actions/runs/36588841649) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-09-29 15:15 | [36588841649](https://github.com/react/react-native/actions/runs/36588841649) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 15:15 | [36588841649](https://github.com/react/react-native/actions/runs/36588841649) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 13:58 | [36579064202](https://github.com/react/react-native/actions/runs/36579064202) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-09-29 13:58 | [36579064202](https://github.com/react/react-native/actions/runs/36579064202) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-09-29 13:58 | [36579064202](https://github.com/react/react-native/actions/runs/36579064202) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 13:58 | [36579064202](https://github.com/react/react-native/actions/runs/36579064202) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 13:58 | [36579064202](https://github.com/react/react-native/actions/runs/36579064202) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-09-29 13:58 | [36579064202](https://github.com/react/react-native/actions/runs/36579064202) | ios debug rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-09-29 13:58 | [36579064202](https://github.com/react/react-native/actions/runs/36579064202) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 13:58 | [36579064202](https://github.com/react/react-native/actions/runs/36579064202) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 13:48 | [36577830851](https://github.com/react/react-native/actions/runs/36577830851) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-09-29 13:48 | [36577830851](https://github.com/react/react-native/actions/runs/36577830851) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-09-29 13:48 | [36577830851](https://github.com/react/react-native/actions/runs/36577830851) | ios release rntester | upstream | - | 48 | 1 | sectionlist-viewability (3) | - | 51 | 1 |
| 2026-09-29 13:48 | [36577830851](https://github.com/react/react-native/actions/runs/36577830851) | ios debug rntester | upstream | - | 48 | 3 | flatlist-scrolltooffset-maintainvisible (1), scrollview-threshold-maintainvisible (3), sectionlist-viewability (5) | - | 52 | 1 |
| 2026-09-29 13:48 | [36577830851](https://github.com/react/react-native/actions/runs/36577830851) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 13:48 | [36577830851](https://github.com/react/react-native/actions/runs/36577830851) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 13:48 | [36577830851](https://github.com/react/react-native/actions/runs/36577830851) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 13:48 | [36577830851](https://github.com/react/react-native/actions/runs/36577830851) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 13:39 | [36576766847](https://github.com/react/react-native/actions/runs/36576766847) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-09-29 13:39 | [36576766847](https://github.com/react/react-native/actions/runs/36576766847) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 1 |
| 2026-09-29 13:39 | [36576766847](https://github.com/react/react-native/actions/runs/36576766847) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 13:39 | [36576766847](https://github.com/react/react-native/actions/runs/36576766847) | android release templateapp | upstream | - | 1 | 1 | start (1) | - | 1 | 1 |
| 2026-09-29 13:39 | [36576766847](https://github.com/react/react-native/actions/runs/36576766847) | ios release rntester | upstream | - | 48 | 2 | flatlist-orientation-maintainvisible (1), sectionlist-viewability (5) | - | 49 | 1 |
| 2026-09-29 13:39 | [36576766847](https://github.com/react/react-native/actions/runs/36576766847) | ios debug rntester | upstream | - | 48 | 1 | flatlist-viewability (1) | - | 1 | 1 |
| 2026-09-29 13:39 | [36576766847](https://github.com/react/react-native/actions/runs/36576766847) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 13:39 | [36576766847](https://github.com/react/react-native/actions/runs/36576766847) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 11:36 | [36562762399](https://github.com/react/react-native/actions/runs/36562762399) | android release rntester | upstream | - | 51 | 49 | alert (1), animated-fade-in-view (1), appearance (1), button (1), filter-animated-blur (1), flatlist-append-maintainvisible (1), flatlist-complex-mutations-maintainvisible (1), flatlist-delete-anchor-maintainvisible (1), flatlist-delete-middle-maintainvisible (1), flatlist-empty-list-maintainvisible (1), flatlist-first-prepend-maintainvisible (1), flatlist-horizontal-add50-reset-maintainvisible (1), flatlist-horizontal-inverted-maintainvisible (1), flatlist-horizontal-inverted-recycle-maintainvisible (1), flatlist-horizontal-maintainvisible (1), flatlist-horizontal-recycle-maintainvisible (1), flatlist-inverted-maintainvisible (1), flatlist-inverted-recycle-maintainvisible (1), flatlist-maintainvisible (1), flatlist-momentum-scroll-maintainvisible (1), flatlist-orientation-maintainvisible (1), flatlist-prepend-delete-maintainvisible (1), flatlist-pull-to-refresh-maintainvisible (1), flatlist-rapid-prepends-maintainvisible (1), flatlist-recycle-maintainvisible (1), flatlist-scrolltooffset-maintainvisible (1), flatlist-throttle-maintainvisible (1), flatlist-variable-height-first-prepend-maintainvisible (1), flatlist-variable-height-maintainvisible (1), flatlist-viewability (1), flatlist (1), launch-app-and-search (1), search (1), image-blur-prefetch (1), image-getsize-local-drawables (1), image-progressive-jpeg (1), image-wide-gamut (1), image (1), legacy-native-module (1), modal (1), new-arch-examples (1), pressable (1), scrollview-minindex-maintainvisible (1), scrollview-threshold-maintainvisible (1), sectionlist-viewability (1), text-width-mode (1), text (1), textinput-uncontrolled (1), touchable (1) | - | 49 | 1 |
| 2026-09-29 11:36 | [36562762399](https://github.com/react/react-native/actions/runs/36562762399) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-09-29 11:36 | [36562762399](https://github.com/react/react-native/actions/runs/36562762399) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 11:36 | [36562762399](https://github.com/react/react-native/actions/runs/36562762399) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 11:36 | [36562762399](https://github.com/react/react-native/actions/runs/36562762399) | ios release rntester | upstream | - | 48 | 1 | sectionlist-viewability (5) | - | 96 | 2 |
| 2026-09-29 11:36 | [36562762399](https://github.com/react/react-native/actions/runs/36562762399) | ios debug rntester | upstream | - | 48 | 4 | flatlist-scrolltooffset-maintainvisible (1), flatlist-viewability (1), scrollview-minindex-maintainvisible (5), sectionlist-viewability (5) | - | 96 | 2 |
| 2026-09-29 11:36 | [36562762399](https://github.com/react/react-native/actions/runs/36562762399) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 11:36 | [36562762399](https://github.com/react/react-native/actions/runs/36562762399) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 10:08 | [36553670490](https://github.com/react/react-native/actions/runs/36553670490) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-09-29 10:08 | [36553670490](https://github.com/react/react-native/actions/runs/36553670490) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-09-29 10:08 | [36553670490](https://github.com/react/react-native/actions/runs/36553670490) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-09-29 10:08 | [36553670490](https://github.com/react/react-native/actions/runs/36553670490) | ios debug rntester | upstream | - | 48 | 1 | sectionlist-viewability (2) | - | 2 | 0 |
| 2026-09-29 10:08 | [36553670490](https://github.com/react/react-native/actions/runs/36553670490) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 10:08 | [36553670490](https://github.com/react/react-native/actions/runs/36553670490) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-29 09:06 | [36547007634](https://github.com/react/react-native/actions/runs/36547007634) | ios debug rntester | upstream | - | 48 | 2 | flatlist-variable-height-first-prepend-maintainvisible (1), sectionlist-viewability (1) | - | 50 | 1 |
| 2026-09-29 09:06 | [36547007634](https://github.com/react/react-native/actions/runs/36547007634) | ios release rntester | upstream | - | 48 | 2 | scrollview-minindex-maintainvisible (2), sectionlist-viewability (5) | - | 50 | 1 |
| 2026-09-28 18:43 | [36467232773](https://github.com/react/react-native/actions/runs/36467232773) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-09-28 18:43 | [36467232773](https://github.com/react/react-native/actions/runs/36467232773) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-09-28 18:43 | [36467232773](https://github.com/react/react-native/actions/runs/36467232773) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 18:43 | [36467232773](https://github.com/react/react-native/actions/runs/36467232773) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 18:43 | [36467232773](https://github.com/react/react-native/actions/runs/36467232773) | ios debug rntester | upstream | - | 48 | 1 | sectionlist-viewability (1) | - | 1 | 0 |
| 2026-09-28 18:43 | [36467232773](https://github.com/react/react-native/actions/runs/36467232773) | ios release rntester | upstream | - | 48 | 1 | sectionlist-viewability (2) | - | 2 | 0 |
| 2026-09-28 18:43 | [36467232773](https://github.com/react/react-native/actions/runs/36467232773) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 18:25 | [36465034563](https://github.com/react/react-native/actions/runs/36465034563) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-09-28 18:25 | [36465034563](https://github.com/react/react-native/actions/runs/36465034563) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-09-28 18:25 | [36465034563](https://github.com/react/react-native/actions/runs/36465034563) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 18:25 | [36465034563](https://github.com/react/react-native/actions/runs/36465034563) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 18:25 | [36465034563](https://github.com/react/react-native/actions/runs/36465034563) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-09-28 18:25 | [36465034563](https://github.com/react/react-native/actions/runs/36465034563) | ios debug rntester | upstream | - | 48 | 2 | image (1), modal (1) | - | 2 | 0 |
| 2026-09-28 18:25 | [36465034563](https://github.com/react/react-native/actions/runs/36465034563) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 18:25 | [36465034563](https://github.com/react/react-native/actions/runs/36465034563) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 17:43 | [36460151200](https://github.com/react/react-native/actions/runs/36460151200) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-09-28 17:43 | [36460151200](https://github.com/react/react-native/actions/runs/36460151200) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-09-28 17:43 | [36460151200](https://github.com/react/react-native/actions/runs/36460151200) | ios release rntester | upstream | - | 48 | 1 | sectionlist-viewability (3) | - | 3 | 0 |
| 2026-09-28 17:43 | [36460151200](https://github.com/react/react-native/actions/runs/36460151200) | ios debug rntester | upstream | - | 48 | 1 | sectionlist-viewability (1) | - | 1 | 0 |
| 2026-09-28 17:43 | [36460151200](https://github.com/react/react-native/actions/runs/36460151200) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 17:43 | [36460151200](https://github.com/react/react-native/actions/runs/36460151200) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 17:43 | [36460151200](https://github.com/react/react-native/actions/runs/36460151200) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 17:43 | [36460151200](https://github.com/react/react-native/actions/runs/36460151200) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 17:01 | [36455174116](https://github.com/react/react-native/actions/runs/36455174116) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-09-28 17:01 | [36455174116](https://github.com/react/react-native/actions/runs/36455174116) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-09-28 17:01 | [36455174116](https://github.com/react/react-native/actions/runs/36455174116) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 17:01 | [36455174116](https://github.com/react/react-native/actions/runs/36455174116) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 17:01 | [36455174116](https://github.com/react/react-native/actions/runs/36455174116) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-09-28 17:01 | [36455174116](https://github.com/react/react-native/actions/runs/36455174116) | ios debug rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-09-28 17:01 | [36455174116](https://github.com/react/react-native/actions/runs/36455174116) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 17:01 | [36455174116](https://github.com/react/react-native/actions/runs/36455174116) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 16:55 | [36454478119](https://github.com/react/react-native/actions/runs/36454478119) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-09-28 16:55 | [36454478119](https://github.com/react/react-native/actions/runs/36454478119) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-09-28 16:55 | [36454478119](https://github.com/react/react-native/actions/runs/36454478119) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 16:55 | [36454478119](https://github.com/react/react-native/actions/runs/36454478119) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 16:55 | [36454478119](https://github.com/react/react-native/actions/runs/36454478119) | ios debug rntester | upstream | - | 48 | 3 | flatlist-recycle-maintainvisible (1), flatlist-throttle-maintainvisible (1), modal (1) | - | 3 | 0 |
| 2026-09-28 16:55 | [36454478119](https://github.com/react/react-native/actions/runs/36454478119) | ios release rntester | upstream | - | 48 | 1 | sectionlist-viewability (1) | - | 1 | 0 |
| 2026-09-28 16:55 | [36454478119](https://github.com/react/react-native/actions/runs/36454478119) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 16:55 | [36454478119](https://github.com/react/react-native/actions/runs/36454478119) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 13:47 | [36431079493](https://github.com/react/react-native/actions/runs/36431079493) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-09-28 13:47 | [36431079493](https://github.com/react/react-native/actions/runs/36431079493) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-09-28 13:47 | [36431079493](https://github.com/react/react-native/actions/runs/36431079493) | ios debug rntester | upstream | - | 44 | 5 | flatlist-empty-list-maintainvisible (1), scrollview-minindex-maintainvisible (5), scrollview-threshold-maintainvisible (1) | flatlist-prepend-delete-maintainvisible, sectionlist-viewability | 75 | 2 |
| 2026-09-28 13:47 | [36431079493](https://github.com/react/react-native/actions/runs/36431079493) | ios release rntester | upstream | - | 48 | 2 | image (1), sectionlist-viewability (5) | - | 85 | 2 |
| 2026-09-28 13:47 | [36431079493](https://github.com/react/react-native/actions/runs/36431079493) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 13:47 | [36431079493](https://github.com/react/react-native/actions/runs/36431079493) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 13:47 | [36431079493](https://github.com/react/react-native/actions/runs/36431079493) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 13:47 | [36431079493](https://github.com/react/react-native/actions/runs/36431079493) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 13:42 | [36430546119](https://github.com/react/react-native/actions/runs/36430546119) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-09-28 13:42 | [36430546119](https://github.com/react/react-native/actions/runs/36430546119) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-09-28 13:42 | [36430546119](https://github.com/react/react-native/actions/runs/36430546119) | ios debug rntester | upstream | - | 48 | 2 | image (1), sectionlist-viewability (1) | - | 2 | 0 |
| 2026-09-28 13:42 | [36430546119](https://github.com/react/react-native/actions/runs/36430546119) | ios release rntester | upstream | - | 48 | 1 | sectionlist-viewability (3) | - | 3 | 0 |
| 2026-09-28 13:42 | [36430546119](https://github.com/react/react-native/actions/runs/36430546119) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 13:42 | [36430546119](https://github.com/react/react-native/actions/runs/36430546119) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 13:42 | [36430546119](https://github.com/react/react-native/actions/runs/36430546119) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 13:42 | [36430546119](https://github.com/react/react-native/actions/runs/36430546119) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 12:37 | [36422996335](https://github.com/react/react-native/actions/runs/36422996335) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-09-28 12:37 | [36422996335](https://github.com/react/react-native/actions/runs/36422996335) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-09-28 12:37 | [36422996335](https://github.com/react/react-native/actions/runs/36422996335) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-09-28 12:37 | [36422996335](https://github.com/react/react-native/actions/runs/36422996335) | ios debug rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-09-28 12:37 | [36422996335](https://github.com/react/react-native/actions/runs/36422996335) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 12:37 | [36422996335](https://github.com/react/react-native/actions/runs/36422996335) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 12:37 | [36422996335](https://github.com/react/react-native/actions/runs/36422996335) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 12:37 | [36422996335](https://github.com/react/react-native/actions/runs/36422996335) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 12:29 | [36422135990](https://github.com/react/react-native/actions/runs/36422135990) | android release rntester | upstream | - | 51 | 0 | - | - | 0 | 0 |
| 2026-09-28 12:29 | [36422135990](https://github.com/react/react-native/actions/runs/36422135990) | android debug rntester | upstream | - | 27 | 0 | - | - | 0 | 0 |
| 2026-09-28 12:29 | [36422135990](https://github.com/react/react-native/actions/runs/36422135990) | ios debug rntester | upstream | - | 48 | 1 | button (1) | - | 1 | 0 |
| 2026-09-28 12:29 | [36422135990](https://github.com/react/react-native/actions/runs/36422135990) | ios release rntester | upstream | - | 48 | 0 | - | - | 0 | 0 |
| 2026-09-28 12:29 | [36422135990](https://github.com/react/react-native/actions/runs/36422135990) | android release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 12:29 | [36422135990](https://github.com/react/react-native/actions/runs/36422135990) | android debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 12:29 | [36422135990](https://github.com/react/react-native/actions/runs/36422135990) | ios debug templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 12:29 | [36422135990](https://github.com/react/react-native/actions/runs/36422135990) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 10:53 | [36412375996](https://github.com/react/react-native/actions/runs/36412375996) | android release rntester | upstream | - | 51 | 49 | - | alert, animated-fade-in-view, appearance, button, filter-animated-blur, flatlist-append-maintainvisible, flatlist-complex-mutations-maintainvisible, flatlist-delete-anchor-maintainvisible, flatlist-delete-middle-maintainvisible, flatlist-empty-list-maintainvisible, flatlist-first-prepend-maintainvisible, flatlist-horizontal-add50-reset-maintainvisible, flatlist-horizontal-inverted-maintainvisible, flatlist-horizontal-inverted-recycle-maintainvisible, flatlist-horizontal-maintainvisible, flatlist-horizontal-recycle-maintainvisible, flatlist-inverted-maintainvisible, flatlist-inverted-recycle-maintainvisible, flatlist-maintainvisible, flatlist-momentum-scroll-maintainvisible, flatlist-orientation-maintainvisible, flatlist-prepend-delete-maintainvisible, flatlist-pull-to-refresh-maintainvisible, flatlist-rapid-prepends-maintainvisible, flatlist-recycle-maintainvisible, flatlist-scrolltooffset-maintainvisible, flatlist-throttle-maintainvisible, flatlist-variable-height-first-prepend-maintainvisible, flatlist-variable-height-maintainvisible, flatlist-viewability, flatlist, launch-app-and-search, search, image-blur-prefetch, image-getsize-local-drawables, image-progressive-jpeg, image-wide-gamut, image, legacy-native-module, modal, new-arch-examples, pressable, scrollview-minindex-maintainvisible, scrollview-threshold-maintainvisible, sectionlist-viewability, text-width-mode, text, textinput-uncontrolled, touchable | 98 | 2 |
| 2026-09-28 10:53 | [36412375996](https://github.com/react/react-native/actions/runs/36412375996) | android debug rntester | upstream | - | 27 | 25 | - | alert, animated-fade-in-view, appearance, button, filter-animated-blur, flatlist-viewability, flatlist, launch-app-and-search, search, image-blur-prefetch, image-getsize-local-drawables, image-progressive-jpeg, image-wide-gamut, image, legacy-native-module, modal, new-arch-examples, pressable, scrollview-minindex-maintainvisible, scrollview-threshold-maintainvisible, sectionlist-viewability, text-width-mode, text, textinput-uncontrolled, touchable | 50 | 2 |
| 2026-09-28 10:53 | [36412375996](https://github.com/react/react-native/actions/runs/36412375996) | android debug templateapp | upstream | - | 1 | 1 | - | start | 2 | 2 |
| 2026-09-28 10:53 | [36412375996](https://github.com/react/react-native/actions/runs/36412375996) | android release templateapp | upstream | - | 1 | 1 | - | start | 2 | 2 |
| 2026-09-28 10:53 | [36412375996](https://github.com/react/react-native/actions/runs/36412375996) | ios debug rntester | upstream | - | 48 | 3 | fabric-interop-add-children (1), scrollview-minindex-maintainvisible (1), sectionlist-viewability (6) | - | 99 | 2 |
| 2026-09-28 10:53 | [36412375996](https://github.com/react/react-native/actions/runs/36412375996) | ios release rntester | upstream | - | 48 | 1 | sectionlist-viewability (5) | - | 96 | 2 |
| 2026-09-28 10:53 | [36412375996](https://github.com/react/react-native/actions/runs/36412375996) | ios debug templateapp | upstream | - | 1 | 1 | start (1) | - | 1 | 0 |
| 2026-09-28 10:53 | [36412375996](https://github.com/react/react-native/actions/runs/36412375996) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
| 2026-09-28 09:52 | [36406213503](https://github.com/react/react-native/actions/runs/36406213503) | android debug rntester | upstream | - | 27 | 25 | - | alert, animated-fade-in-view, appearance, button, filter-animated-blur, flatlist-viewability, flatlist, launch-app-and-search, search, image-blur-prefetch, image-getsize-local-drawables, image-progressive-jpeg, image-wide-gamut, image, legacy-native-module, modal, new-arch-examples, pressable, scrollview-minindex-maintainvisible, scrollview-threshold-maintainvisible, sectionlist-viewability, text-width-mode, text, textinput-uncontrolled, touchable | 50 | 2 |
| 2026-09-28 09:52 | [36406213503](https://github.com/react/react-native/actions/runs/36406213503) | android release rntester | upstream | - | 51 | 49 | - | alert, animated-fade-in-view, appearance, button, filter-animated-blur, flatlist-append-maintainvisible, flatlist-complex-mutations-maintainvisible, flatlist-delete-anchor-maintainvisible, flatlist-delete-middle-maintainvisible, flatlist-empty-list-maintainvisible, flatlist-first-prepend-maintainvisible, flatlist-horizontal-add50-reset-maintainvisible, flatlist-horizontal-inverted-maintainvisible, flatlist-horizontal-inverted-recycle-maintainvisible, flatlist-horizontal-maintainvisible, flatlist-horizontal-recycle-maintainvisible, flatlist-inverted-maintainvisible, flatlist-inverted-recycle-maintainvisible, flatlist-maintainvisible, flatlist-momentum-scroll-maintainvisible, flatlist-orientation-maintainvisible, flatlist-prepend-delete-maintainvisible, flatlist-pull-to-refresh-maintainvisible, flatlist-rapid-prepends-maintainvisible, flatlist-recycle-maintainvisible, flatlist-scrolltooffset-maintainvisible, flatlist-throttle-maintainvisible, flatlist-variable-height-first-prepend-maintainvisible, flatlist-variable-height-maintainvisible, flatlist-viewability, flatlist, launch-app-and-search, search, image-blur-prefetch, image-getsize-local-drawables, image-progressive-jpeg, image-wide-gamut, image, legacy-native-module, modal, new-arch-examples, pressable, scrollview-minindex-maintainvisible, scrollview-threshold-maintainvisible, sectionlist-viewability, text-width-mode, text, textinput-uncontrolled, touchable | 98 | 2 |
| 2026-09-28 09:52 | [36406213503](https://github.com/react/react-native/actions/runs/36406213503) | android debug templateapp | upstream | - | 1 | 1 | - | start | 2 | 2 |
| 2026-09-28 09:52 | [36406213503](https://github.com/react/react-native/actions/runs/36406213503) | android release templateapp | upstream | - | 1 | 1 | - | start | 2 | 2 |
| 2026-09-28 09:52 | [36406213503](https://github.com/react/react-native/actions/runs/36406213503) | ios release rntester | upstream | - | 48 | 1 | sectionlist-viewability (5) | - | 48 | 1 |
| 2026-09-28 09:52 | [36406213503](https://github.com/react/react-native/actions/runs/36406213503) | ios debug rntester | upstream | - | 48 | 1 | alert (1) | - | 49 | 1 |
| 2026-09-28 09:52 | [36406213503](https://github.com/react/react-native/actions/runs/36406213503) | ios debug templateapp | upstream | - | 1 | 1 | start (1) | - | 1 | 0 |
| 2026-09-28 09:52 | [36406213503](https://github.com/react/react-native/actions/runs/36406213503) | ios release templateapp | upstream | - | 1 | 0 | - | - | 0 | 0 |
