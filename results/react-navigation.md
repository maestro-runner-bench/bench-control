# react-navigation

Upstream runs agent-device.

Times in minutes. *Run* is the whole workflow run (builds included); *job* is one job; *tests* is its test step only; *queue* is the wait for a runner.

## Summary

| Project | Platform | Flavour | Side | Build | Runs | Median e2e (min) | Green runs | Runs with no first-attempt failure | First-attempt failures / run | Final failures / run | Runs needing a retry job | Runner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| react-navigation | android | - | ours | 6904d0f | 5 | 25.8 | 5/5 | 5/5 | 0.00 | 0.00 | 0/5 | ubuntu-latest |
| react-navigation | android | - | ours | older | 3 | 26.6 | 2/2 | 2/2 | 0.00 | 0.00 | 0/3 | ubuntu-latest |
| react-navigation | android | - | ours | d51beed | 2 | - | 0/2 | 1/1 | 0.00 | 0.00 | 0/2 | ubuntu-latest |
| react-navigation | android | - | upstream | - | 47 | 23.9 | 38/47 | 27/47 | 0.60 | 0.21 | 0/47 | ubuntu-latest |
| react-navigation | ios | - | ours | 6904d0f | 5 | 18.4 | 5/5 | 4/5 | 0.20 | 0.00 | 0/5 | macos-latest |
| react-navigation | ios | - | ours | older | 3 | 21.2 | 3/3 | 2/3 | 0.33 | 0.00 | 0/3 | macos-latest |
| react-navigation | ios | - | upstream | - | 31 | 24.8 | 23/31 | 14/31 | 0.68 | 0.26 | 0/31 | macos-latest |

## Runs: maestro-runner (bench fork)

| Started (UTC) | Run | Build | Run time | Job | Job time | Tests | Queue | Result |
|---|---|---|---|---|---|---|---|---|
| 2026-10-03 18:39 | [37145037017](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37145037017) | 6904d0f | 30.1 | e2e-android | 29.4 | 26.6 | 0.0 | 39/39 |
| 2026-10-03 18:39 | [37145035430](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37145035430) | 6904d0f | 24.2 | e2e-ios | 22.6 | 18.4 | 0.1 | 39/39 |
| 2026-10-03 14:53 | [37131251179](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37131251179) | 6904d0f | 26.9 | e2e-android | 26.1 | 23.0 | 0.0 | 39/39 |
| 2026-10-03 14:53 | [37131249734](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37131249734) | 6904d0f | 13.0 | e2e-ios | 11.7 | 10.3 | 0.1 | 39/39 |
| 2026-10-03 10:22 | [37116220893](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37116220893) | 6904d0f | 30.0 | e2e-android | 29.4 | 26.6 | 0.0 | 39/39 |
| 2026-10-03 10:22 | [37116219437](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37116219437) | 6904d0f | 17.2 | e2e-ios | 15.8 | 12.2 | 0.1 | 39/39 |
| 2026-10-02 23:31 | [37078011839](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37078011839) | 6904d0f | 29.4 | e2e-android | 28.7 | 25.8 | 0.0 | 39/39 |
| 2026-10-02 23:31 | [37078009816](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37078009816) | 6904d0f | 52.9 | e2e-ios | 24.6 | 19.1 | 17.1 | 39/39, 1 passed on retry |
| 2026-10-02 20:05 | [37058311092](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37058311092) | 6904d0f | 36.5 | e2e-android | 26.1 | 23.0 | 0.0 | 39/39 |
| 2026-10-02 20:05 | [37058306195](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37058306195) | 6904d0f | 45.0 | e2e-ios | 26.8 | 19.5 | 0.1 | 39/39 |
| 2026-10-02 09:02 | [36987509817](https://github.com/maestro-runner-bench/react-navigation/actions/runs/36987509817) | maestro-runner 1.1.28.1 | 30.4 | e2e-android | 29.7 | 26.9 | 0.1 | 39/39 |
| 2026-10-02 09:02 | [36987506264](https://github.com/maestro-runner-bench/react-navigation/actions/runs/36987506264) | maestro-runner 1.1.28.1 | 30.4 | e2e-ios | 29.0 | 21.2 | 0.1 | 39/39, 1 passed on retry |
| 2026-10-01 19:51 | [36917328670](https://github.com/maestro-runner-bench/react-navigation/actions/runs/36917328670) | maestro-runner 1.1.28.1 | 37.5 | e2e-ios | 26.9 | 19.3 | 6.4 | 39/39 |
| 2026-10-01 19:51 | [36917324532](https://github.com/maestro-runner-bench/react-navigation/actions/runs/36917324532) | maestro-runner 1.1.28.1 | 30.9 | e2e-android | 29.2 | 26.3 | 0.0 | 39/39 |
| 2026-10-01 19:49 | [36917171417](https://github.com/maestro-runner-bench/react-navigation/actions/runs/36917171417) | - | 2.2 | e2e-android | 1.6 | - | 0.0 | cancelled before tests |
| 2026-10-01 16:47 | [36894629274](https://github.com/maestro-runner-bench/react-navigation/actions/runs/36894629274) | maestro-runner 1.1.28 | 61.3 | e2e-ios | 31.4 | 23.9 | 0.1 | 39/39 |
| 2026-10-01 15:42 | [36886332223](https://github.com/maestro-runner-bench/react-navigation/actions/runs/36886332223) | d51beed | 8.6 | e2e-android | 7.8 | 4.5 | 0.1 | cancelled during tests (time limit or by hand) |
| 2026-10-01 15:08 | [36881943539](https://github.com/maestro-runner-bench/react-navigation/actions/runs/36881943539) | d51beed | 32.7 | e2e-android | 19.1 | 16.3 | 0.1 | cancelled during tests (time limit or by hand) |

## Runs: upstream

| Started (UTC) | Run | Build | Run time | Job | Job time | Tests | Queue | Result |
|---|---|---|---|---|---|---|---|---|
| 2026-10-03 04:12 | [37095785622](https://github.com/react-navigation/react-navigation/actions/runs/37095785622) | agent-device | 36.6 | e2e-android | 26.9 | 24.2 | 0.4 | 39/39 |
| 2026-10-03 04:10 | [37095648277](https://github.com/react-navigation/react-navigation/actions/runs/37095648277) | agent-device | 57.0 | e2e-ios | 38.1 | 28.4 | 0.1 | 39/39, 1 passed on retry |
| 2026-10-02 16:24 | [37033699295](https://github.com/react-navigation/react-navigation/actions/runs/37033699295) | agent-device | 37.1 | e2e-android | 27.4 | 24.6 | 0.0 | 39/39 |
| 2026-10-02 16:24 | [37033699381](https://github.com/react-navigation/react-navigation/actions/runs/37033699381) | agent-device | 56.6 | e2e-ios | 37.3 | 29.5 | 0.1 | 39/39, 1 passed on retry |
| 2026-10-02 15:20 | [37026224479](https://github.com/react-navigation/react-navigation/actions/runs/37026224479) | agent-device | 35.2 | e2e-android | 25.7 | 22.5 | 0.1 | 39/39 |
| 2026-10-02 15:20 | [37026224342](https://github.com/react-navigation/react-navigation/actions/runs/37026224342) | agent-device | 42.4 | e2e-ios | 34.6 | 26.6 | 0.2 | 39/39 |
| 2026-10-02 04:07 | [36963190410](https://github.com/react-navigation/react-navigation/actions/runs/36963190410) | agent-device | 38.5 | e2e-android | 29.0 | 25.9 | 0.1 | 39/39 |
| 2026-10-02 04:05 | [36962985542](https://github.com/react-navigation/react-navigation/actions/runs/36962985542) | agent-device | 52.0 | e2e-ios | 33.8 | 24.8 | 0.1 | 39/39 |
| 2026-10-01 04:08 | [36813742119](https://github.com/react-navigation/react-navigation/actions/runs/36813742119) | agent-device | 38.5 | e2e-android | 28.6 | 25.6 | 0.1 | 39/39 |
| 2026-10-01 04:05 | [36813516059](https://github.com/react-navigation/react-navigation/actions/runs/36813516059) | agent-device | 53.4 | e2e-ios | 34.3 | 27.9 | 0.1 | 39/39, 1 passed on retry |
| 2026-09-30 04:08 | [36667502029](https://github.com/react-navigation/react-navigation/actions/runs/36667502029) | agent-device | 32.0 | e2e-android | 23.3 | 20.3 | 0.0 | 39/39 |
| 2026-09-30 04:05 | [36667287071](https://github.com/react-navigation/react-navigation/actions/runs/36667287071) | agent-device | 43.0 | e2e-ios | 28.3 | 22.7 | 0.1 | 39/39, 1 passed on retry |
| 2026-09-29 17:01 | [36601956215](https://github.com/react-navigation/react-navigation/actions/runs/36601956215) | agent-device | 28.6 | e2e-android | 20.4 | 17.4 | 0.0 | 39/39 |
| 2026-09-29 17:01 | [36601955925](https://github.com/react-navigation/react-navigation/actions/runs/36601955925) | agent-device | 51.6 | e2e-ios | 36.9 | 29.1 | 0.1 | 39/39, 1 passed on retry |
| 2026-09-29 04:08 | [36520250143](https://github.com/react-navigation/react-navigation/actions/runs/36520250143) | agent-device | 39.4 | e2e-android | 27.6 | 24.6 | 0.1 | 39/39 |
| 2026-09-29 04:05 | [36520017465](https://github.com/react-navigation/react-navigation/actions/runs/36520017465) | agent-device | 26.5 | e2e-ios | 18.4 | 14.9 | 0.1 | 39/39 |
| 2026-09-28 14:53 | [36439386894](https://github.com/react-navigation/react-navigation/actions/runs/36439386894) | agent-device | 28.9 | e2e-android | 28.0 | 25.2 | 0.1 | 39/39 |
| 2026-09-28 14:53 | [36439386994](https://github.com/react-navigation/react-navigation/actions/runs/36439386994) | agent-device | 35.6 | e2e-ios | 34.3 | 27.0 | 0.2 | 39/39 |
| 2026-09-28 13:10 | [36426693656](https://github.com/react-navigation/react-navigation/actions/runs/36426693656) | agent-device | 43.9 | e2e-android | 30.9 | 28.1 | 0.1 | 38/39 |
| 2026-09-28 13:10 | [36426693853](https://github.com/react-navigation/react-navigation/actions/runs/36426693853) | agent-device | 45.5 | e2e-ios | 22.6 | 17.4 | 0.1 | 39/39, 1 passed on retry |
| 2026-09-28 10:08 | [36407924092](https://github.com/react-navigation/react-navigation/actions/runs/36407924092) | agent-device | 31.8 | e2e-android | 21.8 | 18.9 | 0.1 | 38/39 |
| 2026-09-28 10:08 | [36407924066](https://github.com/react-navigation/react-navigation/actions/runs/36407924066) | agent-device | 54.3 | e2e-ios | 37.2 | 26.4 | 0.1 | 38/39 |
| 2026-09-28 04:09 | [36376474939](https://github.com/react-navigation/react-navigation/actions/runs/36376474939) | agent-device | 26.8 | e2e-android | 26.1 | 22.9 | 0.1 | 38/39, 1 passed on retry |
| 2026-09-28 04:05 | [36376272202](https://github.com/react-navigation/react-navigation/actions/runs/36376272202) | agent-device | 36.1 | e2e-ios | 34.4 | 24.3 | 0.1 | 38/39 |
| 2026-09-27 04:07 | [36293397178](https://github.com/react-navigation/react-navigation/actions/runs/36293397178) | agent-device | 28.3 | e2e-android | 27.6 | 24.7 | 0.1 | 38/39 |
| 2026-09-27 04:04 | [36293266594](https://github.com/react-navigation/react-navigation/actions/runs/36293266594) | agent-device | 31.8 | e2e-ios | 30.4 | 22.4 | 0.2 | 38/39, 1 passed on retry |
| 2026-09-26 04:07 | [36216899586](https://github.com/react-navigation/react-navigation/actions/runs/36216899586) | agent-device | 40.2 | e2e-android | 30.9 | 27.4 | 0.0 | 37/39, 1 passed on retry |
| 2026-09-26 04:04 | [36216757877](https://github.com/react-navigation/react-navigation/actions/runs/36216757877) | agent-device | 45.1 | e2e-ios | 30.2 | 22.5 | 0.1 | 38/39 |
| 2026-09-25 04:07 | [36093183306](https://github.com/react-navigation/react-navigation/actions/runs/36093183306) | agent-device | 38.9 | e2e-android | 29.9 | 26.9 | 0.1 | 38/39, 2 passed on retry |
| 2026-09-25 04:05 | [36092975329](https://github.com/react-navigation/react-navigation/actions/runs/36092975329) | agent-device | 60.1 | e2e-ios | 36.1 | 25.4 | 0.1 | 38/39 |
| 2026-09-24 04:07 | [35954318172](https://github.com/react-navigation/react-navigation/actions/runs/35954318172) | agent-device | 29.4 | e2e-android | 28.7 | 25.6 | 0.0 | 38/39, 1 passed on retry |
| 2026-09-24 04:04 | [35954111092](https://github.com/react-navigation/react-navigation/actions/runs/35954111092) | agent-device | 36.8 | e2e-ios | 35.1 | 26.3 | 0.1 | 38/39, 2 passed on retry |
| 2026-09-23 04:08 | [35817094576](https://github.com/react-navigation/react-navigation/actions/runs/35817094576) | agent-device | 38.7 | e2e-android | 29.0 | 26.2 | 0.0 | 38/39, 1 passed on retry |
| 2026-09-23 04:05 | [35816881656](https://github.com/react-navigation/react-navigation/actions/runs/35816881656) | agent-device | 44.3 | e2e-ios | 24.4 | 18.3 | 0.1 | 38/39 |
| 2026-09-22 21:25 | [35786536418](https://github.com/react-navigation/react-navigation/actions/runs/35786536418) | agent-device | 34.7 | e2e-android | 25.0 | 22.2 | 0.1 | 38/39 |
| 2026-09-22 21:25 | [35786536434](https://github.com/react-navigation/react-navigation/actions/runs/35786536434) | agent-device | 67.2 | e2e-ios | 49.1 | 35.7 | 0.1 | 38/39, 1 passed on retry |
| 2026-09-22 04:07 | [35685684910](https://github.com/react-navigation/react-navigation/actions/runs/35685684910) | agent-device | 36.5 | e2e-android | 27.0 | 24.2 | 0.1 | 39/39 |
| 2026-09-22 04:04 | [35685504199](https://github.com/react-navigation/react-navigation/actions/runs/35685504199) | agent-device | 48.8 | e2e-ios | 34.1 | 24.8 | 0.1 | 39/39 |
| 2026-09-21 11:43 | [35595560203](https://github.com/react-navigation/react-navigation/actions/runs/35595560203) | agent-device | 20.2 | e2e-android | 19.6 | 16.6 | 0.1 | 39/39 |
| 2026-09-21 11:43 | [35595560250](https://github.com/react-navigation/react-navigation/actions/runs/35595560250) | agent-device | 35.6 | e2e-ios | 33.7 | 25.4 | 0.1 | 39/39 |
| 2026-09-21 04:08 | [35559883290](https://github.com/react-navigation/react-navigation/actions/runs/35559883290) | agent-device | 21.3 | e2e-android | 20.6 | 17.1 | 0.1 | 39/39 |
| 2026-09-21 04:05 | [35559706501](https://github.com/react-navigation/react-navigation/actions/runs/35559706501) | agent-device | 36.6 | e2e-ios | 35.1 | 25.2 | 0.1 | 39/39 |
| 2026-09-20 04:07 | [35488343748](https://github.com/react-navigation/react-navigation/actions/runs/35488343748) | agent-device | 35.4 | e2e-android | 26.3 | 23.5 | 0.1 | 39/39 |
| 2026-09-20 04:04 | [35488219184](https://github.com/react-navigation/react-navigation/actions/runs/35488219184) | agent-device | 45.3 | e2e-ios | 27.4 | 21.1 | 0.1 | 39/39 |
| 2026-09-19 10:42 | [35438146683](https://github.com/react-navigation/react-navigation/actions/runs/35438146683) | agent-device | 32.4 | e2e-android | 22.6 | 19.7 | 0.1 | 39/39 |
| 2026-09-19 10:42 | [35438146685](https://github.com/react-navigation/react-navigation/actions/runs/35438146685) | agent-device | 46.4 | e2e-ios | 25.2 | 19.9 | 0.1 | 39/39 |
| 2026-09-19 04:07 | [35420441248](https://github.com/react-navigation/react-navigation/actions/runs/35420441248) | agent-device | 35.7 | e2e-android | 26.6 | 23.9 | 0.0 | 39/39, 1 passed on retry |
| 2026-09-19 04:04 | [35420324255](https://github.com/react-navigation/react-navigation/actions/runs/35420324255) | agent-device | 39.0 | e2e-ios | 26.0 | 20.0 | 0.1 | 39/39 |
| 2026-09-18 23:42 | [35406733671](https://github.com/react-navigation/react-navigation/actions/runs/35406733671) | agent-device | 22.9 | e2e-android | 22.1 | 19.4 | 0.0 | 39/39 |
| 2026-09-18 23:42 | [35406733658](https://github.com/react-navigation/react-navigation/actions/runs/35406733658) | agent-device | 43.9 | e2e-ios | 42.4 | 31.8 | 0.1 | 39/39, 1 passed on retry |
| 2026-09-18 21:26 | [35396777244](https://github.com/react-navigation/react-navigation/actions/runs/35396777244) | agent-device | 33.9 | e2e-android | 25.1 | 21.6 | 0.1 | 39/39 |
| 2026-09-18 21:26 | [35396777245](https://github.com/react-navigation/react-navigation/actions/runs/35396777245) | agent-device | 51.6 | e2e-ios | 34.0 | 27.4 | 0.1 | 39/39 |
| 2026-09-18 20:41 | [35392819788](https://github.com/react-navigation/react-navigation/actions/runs/35392819788) | agent-device | 29.4 | e2e-ios | 27.6 | 21.1 | 0.1 | 39/39 |
| 2026-09-18 20:41 | [35392819880](https://github.com/react-navigation/react-navigation/actions/runs/35392819880) | agent-device | 29.2 | e2e-android | 27.2 | 24.3 | 0.1 | 39/39 |
| 2026-09-18 19:45 | [35387707183](https://github.com/react-navigation/react-navigation/actions/runs/35387707183) | agent-device | 27.1 | e2e-android | 26.2 | 23.4 | 0.1 | 39/39 |
| 2026-09-18 19:45 | [35387707067](https://github.com/react-navigation/react-navigation/actions/runs/35387707067) | agent-device | 30.2 | e2e-ios | 28.4 | 21.8 | 0.1 | 39/39 |
| 2026-09-18 04:07 | [35305768494](https://github.com/react-navigation/react-navigation/actions/runs/35305768494) | agent-device | 31.8 | e2e-android | 23.4 | 20.5 | 0.1 | 39/39, 1 passed on retry |
| 2026-09-18 04:04 | [35305580529](https://github.com/react-navigation/react-navigation/actions/runs/35305580529) | agent-device | 42.3 | e2e-ios | 28.3 | 21.2 | 0.2 | 39/39, 1 passed on retry |
| 2026-09-17 20:13 | [35269517751](https://github.com/react-navigation/react-navigation/actions/runs/35269517751) | agent-device | 27.9 | e2e-android | 27.3 | 24.3 | 0.1 | 39/39 |
| 2026-09-17 20:13 | [35269516996](https://github.com/react-navigation/react-navigation/actions/runs/35269516996) | agent-device | 27.5 | e2e-ios | 25.8 | 18.6 | 0.2 | 39/39, 1 passed on retry |
| 2026-09-17 19:01 | [35262357123](https://github.com/react-navigation/react-navigation/actions/runs/35262357123) | agent-device | - | e2e-ios | - | 24.5 | 0.1 | 39/39 |
| 2026-09-17 19:01 | [35262357256](https://github.com/react-navigation/react-navigation/actions/runs/35262357256) | agent-device | - | e2e-android | - | 25.1 | 0.1 | 39/39, 1 passed on retry |
| 2026-09-05 04:07 | [33943691205](https://github.com/react-navigation/react-navigation/actions/runs/33943691205) | agent-device | - | e2e-android | - | 27.9 | 0.1 | 39/39, 1 passed on retry |
| 2026-09-04 04:08 | [33835679643](https://github.com/react-navigation/react-navigation/actions/runs/33835679643) | agent-device | - | e2e-android | - | 24.2 | 0.1 | 39/39 |
| 2026-09-02 04:08 | [33589635197](https://github.com/react-navigation/react-navigation/actions/runs/33589635197) | agent-device | - | e2e-android | - | 23.9 | 0.1 | 39/39 |
| 2026-08-05 20:04 | [31042334082](https://github.com/react-navigation/react-navigation/actions/runs/31042334082) | agent-device | - | e2e-android | - | 23.4 | 0.2 | 39/39 |
| 2026-08-05 14:12 | [31013967027](https://github.com/react-navigation/react-navigation/actions/runs/31013967027) | agent-device | - | e2e-android | - | 23.2 | 0.1 | 39/39 |
| 2026-08-05 05:02 | [30976894497](https://github.com/react-navigation/react-navigation/actions/runs/30976894497) | agent-device | - | e2e-android | - | 27.8 | 0.1 | 39/39, 1 passed on retry |
| 2026-08-04 05:02 | [30879450590](https://github.com/react-navigation/react-navigation/actions/runs/30879450590) | agent-device | - | e2e-android | - | 19.6 | 0.1 | 39/39 |
| 2026-08-04 00:46 | [30866636153](https://github.com/react-navigation/react-navigation/actions/runs/30866636153) | agent-device | - | e2e-android | - | 23.0 | 0.1 | 39/39 |
| 2026-08-03 16:28 | [30832352180](https://github.com/react-navigation/react-navigation/actions/runs/30832352180) | agent-device | - | e2e-android | - | 23.0 | 0.1 | 39/39 |
| 2026-08-03 11:02 | [30807945335](https://github.com/react-navigation/react-navigation/actions/runs/30807945335) | agent-device | - | e2e-android | - | 24.1 | 0.1 | 39/39, 2 passed on retry |
| 2026-08-03 05:12 | [30786478984](https://github.com/react-navigation/react-navigation/actions/runs/30786478984) | agent-device | - | e2e-android | - | 23.1 | 0.1 | 39/39, 1 passed on retry |
| 2026-08-02 17:23 | [30758758104](https://github.com/react-navigation/react-navigation/actions/runs/30758758104) | agent-device | - | e2e-android | - | 23.5 | 0.1 | 39/39, 1 passed on retry |
| 2026-08-02 05:03 | [30733450711](https://github.com/react-navigation/react-navigation/actions/runs/30733450711) | agent-device | - | e2e-android | - | 23.4 | 0.1 | 39/39, 1 passed on retry |
| 2026-08-01 05:04 | [30685120778](https://github.com/react-navigation/react-navigation/actions/runs/30685120778) | agent-device | - | e2e-android | - | 23.2 | 0.1 | 39/39 |
| 2026-07-31 21:37 | [30667229447](https://github.com/react-navigation/react-navigation/actions/runs/30667229447) | agent-device | - | e2e-android | - | 24.9 | 0.1 | 39/39, 1 passed on retry |
| 2026-07-31 05:09 | [30606027234](https://github.com/react-navigation/react-navigation/actions/runs/30606027234) | agent-device | - | e2e-android | - | 26.6 | 0.1 | 39/39, 1 passed on retry |

## Trend

![react-navigation-android](charts/react-navigation-android.svg)

![react-navigation-ios](charts/react-navigation-ios.svg)


## Retried test cases

Per run, from each job's log: a flow *failed at least once* if any of its attempts failed, inside its job (maestro-runner `--retries`, React Native's iOS per-flow attempts, agent-device, Expo's rounds) or in a retry job (React Native's retry_1/retry_2); it *passed on retry* if it then passed. *Extra flow runs* counts every run of a flow beyond its first, including whole-suite reruns of flows that had passed. Runs whose logs had expired are left out.

Each cell: **ours vs upstream**; the better one in bold. Ours is the newest maestro-runner build.

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing (ours / upstream) |
|---|---|---|---|---|---|---|---|---|---|
| android | 6904d0f | 5 vs 47 | 25.8 vs **23.9** | **100%** vs 66% | **0.00** vs 0.38 | 0% vs 0% | **0.0** vs 0.4 | 0% vs 0% | - / Tab View - Scrollable Tab Bar ×7, Bottom Tabs - Preload Flow ×5, Screen Layout ×2 |
| ios | 6904d0f | 5 vs 31 | **18.4** vs 24.8 | **80%** vs 61% | **0.20** vs 0.42 | 0% vs 0% | **0.2** vs 0.5 | 0% vs 0% | Material Top Tabs - Basic ×1 / Screen Layout ×3, Tab View - Scrollable Tab Bar ×3, Stack - Prevent Remove ×2 |

Ours on earlier maestro-runner builds:

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing |
|---|---|---|---|---|---|---|---|---|---|
| android | older | 2 | 26.6 | 100% | 0.00 | 0% | 0.0 | 0% | - |
| android | d51beed | 2 | 10.4 | 100% | 0.00 | 0% | 0.0 | 0% | - |
| ios | older | 3 | 21.2 | 67% | 0.33 | 0% | 0.3 | 0% | Screen Layout ×1 |

### Per run

| Started (UTC) | Run | Platform | Side | Build | Flows | Failed at least once | Passed on retry (failed attempts) | Failed at the end | Extra flow runs | Retry jobs |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-03 18:39 | [37145037017](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37145037017) | android | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-03 18:39 | [37145035430](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37145035430) | ios | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-03 14:53 | [37131251179](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37131251179) | android | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-03 14:53 | [37131249734](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37131249734) | ios | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-03 10:22 | [37116220893](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37116220893) | android | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-03 10:22 | [37116219437](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37116219437) | ios | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-03 04:12 | [37095785622](https://github.com/react-navigation/react-navigation/actions/runs/37095785622) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-10-03 04:10 | [37095648277](https://github.com/react-navigation/react-navigation/actions/runs/37095648277) | ios | upstream | - | 39 | 1 | Screen Layout (1) | - | 1 | 0 |
| 2026-10-02 23:31 | [37078011839](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37078011839) | android | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-02 23:31 | [37078009816](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37078009816) | ios | ours | 6904d0f | 39 | 1 | Material Top Tabs - Basic (1) | - | 1 | 0 |
| 2026-10-02 20:05 | [37058311092](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37058311092) | android | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-02 20:05 | [37058306195](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37058306195) | ios | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-02 16:24 | [37033699295](https://github.com/react-navigation/react-navigation/actions/runs/37033699295) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-10-02 16:24 | [37033699381](https://github.com/react-navigation/react-navigation/actions/runs/37033699381) | ios | upstream | - | 39 | 1 | Loaders (1) | - | 1 | 0 |
| 2026-10-02 15:20 | [37026224479](https://github.com/react-navigation/react-navigation/actions/runs/37026224479) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-10-02 15:20 | [37026224342](https://github.com/react-navigation/react-navigation/actions/runs/37026224342) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-10-02 09:02 | [36987509817](https://github.com/maestro-runner-bench/react-navigation/actions/runs/36987509817) | android | ours | - | 39 | 0 | - | - | 0 | 0 |
| 2026-10-02 09:02 | [36987506264](https://github.com/maestro-runner-bench/react-navigation/actions/runs/36987506264) | ios | ours | - | 39 | 1 | Screen Layout (1) | - | 1 | 0 |
| 2026-10-02 04:07 | [36963190410](https://github.com/react-navigation/react-navigation/actions/runs/36963190410) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-10-02 04:05 | [36962985542](https://github.com/react-navigation/react-navigation/actions/runs/36962985542) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-10-01 19:51 | [36917328670](https://github.com/maestro-runner-bench/react-navigation/actions/runs/36917328670) | ios | ours | - | 39 | 0 | - | - | 0 | 0 |
| 2026-10-01 19:51 | [36917324532](https://github.com/maestro-runner-bench/react-navigation/actions/runs/36917324532) | android | ours | - | 39 | 0 | - | - | 0 | 0 |
| 2026-10-01 16:47 | [36894629274](https://github.com/maestro-runner-bench/react-navigation/actions/runs/36894629274) | ios | ours | - | 39 | 0 | - | - | 0 | 0 |
| 2026-10-01 15:42 | [36886332223](https://github.com/maestro-runner-bench/react-navigation/actions/runs/36886332223) | android | ours | d51beed | 5 | 0 | - | - | 0 | 0 |
| 2026-10-01 15:08 | [36881943539](https://github.com/maestro-runner-bench/react-navigation/actions/runs/36881943539) | android | ours | d51beed | 16 | 0 | - | - | 0 | 0 |
| 2026-10-01 04:08 | [36813742119](https://github.com/react-navigation/react-navigation/actions/runs/36813742119) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-10-01 04:05 | [36813516059](https://github.com/react-navigation/react-navigation/actions/runs/36813516059) | ios | upstream | - | 39 | 1 | Screen Layout (2) | - | 2 | 0 |
| 2026-09-30 04:08 | [36667502029](https://github.com/react-navigation/react-navigation/actions/runs/36667502029) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-30 04:05 | [36667287071](https://github.com/react-navigation/react-navigation/actions/runs/36667287071) | ios | upstream | - | 39 | 1 | Tab View - Scrollable Tab Bar (1) | - | 1 | 0 |
| 2026-09-29 17:01 | [36601956215](https://github.com/react-navigation/react-navigation/actions/runs/36601956215) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-29 17:01 | [36601955925](https://github.com/react-navigation/react-navigation/actions/runs/36601955925) | ios | upstream | - | 39 | 1 | Screen Layout (1) | - | 1 | 0 |
| 2026-09-29 04:08 | [36520250143](https://github.com/react-navigation/react-navigation/actions/runs/36520250143) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-29 04:05 | [36520017465](https://github.com/react-navigation/react-navigation/actions/runs/36520017465) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-28 14:53 | [36439386894](https://github.com/react-navigation/react-navigation/actions/runs/36439386894) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-28 14:53 | [36439386994](https://github.com/react-navigation/react-navigation/actions/runs/36439386994) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-28 13:10 | [36426693656](https://github.com/react-navigation/react-navigation/actions/runs/36426693656) | android | upstream | - | 38 | 0 | - | - | 0 | 0 |
| 2026-09-28 13:10 | [36426693853](https://github.com/react-navigation/react-navigation/actions/runs/36426693853) | ios | upstream | - | 39 | 1 | Tab View - Scrollable Tab Bar (1) | - | 1 | 0 |
| 2026-09-28 10:08 | [36407924092](https://github.com/react-navigation/react-navigation/actions/runs/36407924092) | android | upstream | - | 38 | 0 | - | - | 0 | 0 |
| 2026-09-28 10:08 | [36407924066](https://github.com/react-navigation/react-navigation/actions/runs/36407924066) | ios | upstream | - | 38 | 0 | - | - | 0 | 0 |
| 2026-09-28 04:09 | [36376474939](https://github.com/react-navigation/react-navigation/actions/runs/36376474939) | android | upstream | - | 38 | 1 | Tab View - Scrollable Tab Bar (2) | - | 2 | 0 |
| 2026-09-28 04:05 | [36376272202](https://github.com/react-navigation/react-navigation/actions/runs/36376272202) | ios | upstream | - | 38 | 0 | - | - | 0 | 0 |
| 2026-09-27 04:07 | [36293397178](https://github.com/react-navigation/react-navigation/actions/runs/36293397178) | android | upstream | - | 38 | 0 | - | - | 0 | 0 |
| 2026-09-27 04:04 | [36293266594](https://github.com/react-navigation/react-navigation/actions/runs/36293266594) | ios | upstream | - | 38 | 1 | Native Stack - Prevent Remove (1) | - | 1 | 0 |
| 2026-09-26 04:07 | [36216899586](https://github.com/react-navigation/react-navigation/actions/runs/36216899586) | android | upstream | - | 37 | 1 | Tab View - Scrollable Tab Bar (1) | - | 1 | 0 |
| 2026-09-26 04:04 | [36216757877](https://github.com/react-navigation/react-navigation/actions/runs/36216757877) | ios | upstream | - | 38 | 0 | - | - | 0 | 0 |
| 2026-09-25 04:07 | [36093183306](https://github.com/react-navigation/react-navigation/actions/runs/36093183306) | android | upstream | - | 38 | 2 | Tab View - Scrollable Tab Bar (2), Bottom Tabs - Preload Flow (1) | - | 3 | 0 |
| 2026-09-25 04:05 | [36092975329](https://github.com/react-navigation/react-navigation/actions/runs/36092975329) | ios | upstream | - | 38 | 0 | - | - | 0 | 0 |
| 2026-09-24 04:07 | [35954318172](https://github.com/react-navigation/react-navigation/actions/runs/35954318172) | android | upstream | - | 38 | 1 | Tab View - Scrollable Tab Bar (1) | - | 1 | 0 |
| 2026-09-24 04:04 | [35954111092](https://github.com/react-navigation/react-navigation/actions/runs/35954111092) | ios | upstream | - | 38 | 2 | Tab View - Scrollable Tab Bar (1), Showcase - Drawer (1) | - | 2 | 0 |
| 2026-09-23 04:08 | [35817094576](https://github.com/react-navigation/react-navigation/actions/runs/35817094576) | android | upstream | - | 38 | 1 | Tab View - Scrollable Tab Bar (1) | - | 1 | 0 |
| 2026-09-23 04:05 | [35816881656](https://github.com/react-navigation/react-navigation/actions/runs/35816881656) | ios | upstream | - | 38 | 0 | - | - | 0 | 0 |
| 2026-09-22 21:25 | [35786536418](https://github.com/react-navigation/react-navigation/actions/runs/35786536418) | android | upstream | - | 38 | 0 | - | - | 0 | 0 |
| 2026-09-22 21:25 | [35786536434](https://github.com/react-navigation/react-navigation/actions/runs/35786536434) | ios | upstream | - | 38 | 1 | Stack - Retain (1) | - | 1 | 0 |
| 2026-09-22 04:07 | [35685684910](https://github.com/react-navigation/react-navigation/actions/runs/35685684910) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-22 04:04 | [35685504199](https://github.com/react-navigation/react-navigation/actions/runs/35685504199) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-21 11:43 | [35595560203](https://github.com/react-navigation/react-navigation/actions/runs/35595560203) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-21 11:43 | [35595560250](https://github.com/react-navigation/react-navigation/actions/runs/35595560250) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-21 04:08 | [35559883290](https://github.com/react-navigation/react-navigation/actions/runs/35559883290) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-21 04:05 | [35559706501](https://github.com/react-navigation/react-navigation/actions/runs/35559706501) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-20 04:07 | [35488343748](https://github.com/react-navigation/react-navigation/actions/runs/35488343748) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-20 04:04 | [35488219184](https://github.com/react-navigation/react-navigation/actions/runs/35488219184) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-19 10:42 | [35438146683](https://github.com/react-navigation/react-navigation/actions/runs/35438146683) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-19 10:42 | [35438146685](https://github.com/react-navigation/react-navigation/actions/runs/35438146685) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-19 04:07 | [35420441248](https://github.com/react-navigation/react-navigation/actions/runs/35420441248) | android | upstream | - | 39 | 1 | Bottom Tabs - Preload Flow (1) | - | 1 | 0 |
| 2026-09-19 04:04 | [35420324255](https://github.com/react-navigation/react-navigation/actions/runs/35420324255) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-18 23:42 | [35406733671](https://github.com/react-navigation/react-navigation/actions/runs/35406733671) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-18 23:42 | [35406733658](https://github.com/react-navigation/react-navigation/actions/runs/35406733658) | ios | upstream | - | 39 | 1 | Stack - Prevent Remove (2) | - | 2 | 0 |
| 2026-09-18 21:26 | [35396777244](https://github.com/react-navigation/react-navigation/actions/runs/35396777244) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-18 21:26 | [35396777245](https://github.com/react-navigation/react-navigation/actions/runs/35396777245) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-18 20:41 | [35392819788](https://github.com/react-navigation/react-navigation/actions/runs/35392819788) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-18 20:41 | [35392819880](https://github.com/react-navigation/react-navigation/actions/runs/35392819880) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-18 19:45 | [35387707183](https://github.com/react-navigation/react-navigation/actions/runs/35387707183) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-18 19:45 | [35387707067](https://github.com/react-navigation/react-navigation/actions/runs/35387707067) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-18 04:07 | [35305768494](https://github.com/react-navigation/react-navigation/actions/runs/35305768494) | android | upstream | - | 39 | 1 | Showcase - Native Stack (1) | - | 1 | 0 |
| 2026-09-18 04:04 | [35305580529](https://github.com/react-navigation/react-navigation/actions/runs/35305580529) | ios | upstream | - | 39 | 1 | Native Stack - Card + Modal (1) | - | 1 | 0 |
| 2026-09-17 20:13 | [35269517751](https://github.com/react-navigation/react-navigation/actions/runs/35269517751) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-17 20:13 | [35269516996](https://github.com/react-navigation/react-navigation/actions/runs/35269516996) | ios | upstream | - | 39 | 1 | Stack - Prevent Remove (1) | - | 1 | 0 |
| 2026-09-17 19:01 | [35262357123](https://github.com/react-navigation/react-navigation/actions/runs/35262357123) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-17 19:01 | [35262357256](https://github.com/react-navigation/react-navigation/actions/runs/35262357256) | android | upstream | - | 39 | 1 | Bottom Tabs - Preload Flow (1) | - | 1 | 0 |
| 2026-09-05 04:07 | [33943691205](https://github.com/react-navigation/react-navigation/actions/runs/33943691205) | android | upstream | - | 39 | 1 | Tab View - Scrollable Tab Bar (1) | - | 1 | 0 |
| 2026-09-04 04:08 | [33835679643](https://github.com/react-navigation/react-navigation/actions/runs/33835679643) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-02 04:08 | [33589635197](https://github.com/react-navigation/react-navigation/actions/runs/33589635197) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-08-05 20:04 | [31042334082](https://github.com/react-navigation/react-navigation/actions/runs/31042334082) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-08-05 14:12 | [31013967027](https://github.com/react-navigation/react-navigation/actions/runs/31013967027) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-08-05 05:02 | [30976894497](https://github.com/react-navigation/react-navigation/actions/runs/30976894497) | android | upstream | - | 39 | 1 | Screen Layout (1) | - | 1 | 0 |
| 2026-08-04 05:02 | [30879450590](https://github.com/react-navigation/react-navigation/actions/runs/30879450590) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-08-04 00:46 | [30866636153](https://github.com/react-navigation/react-navigation/actions/runs/30866636153) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-08-03 16:28 | [30832352180](https://github.com/react-navigation/react-navigation/actions/runs/30832352180) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-08-03 11:02 | [30807945335](https://github.com/react-navigation/react-navigation/actions/runs/30807945335) | android | upstream | - | 39 | 2 | Screen Layout (1), Bottom Tabs - Preload Flow (2) | - | 3 | 0 |
| 2026-08-03 05:12 | [30786478984](https://github.com/react-navigation/react-navigation/actions/runs/30786478984) | android | upstream | - | 39 | 1 | Native Stack - Card + Modal (1) | - | 1 | 0 |
| 2026-08-02 17:23 | [30758758104](https://github.com/react-navigation/react-navigation/actions/runs/30758758104) | android | upstream | - | 39 | 1 | Bottom Tabs - Preload Flow (1) | - | 1 | 0 |
| 2026-08-02 05:03 | [30733450711](https://github.com/react-navigation/react-navigation/actions/runs/30733450711) | android | upstream | - | 39 | 1 | Native Stack - Card + Modal (1) | - | 1 | 0 |
| 2026-08-01 05:04 | [30685120778](https://github.com/react-navigation/react-navigation/actions/runs/30685120778) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-07-31 21:37 | [30667229447](https://github.com/react-navigation/react-navigation/actions/runs/30667229447) | android | upstream | - | 39 | 1 | Stack - Prevent Remove (1) | - | 1 | 0 |
| 2026-07-31 05:09 | [30606027234](https://github.com/react-navigation/react-navigation/actions/runs/30606027234) | android | upstream | - | 39 | 1 | Tab View - Scrollable Tab Bar (1) | - | 1 | 0 |
