# Bench results

Generated 2026-10-03 14:08 UTC from 1056 e2e jobs.

Per project, platform and flavour: ours (maestro-runner) against upstream (Maestro, or agent-device for React Navigation); ours one line per maestro-runner build, newest first ("older" = before builds were recorded). Times are the e2e test step only (no builds, no queue). First-attempt failures count flows that failed at least once before passing or failing for good; job retry rounds are React Native's retry_1/retry_2 jobs.

| Project | Platform | Flavour | Side | Build | Runs | Median e2e (min) | Green runs | Runs with no first-attempt failure | First-attempt failures / run | Final failures / run | Runs needing a retry job | Runner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| enriched-html | android | - | ours | 6904d0f | 4 | 27.2 | 0/4 | 0/4 | 8.50 | 7.50 | 0/4 | ubuntu-latest |
| enriched-html | android | - | ours | 49360bb | 1 | 26.4 | 0/1 | 0/1 | 42.00 | 42.00 | 0/1 | ubuntu-latest |
| enriched-html | android | - | ours | older | 4 | 23.9 | 0/4 | 0/3 | 29.00 | 28.33 | 0/4 | ubuntu-latest |
| enriched-html | ios | - | ours | 6904d0f | 4 | 34.1 | 0/4 | 0/4 | 4.50 | 2.50 | 0/4 | macos-26 |
| enriched-html | ios | - | ours | 49360bb | 1 | 31.0 | 0/1 | 0/1 | 5.00 | 3.00 | 0/1 | macos-26 |
| enriched-html | ios | - | ours | older | 4 | 33.5 | 0/3 | 0/3 | 18.67 | 17.33 | 0/4 | macos-26 |
| expo | android | - | ours | 6904d0f | 3 | 13.8 | 3/3 | 0/3 | 1.33 | 0.33 | 0/3 | ubuntu-24.04 |
| expo | android | - | ours | older | 4 | 27.9 | 1/4 | 0/4 | 4.50 | 3.75 | 0/4 | ubuntu-24.04 |
| expo | android | - | upstream | - | 48 | 14.5 | 42/48 | 21/48 | 1.21 | 0.10 | 0/48 | ubuntu-24.04 |
| expo | ios | - | ours | 6904d0f | 2 | 9.9 | 2/2 | 0/2 | 1.00 | 0.00 | 0/2 | macos-26 |
| expo | ios | - | ours | older | 4 | 11.4 | 1/4 | 1/4 | 1.75 | 1.50 | 0/4 | macos-26 |
| expo | ios | - | upstream | - | 45 | 16.1 | 34/45 | 25/45 | 0.76 | 0.04 | 0/45 | macos-26 |
| pager-view | android | - | ours | 6904d0f | 3 | 20.0 | 0/3 | 0/3 | 9.33 | 9.00 | 0/3 | ubuntu-latest |
| pager-view | android | - | ours | older | 1 | 0.3 | 0/1 | - | - | - | 0/1 | ubuntu-latest |
| pager-view | android | - | ours | 49360bb | 1 | 20.1 | 0/1 | 0/1 | 9.00 | 9.00 | 0/1 | ubuntu-latest |
| pager-view | ios | - | ours | 6904d0f | 4 | 8.2 | 0/4 | 0/4 | 4.00 | 4.00 | 0/4 | macos-26 |
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
| react-navigation | android | - | ours | 6904d0f | 3 | 25.8 | 3/3 | 3/3 | 0.00 | 0.00 | 0/3 | ubuntu-latest |
| react-navigation | android | - | ours | older | 3 | 26.6 | 2/2 | 2/2 | 0.00 | 0.00 | 0/3 | ubuntu-latest |
| react-navigation | android | - | ours | d51beed | 2 | - | 0/2 | 1/1 | 0.00 | 0.00 | 0/2 | ubuntu-latest |
| react-navigation | android | - | upstream | - | 47 | 23.9 | 38/47 | 27/47 | 0.60 | 0.21 | 0/47 | ubuntu-latest |
| react-navigation | ios | - | ours | 6904d0f | 3 | 19.1 | 3/3 | 2/3 | 0.33 | 0.00 | 0/3 | macos-latest |
| react-navigation | ios | - | ours | older | 3 | 21.2 | 3/3 | 2/3 | 0.33 | 0.00 | 0/3 | macos-latest |
| react-navigation | ios | - | upstream | - | 31 | 24.8 | 23/31 | 14/31 | 0.68 | 0.26 | 0/31 | macos-latest |

Upstream React Native runs its e2e jobs on larger runners (macos-*-large, 8-core-ubuntu); the bench fork uses the standard ones (macos-*-intel, ubuntu-latest).


## Per repo

- [enriched-html](enriched-html.md)
- [expo](expo.md)
- [pager-view](pager-view.md)
- [react-native](react-native.md)
- [react-navigation](react-navigation.md)

Retried test cases per run, all repos: [RETRIES.md](RETRIES.md)
