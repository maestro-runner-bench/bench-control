# react-navigation

Upstream runs agent-device.

Times in minutes. *Run* is the whole workflow run (builds included); *job* is one job; *tests* is its test step only; *queue* is the wait for a runner.

## Summary

| Project | Platform | Flavour | Side | Build | Runs | Median e2e (min) | Green runs | Runs with no first-attempt failure | First-attempt failures / run | Final failures / run | Runs needing a retry job | Runner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| react-navigation | android | - | ours | e8a87b5 | 20 | 25.4 | 20/20 | 18/20 | 0.10 | 0.00 | 0/20 | ubuntu-latest |
| react-navigation | android | - | ours | 6904d0f | 17 | 26.2 | 17/17 | 14/17 | 0.24 | 0.00 | 0/17 | ubuntu-latest |
| react-navigation | android | - | upstream | - | 54 | 23.9 | 45/54 | 34/54 | 0.52 | 0.19 | 0/54 | ubuntu-latest |
| react-navigation | ios | - | ours | e8a87b5 | 20 | 18.3 | 20/20 | 18/20 | 0.10 | 0.00 | 0/20 | macos-latest |
| react-navigation | ios | - | ours | older | 1 | 1.4 | 0/1 | - | - | - | 0/1 | macos-latest |
| react-navigation | ios | - | ours | 6904d0f | 17 | 19.0 | 17/17 | 14/17 | 0.18 | 0.00 | 0/17 | macos-latest |
| react-navigation | ios | - | upstream | - | 67 | 24.0 | 59/67 | 35/67 | 0.57 | 0.12 | 0/67 | macos-latest |

## Runs: maestro-runner (bench fork)

| Started (UTC) | Run | Build | Run time | Job | Job time | Tests | Queue | Result |
|---|---|---|---|---|---|---|---|---|
| 2026-10-07 21:57 | [37692975274](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37692975274) | e8a87b5 | 29.1 | e2e-android | 28.4 | 25.3 | 0.0 | 39/39 |
| 2026-10-07 21:57 | [37692972267](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37692972267) | e8a87b5 | 27.0 | e2e-ios | 25.5 | 18.9 | 0.1 | 39/39 |
| 2026-10-07 16:36 | [37653349409](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37653349409) | e8a87b5 | 30.8 | e2e-android | 29.9 | 26.8 | 0.1 | 39/39 |
| 2026-10-07 16:36 | [37653345106](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37653345106) | e8a87b5 | 30.5 | e2e-ios | 29.1 | 21.4 | 0.1 | 39/39 |
| 2026-10-07 11:20 | [37613392889](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37613392889) | e8a87b5 | 29.9 | e2e-android | 29.2 | 26.2 | 0.0 | 39/39 |
| 2026-10-07 11:20 | [37613389805](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37613389805) | e8a87b5 | 32.8 | e2e-ios | 26.0 | 19.6 | 0.2 | 39/39 |
| 2026-10-07 05:59 | [37579049256](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37579049256) | e8a87b5 | 22.9 | e2e-android | 22.2 | 19.5 | 0.0 | 39/39 |
| 2026-10-07 05:59 | [37579047010](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37579047010) | e8a87b5 | 18.0 | e2e-ios | 16.4 | 12.3 | 0.1 | 39/39 |
| 2026-10-07 03:29 | [37566964182](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37566964182) | e8a87b5 | 30.1 | e2e-android | 29.5 | 26.4 | 0.0 | 39/39 |
| 2026-10-07 03:29 | [37566962164](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37566962164) | e8a87b5 | 30.9 | e2e-ios | 29.6 | 19.7 | 0.1 | 39/39 |
| 2026-10-07 00:54 | [37554369088](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37554369088) | e8a87b5 | 26.7 | e2e-android | 25.9 | 22.5 | 0.0 | 39/39 |
| 2026-10-07 00:54 | [37554366542](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37554366542) | e8a87b5 | 20.4 | e2e-ios | 18.7 | 14.2 | 0.1 | 39/39 |
| 2026-10-06 22:29 | [37540927744](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37540927744) | e8a87b5 | 25.9 | e2e-android | 25.2 | 22.1 | 0.1 | 39/39 |
| 2026-10-06 22:29 | [37540924470](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37540924470) | e8a87b5 | 29.5 | e2e-ios | 27.9 | 20.9 | 0.1 | 39/39 |
| 2026-10-06 19:38 | [37520539021](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37520539021) | e8a87b5 | 31.8 | e2e-android | 30.9 | 27.7 | 0.1 | 39/39 |
| 2026-10-06 19:38 | [37520535200](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37520535200) | e8a87b5 | 24.5 | e2e-ios | 22.8 | 17.4 | 0.1 | 39/39 |
| 2026-10-06 16:47 | [37498469935](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37498469935) | e8a87b5 | 27.9 | e2e-android | 27.1 | 23.8 | 0.0 | 39/39 |
| 2026-10-06 16:47 | [37498465100](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37498465100) | e8a87b5 | 26.1 | e2e-ios | 24.4 | 18.1 | 0.1 | 39/39 |
| 2026-10-06 13:50 | [37473990531](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37473990531) | e8a87b5 | 38.1 | e2e-android | 29.6 | 26.7 | 0.1 | 39/39 |
| 2026-10-06 13:50 | [37473985583](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37473985583) | e8a87b5 | 42.5 | e2e-ios | 20.7 | 14.8 | 0.1 | 39/39, 1 passed on retry |
| 2026-10-06 10:59 | [37453432301](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37453432301) | e8a87b5 | 33.7 | e2e-android | 33.0 | 29.4 | 0.0 | 39/39, 1 passed on retry |
| 2026-10-06 10:59 | [37453428830](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37453428830) | e8a87b5 | 25.4 | e2e-ios | 23.8 | 18.0 | 0.1 | 39/39 |
| 2026-10-06 08:13 | [37434735427](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37434735427) | e8a87b5 | 30.4 | e2e-android | 29.6 | 26.6 | 0.1 | 39/39 |
| 2026-10-06 08:13 | [37434732215](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37434732215) | e8a87b5 | 26.1 | e2e-ios | 24.6 | 18.3 | 0.2 | 39/39 |
| 2026-10-06 05:44 | [37420011410](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37420011410) | e8a87b5 | 23.4 | e2e-android | 22.8 | 19.9 | 0.0 | 39/39, 1 passed on retry |
| 2026-10-06 05:44 | [37420009070](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37420009070) | e8a87b5 | 25.1 | e2e-ios | 23.5 | 18.2 | 0.1 | 39/39 |
| 2026-10-06 03:14 | [37408061296](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37408061296) | e8a87b5 | 22.5 | e2e-android | 21.7 | 18.6 | 0.0 | 39/39 |
| 2026-10-06 03:14 | [37408058665](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37408058665) | e8a87b5 | 29.1 | e2e-ios | 27.8 | 22.5 | 0.1 | 39/39, 1 passed on retry |
| 2026-10-06 00:44 | [37395564636](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37395564636) | e8a87b5 | 30.9 | e2e-android | 30.1 | 26.5 | 0.1 | 39/39 |
| 2026-10-06 00:44 | [37395562190](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37395562190) | e8a87b5 | 24.3 | e2e-ios | 22.8 | 16.4 | 0.1 | 39/39 |
| 2026-10-05 22:19 | [37381716983](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37381716983) | e8a87b5 | 26.4 | e2e-android | 25.7 | 22.1 | 0.0 | 39/39 |
| 2026-10-05 22:19 | [37381713936](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37381713936) | e8a87b5 | 24.9 | e2e-ios | 23.1 | 17.4 | 0.1 | 39/39 |
| 2026-10-05 20:35 | [37370666556](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37370666556) | - | 13.6 | e2e-ios | 6.8 | 1.4 | 0.2 | failure |
| 2026-10-05 18:50 | [37359047865](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37359047865) | e8a87b5 | 33.9 | e2e-android | 26.2 | 22.9 | 0.1 | 39/39 |
| 2026-10-05 18:50 | [37359043490](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37359043490) | e8a87b5 | 40.3 | e2e-ios | 22.1 | 15.6 | 0.7 | 39/39 |
| 2026-10-05 15:43 | [37335175110](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37335175110) | e8a87b5 | 38.1 | e2e-android | 29.5 | 26.6 | 0.0 | 39/39 |
| 2026-10-05 15:43 | [37335170371](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37335170371) | e8a87b5 | 58.1 | e2e-ios | 38.0 | 28.1 | 0.2 | 39/39 |
| 2026-10-05 12:58 | [37313284114](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37313284114) | e8a87b5 | 29.1 | e2e-android | 28.4 | 25.4 | 0.0 | 39/39 |
| 2026-10-05 12:58 | [37313280155](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37313280155) | e8a87b5 | 31.3 | e2e-ios | 24.7 | 19.5 | 5.1 | 39/39 |
| 2026-10-05 09:27 | [37290122887](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37290122887) | e8a87b5 | 25.6 | e2e-android | 24.8 | 21.8 | 0.1 | 39/39 |
| 2026-10-05 09:27 | [37290119820](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37290119820) | e8a87b5 | 33.2 | e2e-ios | 25.4 | 19.1 | 0.4 | 39/39 |
| 2026-10-05 05:10 | [37266615578](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37266615578) | 6904d0f | 34.6 | e2e-android | 34.0 | 30.8 | 0.0 | 39/39 |
| 2026-10-05 05:10 | [37266613791](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37266613791) | 6904d0f | 29.1 | e2e-ios | 27.5 | 21.7 | 0.1 | 39/39 |
| 2026-10-05 03:12 | [37258514908](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37258514908) | 6904d0f | 30.0 | e2e-android | 29.2 | 26.2 | 0.0 | 39/39 |
| 2026-10-05 03:12 | [37258513089](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37258513089) | 6904d0f | 23.2 | e2e-ios | 21.9 | 17.1 | 0.1 | 39/39 |
| 2026-10-05 01:04 | [37249946360](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37249946360) | 6904d0f | 22.0 | e2e-android | 21.3 | 18.7 | 0.0 | 39/39 |
| 2026-10-05 01:04 | [37249944679](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37249944679) | 6904d0f | 23.5 | e2e-ios | 22.4 | 16.8 | 0.1 | 39/39 |
| 2026-10-04 23:01 | [37242206606](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37242206606) | 6904d0f | 28.4 | e2e-android | 27.9 | 24.6 | 0.0 | 39/39 |
| 2026-10-04 23:01 | [37242205050](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37242205050) | 6904d0f | 28.3 | e2e-ios | 26.7 | 20.5 | 0.2 | 39/39 |
| 2026-10-04 21:02 | [37234473598](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37234473598) | 6904d0f | 30.6 | e2e-android | 29.8 | 26.5 | 0.0 | 39/39 |
| 2026-10-04 21:02 | [37234471108](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37234471108) | 6904d0f | 29.5 | e2e-ios | 27.9 | 20.7 | 0.1 | 39/39 |
| 2026-10-04 19:09 | [37227184345](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37227184345) | 6904d0f | 25.7 | e2e-android | 25.2 | 22.5 | 0.0 | 39/39 |
| 2026-10-04 19:09 | [37227182470](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37227182470) | 6904d0f | 22.1 | e2e-ios | 20.5 | 16.0 | 0.1 | 39/39, 1 passed on retry |
| 2026-10-04 17:00 | [37218903309](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37218903309) | 6904d0f | 38.4 | e2e-android | 37.8 | 34.5 | 0.0 | 39/39, 2 passed on retry |
| 2026-10-04 17:00 | [37218901316](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37218901316) | 6904d0f | 27.4 | e2e-ios | 26.0 | 20.1 | 0.1 | 39/39, 1 passed on retry |
| 2026-10-04 14:57 | [37211201173](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37211201173) | 6904d0f | 21.9 | e2e-android | 21.3 | 18.7 | 0.0 | 39/39 |
| 2026-10-04 14:57 | [37211199412](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37211199412) | 6904d0f | 23.0 | e2e-ios | 21.5 | 17.7 | 0.1 | 39/39 |
| 2026-10-04 12:39 | [37202864501](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37202864501) | 6904d0f | 34.8 | e2e-android | 34.0 | 31.0 | 0.1 | 39/39, 1 passed on retry |
| 2026-10-04 12:39 | [37202862773](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37202862773) | 6904d0f | 27.7 | e2e-ios | 26.4 | 22.2 | 0.1 | 39/39 |
| 2026-10-04 10:05 | [37194258500](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37194258500) | 6904d0f | 30.0 | e2e-android | 29.3 | 26.5 | 0.0 | 39/39, 1 passed on retry |
| 2026-10-04 10:05 | [37194256527](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37194256527) | 6904d0f | 28.2 | e2e-ios | 26.7 | 19.4 | 0.2 | 39/39 |
| 2026-10-04 06:41 | [37183539678](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37183539678) | 6904d0f | 25.8 | e2e-android | 25.1 | 22.1 | 0.0 | 39/39 |
| 2026-10-04 06:41 | [37183538410](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37183538410) | 6904d0f | 20.0 | e2e-ios | 17.1 | 12.8 | 1.5 | 39/39 |
| 2026-10-04 05:29 | [37180049976](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37180049976) | 6904d0f | 34.0 | e2e-android | 33.4 | 30.2 | 0.0 | 39/39 |
| 2026-10-04 05:29 | [37180048690](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37180048690) | 6904d0f | 25.1 | e2e-ios | 23.7 | 19.0 | 0.1 | 39/39 |
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

## Runs: upstream

| Started (UTC) | Run | Build | Run time | Job | Job time | Tests | Queue | Result |
|---|---|---|---|---|---|---|---|---|
| 2026-10-07 04:08 | [37570045585](https://github.com/react-navigation/react-navigation/actions/runs/37570045585) | agent-device | 33.9 | e2e-android | 26.9 | 24.0 | 0.1 | 39/39 |
| 2026-10-07 04:05 | [37569827168](https://github.com/react-navigation/react-navigation/actions/runs/37569827168) | agent-device | 50.9 | e2e-ios | 35.0 | 26.7 | 0.2 | 39/39 |
| 2026-10-06 11:10 | [37454662174](https://github.com/react-navigation/react-navigation/actions/runs/37454662174) | agent-device | 37.7 | e2e-android | 27.5 | 24.5 | 0.1 | 39/39 |
| 2026-10-06 11:10 | [37454662129](https://github.com/react-navigation/react-navigation/actions/runs/37454662129) | agent-device | 58.0 | e2e-ios | 37.1 | 28.3 | 0.1 | 39/39 |
| 2026-10-06 04:08 | [37412295800](https://github.com/react-navigation/react-navigation/actions/runs/37412295800) | agent-device | 39.5 | e2e-android | 26.8 | 24.0 | 0.0 | 39/39 |
| 2026-10-05 18:34 | [37357015711](https://github.com/react-navigation/react-navigation/actions/runs/37357015711) | agent-device | 47.6 | e2e-ios | 38.0 | 29.8 | 0.1 | 39/39, 1 passed on retry |
| 2026-10-05 18:34 | [37357015502](https://github.com/react-navigation/react-navigation/actions/runs/37357015502) | agent-device | 27.4 | e2e-android | 26.4 | 23.6 | 0.1 | 39/39 |
| 2026-10-05 15:02 | [37329634069](https://github.com/react-navigation/react-navigation/actions/runs/37329634069) | agent-device | 40.5 | e2e-android | 27.8 | 24.9 | 0.1 | 39/39 |
| 2026-10-05 15:02 | [37329633022](https://github.com/react-navigation/react-navigation/actions/runs/37329633022) | agent-device | 61.2 | e2e-ios | 41.5 | 31.4 | 0.2 | 39/39, 1 passed on retry |
| 2026-10-05 04:13 | [37262554846](https://github.com/react-navigation/react-navigation/actions/runs/37262554846) | agent-device | 34.8 | e2e-android | 26.9 | 24.0 | 0.1 | 39/39 |
| 2026-10-05 04:10 | [37262362326](https://github.com/react-navigation/react-navigation/actions/runs/37262362326) | agent-device | 60.0 | e2e-ios | 44.5 | 36.2 | 0.2 | 39/39, 2 passed on retry |
| 2026-10-04 05:26 | [37179899296](https://github.com/react-navigation/react-navigation/actions/runs/37179899296) | agent-device | 23.9 | e2e-android | 23.2 | 20.0 | 0.1 | 39/39 |
| 2026-10-04 05:21 | [37179668697](https://github.com/react-navigation/react-navigation/actions/runs/37179668697) | agent-device | 40.2 | e2e-ios | 38.7 | 25.8 | 0.1 | 39/39 |
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
| 2026-09-05 04:04 | [33943579118](https://github.com/react-navigation/react-navigation/actions/runs/33943579118) | agent-device | 44.7 | e2e-ios | 28.0 | 18.9 | 0.1 | 39/39 |
| 2026-09-04 04:08 | [33835679643](https://github.com/react-navigation/react-navigation/actions/runs/33835679643) | agent-device | - | e2e-android | - | 24.2 | 0.1 | 39/39 |
| 2026-09-04 04:04 | [33835488234](https://github.com/react-navigation/react-navigation/actions/runs/33835488234) | agent-device | 50.5 | e2e-ios | 29.4 | 21.8 | 0.1 | 39/39 |
| 2026-09-02 04:08 | [33589635197](https://github.com/react-navigation/react-navigation/actions/runs/33589635197) | agent-device | - | e2e-android | - | 23.9 | 0.1 | 39/39 |
| 2026-09-02 04:05 | [33589438966](https://github.com/react-navigation/react-navigation/actions/runs/33589438966) | agent-device | 41.9 | e2e-ios | 29.6 | 24.4 | 0.1 | 39/39, 1 passed on retry |
| 2026-08-16 04:12 | [31926067597](https://github.com/react-navigation/react-navigation/actions/runs/31926067597) | agent-device | 26.3 | e2e-ios | 25.2 | 18.9 | 0.1 | 39/39 |
| 2026-08-15 04:08 | [31863655299](https://github.com/react-navigation/react-navigation/actions/runs/31863655299) | agent-device | 45.0 | e2e-ios | 27.6 | 19.8 | 0.1 | 39/39, 1 passed on retry |
| 2026-08-14 04:33 | [31770206908](https://github.com/react-navigation/react-navigation/actions/runs/31770206908) | agent-device | 44.7 | e2e-ios | 25.1 | 20.0 | 0.1 | 39/39 |
| 2026-08-13 04:33 | [31667421551](https://github.com/react-navigation/react-navigation/actions/runs/31667421551) | agent-device | 46.2 | e2e-ios | 25.4 | 17.8 | 0.1 | 39/39 |
| 2026-08-12 04:33 | [31563616036](https://github.com/react-navigation/react-navigation/actions/runs/31563616036) | agent-device | 42.8 | e2e-ios | 28.2 | 20.2 | 0.1 | 39/39, 1 passed on retry |
| 2026-08-11 04:28 | [31458555841](https://github.com/react-navigation/react-navigation/actions/runs/31458555841) | agent-device | 44.8 | e2e-ios | 30.0 | 22.1 | 0.1 | 39/39 |
| 2026-08-10 21:32 | [31434316365](https://github.com/react-navigation/react-navigation/actions/runs/31434316365) | agent-device | 45.3 | e2e-ios | 29.9 | 23.2 | 0.1 | 39/39, 2 passed on retry |
| 2026-08-10 14:44 | [31399797442](https://github.com/react-navigation/react-navigation/actions/runs/31399797442) | agent-device | 48.5 | e2e-ios | 33.0 | 24.8 | 0.1 | 39/39 |
| 2026-08-10 04:30 | [31355689716](https://github.com/react-navigation/react-navigation/actions/runs/31355689716) | agent-device | 35.5 | e2e-ios | 33.8 | 24.3 | 0.1 | 39/39, 1 passed on retry |
| 2026-08-09 04:26 | [31294568479](https://github.com/react-navigation/react-navigation/actions/runs/31294568479) | agent-device | 42.0 | e2e-ios | 40.4 | 31.1 | 0.1 | 39/39 |
| 2026-08-08 09:00 | [31249634806](https://github.com/react-navigation/react-navigation/actions/runs/31249634806) | agent-device | 25.1 | e2e-ios | 24.0 | 18.6 | 0.1 | 39/39, 1 passed on retry |
| 2026-08-08 04:22 | [31239308276](https://github.com/react-navigation/react-navigation/actions/runs/31239308276) | agent-device | 55.5 | e2e-ios | 35.0 | 22.5 | 0.1 | 39/39 |
| 2026-08-07 19:10 | [31210320959](https://github.com/react-navigation/react-navigation/actions/runs/31210320959) | agent-device | 46.9 | e2e-ios | 29.9 | 21.9 | 0.1 | 39/39 |
| 2026-08-07 04:38 | [31148034317](https://github.com/react-navigation/react-navigation/actions/runs/31148034317) | agent-device | 45.9 | e2e-ios | 27.0 | 19.8 | 0.1 | 39/39 |
| 2026-08-06 09:49 | [31090680669](https://github.com/react-navigation/react-navigation/actions/runs/31090680669) | agent-device | 42.9 | e2e-ios | 30.9 | 23.6 | 0.1 | 39/39 |
| 2026-08-05 20:04 | [31042334082](https://github.com/react-navigation/react-navigation/actions/runs/31042334082) | agent-device | - | e2e-android | - | 23.4 | 0.2 | 39/39 |
| 2026-08-05 14:12 | [31013967027](https://github.com/react-navigation/react-navigation/actions/runs/31013967027) | agent-device | - | e2e-android | - | 23.2 | 0.1 | 39/39 |
| 2026-08-05 14:12 | [31013966930](https://github.com/react-navigation/react-navigation/actions/runs/31013966930) | agent-device | 54.9 | e2e-ios | 41.6 | 35.4 | 0.1 | 39/39, 1 passed on retry |
| 2026-08-05 05:02 | [30976894497](https://github.com/react-navigation/react-navigation/actions/runs/30976894497) | agent-device | - | e2e-android | - | 27.8 | 0.1 | 39/39, 1 passed on retry |
| 2026-08-05 05:01 | [30976832666](https://github.com/react-navigation/react-navigation/actions/runs/30976832666) | agent-device | 57.5 | e2e-ios | 33.0 | 23.4 | 0.1 | 39/39 |
| 2026-08-04 05:02 | [30879450590](https://github.com/react-navigation/react-navigation/actions/runs/30879450590) | agent-device | - | e2e-android | - | 19.6 | 0.1 | 39/39 |
| 2026-08-04 05:01 | [30879372865](https://github.com/react-navigation/react-navigation/actions/runs/30879372865) | agent-device | 51.2 | e2e-ios | 34.3 | 24.8 | 0.1 | 39/39, 1 passed on retry |
| 2026-08-04 00:46 | [30866636153](https://github.com/react-navigation/react-navigation/actions/runs/30866636153) | agent-device | - | e2e-android | - | 23.0 | 0.1 | 39/39 |
| 2026-08-04 00:46 | [30866636029](https://github.com/react-navigation/react-navigation/actions/runs/30866636029) | agent-device | 43.7 | e2e-ios | 42.7 | 31.4 | 0.1 | 39/39, 1 passed on retry |
| 2026-08-03 16:28 | [30832352180](https://github.com/react-navigation/react-navigation/actions/runs/30832352180) | agent-device | - | e2e-android | - | 23.0 | 0.1 | 39/39 |
| 2026-08-03 16:28 | [30832351137](https://github.com/react-navigation/react-navigation/actions/runs/30832351137) | agent-device | 36.4 | e2e-ios | 35.1 | 23.7 | 0.1 | 39/39 |
| 2026-08-03 11:02 | [30807945335](https://github.com/react-navigation/react-navigation/actions/runs/30807945335) | agent-device | - | e2e-android | - | 24.1 | 0.1 | 39/39, 2 passed on retry |
| 2026-08-03 11:02 | [30807945309](https://github.com/react-navigation/react-navigation/actions/runs/30807945309) | agent-device | 32.6 | e2e-ios | 31.2 | 24.2 | 0.1 | 39/39, 1 passed on retry |
| 2026-08-03 05:12 | [30786478984](https://github.com/react-navigation/react-navigation/actions/runs/30786478984) | agent-device | - | e2e-android | - | 23.1 | 0.1 | 39/39, 1 passed on retry |
| 2026-08-03 05:10 | [30786398808](https://github.com/react-navigation/react-navigation/actions/runs/30786398808) | agent-device | 46.5 | e2e-ios | 30.7 | 23.6 | 0.1 | 39/39 |
| 2026-08-02 17:23 | [30758758104](https://github.com/react-navigation/react-navigation/actions/runs/30758758104) | agent-device | - | e2e-android | - | 23.5 | 0.1 | 39/39, 1 passed on retry |
| 2026-08-02 17:23 | [30758758098](https://github.com/react-navigation/react-navigation/actions/runs/30758758098) | agent-device | 44.4 | e2e-ios | 31.1 | 23.1 | 0.1 | 39/39 |
| 2026-08-02 05:03 | [30733450711](https://github.com/react-navigation/react-navigation/actions/runs/30733450711) | agent-device | - | e2e-android | - | 23.4 | 0.1 | 39/39, 1 passed on retry |
| 2026-08-02 05:02 | [30733409614](https://github.com/react-navigation/react-navigation/actions/runs/30733409614) | agent-device | 26.4 | e2e-ios | 25.0 | 19.0 | 0.1 | 39/39 |
| 2026-08-01 05:04 | [30685120778](https://github.com/react-navigation/react-navigation/actions/runs/30685120778) | agent-device | - | e2e-android | - | 23.2 | 0.1 | 39/39 |
| 2026-08-01 05:02 | [30685077227](https://github.com/react-navigation/react-navigation/actions/runs/30685077227) | agent-device | 47.0 | e2e-ios | 32.5 | 23.8 | 0.1 | 39/39, 1 passed on retry |
| 2026-07-31 21:37 | [30667229542](https://github.com/react-navigation/react-navigation/actions/runs/30667229542) | agent-device | 49.8 | e2e-ios | 35.4 | 27.8 | 0.1 | 39/39, 1 passed on retry |
| 2026-07-31 21:37 | [30667229447](https://github.com/react-navigation/react-navigation/actions/runs/30667229447) | agent-device | - | e2e-android | - | 24.9 | 0.1 | 39/39, 1 passed on retry |
| 2026-07-31 05:09 | [30606027234](https://github.com/react-navigation/react-navigation/actions/runs/30606027234) | agent-device | - | e2e-android | - | 26.6 | 0.1 | 39/39, 1 passed on retry |
| 2026-07-31 05:08 | [30605960099](https://github.com/react-navigation/react-navigation/actions/runs/30605960099) | agent-device | 52.6 | e2e-ios | 33.5 | 24.0 | 0.1 | 39/39 |

## Trend

![react-navigation-android](charts/react-navigation-android.svg)

![react-navigation-ios](charts/react-navigation-ios.svg)


## Retried test cases

Per run, from each job's log: a flow *failed at least once* if any of its attempts failed, inside its job (maestro-runner `--retries`, React Native's iOS per-flow attempts, agent-device, Expo's rounds) or in a retry job (React Native's retry_1/retry_2); it *passed on retry* if it then passed. *Extra flow runs* counts every run of a flow beyond its first, including whole-suite reruns of flows that had passed. Runs whose logs had expired are left out.

Each cell: **ours vs upstream**; the better one in bold. Ours is the newest maestro-runner build.

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing (ours / upstream) |
|---|---|---|---|---|---|---|---|---|---|
| android | e8a87b5 | 20 vs 54 | 25.4 vs **23.9** | **90%** vs 70% | **0.10** vs 0.33 | 0% vs 0% | **0.1** vs 0.4 | 0% vs 0% | Tab View - Custom Tab Bar ×1, Showcase - Material Top Tabs ×1 / Tab View - Scrollable Tab Bar ×7, Bottom Tabs - Preload Flow ×5, Screen Layout ×2 |
| ios | e8a87b5 | 20 vs 67 | **18.3** vs 24.0 | **90%** vs 60% | **0.10** vs 0.45 | 0% vs 0% | **0.1** vs 0.5 | 0% vs 0% | Auth Flow ×2 / Tab View - Scrollable Tab Bar ×4, Native Stack - Prevent Remove ×4, Screen Layout ×3 |

Ours on earlier maestro-runner builds:

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing |
|---|---|---|---|---|---|---|---|---|---|
| android | 6904d0f | 17 | 26.2 | 82% | 0.24 | 0% | 0.3 | 0% | Tab View - Scrollable Tab Bar ×2, Tab View - Coverflow ×1, Tab View - Custom Tab Bar ×1 |
| ios | 6904d0f | 17 | 19.0 | 82% | 0.18 | 0% | 0.2 | 0% | Screen Layout ×2, Material Top Tabs - Basic ×1 |

### Per run

| Started (UTC) | Run | Platform | Side | Build | Flows | Failed at least once | Passed on retry (failed attempts) | Failed at the end | Extra flow runs | Retry jobs |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-07 21:57 | [37692975274](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37692975274) | android | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-07 21:57 | [37692972267](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37692972267) | ios | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-07 16:36 | [37653349409](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37653349409) | android | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-07 16:36 | [37653345106](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37653345106) | ios | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-07 11:20 | [37613392889](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37613392889) | android | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-07 11:20 | [37613389805](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37613389805) | ios | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-07 05:59 | [37579049256](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37579049256) | android | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-07 05:59 | [37579047010](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37579047010) | ios | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-07 04:08 | [37570045585](https://github.com/react-navigation/react-navigation/actions/runs/37570045585) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-10-07 04:05 | [37569827168](https://github.com/react-navigation/react-navigation/actions/runs/37569827168) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-10-07 03:29 | [37566964182](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37566964182) | android | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-07 03:29 | [37566962164](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37566962164) | ios | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-07 00:54 | [37554369088](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37554369088) | android | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-07 00:54 | [37554366542](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37554366542) | ios | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-06 22:29 | [37540927744](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37540927744) | android | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-06 22:29 | [37540924470](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37540924470) | ios | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-06 19:38 | [37520539021](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37520539021) | android | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-06 19:38 | [37520535200](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37520535200) | ios | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-06 16:47 | [37498469935](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37498469935) | android | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-06 16:47 | [37498465100](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37498465100) | ios | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-06 13:50 | [37473990531](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37473990531) | android | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-06 13:50 | [37473985583](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37473985583) | ios | ours | e8a87b5 | 39 | 1 | Auth Flow (1) | - | 1 | 0 |
| 2026-10-06 11:10 | [37454662174](https://github.com/react-navigation/react-navigation/actions/runs/37454662174) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-10-06 11:10 | [37454662129](https://github.com/react-navigation/react-navigation/actions/runs/37454662129) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-10-06 10:59 | [37453432301](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37453432301) | android | ours | e8a87b5 | 39 | 1 | Tab View - Custom Tab Bar (1) | - | 1 | 0 |
| 2026-10-06 10:59 | [37453428830](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37453428830) | ios | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-06 08:13 | [37434735427](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37434735427) | android | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-06 08:13 | [37434732215](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37434732215) | ios | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-06 05:44 | [37420011410](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37420011410) | android | ours | e8a87b5 | 39 | 1 | Showcase - Material Top Tabs (1) | - | 1 | 0 |
| 2026-10-06 05:44 | [37420009070](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37420009070) | ios | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-06 04:08 | [37412295800](https://github.com/react-navigation/react-navigation/actions/runs/37412295800) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-10-06 03:14 | [37408061296](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37408061296) | android | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-06 03:14 | [37408058665](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37408058665) | ios | ours | e8a87b5 | 39 | 1 | Auth Flow (1) | - | 1 | 0 |
| 2026-10-06 00:44 | [37395564636](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37395564636) | android | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-06 00:44 | [37395562190](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37395562190) | ios | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-05 22:19 | [37381716983](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37381716983) | android | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-05 22:19 | [37381713936](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37381713936) | ios | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-05 18:50 | [37359047865](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37359047865) | android | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-05 18:50 | [37359043490](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37359043490) | ios | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-05 18:34 | [37357015711](https://github.com/react-navigation/react-navigation/actions/runs/37357015711) | ios | upstream | - | 39 | 1 | Tab View - Coverflow (1) | - | 1 | 0 |
| 2026-10-05 18:34 | [37357015502](https://github.com/react-navigation/react-navigation/actions/runs/37357015502) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-10-05 15:43 | [37335175110](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37335175110) | android | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-05 15:43 | [37335170371](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37335170371) | ios | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-05 15:02 | [37329634069](https://github.com/react-navigation/react-navigation/actions/runs/37329634069) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-10-05 15:02 | [37329633022](https://github.com/react-navigation/react-navigation/actions/runs/37329633022) | ios | upstream | - | 39 | 1 | Tab View - Auto Width Tab Bar (1) | - | 1 | 0 |
| 2026-10-05 12:58 | [37313284114](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37313284114) | android | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-05 12:58 | [37313280155](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37313280155) | ios | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-05 09:27 | [37290122887](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37290122887) | android | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-05 09:27 | [37290119820](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37290119820) | ios | ours | e8a87b5 | 39 | 0 | - | - | 0 | 0 |
| 2026-10-05 05:10 | [37266615578](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37266615578) | android | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-05 05:10 | [37266613791](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37266613791) | ios | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-05 04:13 | [37262554846](https://github.com/react-navigation/react-navigation/actions/runs/37262554846) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-10-05 04:10 | [37262362326](https://github.com/react-navigation/react-navigation/actions/runs/37262362326) | ios | upstream | - | 39 | 2 | Stack - Retain (2), Static config (1) | - | 3 | 0 |
| 2026-10-05 03:12 | [37258514908](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37258514908) | android | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-05 03:12 | [37258513089](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37258513089) | ios | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-05 01:04 | [37249946360](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37249946360) | android | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-05 01:04 | [37249944679](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37249944679) | ios | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-04 23:01 | [37242206606](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37242206606) | android | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-04 23:01 | [37242205050](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37242205050) | ios | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-04 21:02 | [37234473598](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37234473598) | android | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-04 21:02 | [37234471108](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37234471108) | ios | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-04 19:09 | [37227184345](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37227184345) | android | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-04 19:09 | [37227182470](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37227182470) | ios | ours | 6904d0f | 39 | 1 | Screen Layout (1) | - | 1 | 0 |
| 2026-10-04 17:00 | [37218903309](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37218903309) | android | ours | 6904d0f | 39 | 2 | Tab View - Coverflow (1), Tab View - Scrollable Tab Bar (2) | - | 3 | 0 |
| 2026-10-04 17:00 | [37218901316](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37218901316) | ios | ours | 6904d0f | 39 | 1 | Screen Layout (1) | - | 1 | 0 |
| 2026-10-04 14:57 | [37211201173](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37211201173) | android | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-04 14:57 | [37211199412](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37211199412) | ios | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-04 12:39 | [37202864501](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37202864501) | android | ours | 6904d0f | 39 | 1 | Tab View - Scrollable Tab Bar (1) | - | 1 | 0 |
| 2026-10-04 12:39 | [37202862773](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37202862773) | ios | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-04 10:05 | [37194258500](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37194258500) | android | ours | 6904d0f | 39 | 1 | Tab View - Custom Tab Bar (1) | - | 1 | 0 |
| 2026-10-04 10:05 | [37194256527](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37194256527) | ios | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-04 06:41 | [37183539678](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37183539678) | android | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-04 06:41 | [37183538410](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37183538410) | ios | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-04 05:29 | [37180049976](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37180049976) | android | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-04 05:29 | [37180048690](https://github.com/maestro-runner-bench/react-navigation/actions/runs/37180048690) | ios | ours | 6904d0f | 39 | 0 | - | - | 0 | 0 |
| 2026-10-04 05:26 | [37179899296](https://github.com/react-navigation/react-navigation/actions/runs/37179899296) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-10-04 05:21 | [37179668697](https://github.com/react-navigation/react-navigation/actions/runs/37179668697) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
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
| 2026-10-02 04:07 | [36963190410](https://github.com/react-navigation/react-navigation/actions/runs/36963190410) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-10-02 04:05 | [36962985542](https://github.com/react-navigation/react-navigation/actions/runs/36962985542) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
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
| 2026-09-05 04:04 | [33943579118](https://github.com/react-navigation/react-navigation/actions/runs/33943579118) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-04 04:08 | [33835679643](https://github.com/react-navigation/react-navigation/actions/runs/33835679643) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-04 04:04 | [33835488234](https://github.com/react-navigation/react-navigation/actions/runs/33835488234) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-02 04:08 | [33589635197](https://github.com/react-navigation/react-navigation/actions/runs/33589635197) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-09-02 04:05 | [33589438966](https://github.com/react-navigation/react-navigation/actions/runs/33589438966) | ios | upstream | - | 39 | 1 | Stack - Prevent Remove (1) | - | 1 | 0 |
| 2026-08-16 04:12 | [31926067597](https://github.com/react-navigation/react-navigation/actions/runs/31926067597) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-08-15 04:08 | [31863655299](https://github.com/react-navigation/react-navigation/actions/runs/31863655299) | ios | upstream | - | 39 | 1 | Bottom Tabs - Preload Flow (1) | - | 1 | 0 |
| 2026-08-14 04:33 | [31770206908](https://github.com/react-navigation/react-navigation/actions/runs/31770206908) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-08-13 04:33 | [31667421551](https://github.com/react-navigation/react-navigation/actions/runs/31667421551) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-08-12 04:33 | [31563616036](https://github.com/react-navigation/react-navigation/actions/runs/31563616036) | ios | upstream | - | 39 | 1 | Static config (1) | - | 1 | 0 |
| 2026-08-11 04:28 | [31458555841](https://github.com/react-navigation/react-navigation/actions/runs/31458555841) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-08-10 21:32 | [31434316365](https://github.com/react-navigation/react-navigation/actions/runs/31434316365) | ios | upstream | - | 39 | 2 | Tab View - Scrollable Tab Bar (1), Drawer - Master Detail (1) | - | 2 | 0 |
| 2026-08-10 14:44 | [31399797442](https://github.com/react-navigation/react-navigation/actions/runs/31399797442) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-08-10 04:30 | [31355689716](https://github.com/react-navigation/react-navigation/actions/runs/31355689716) | ios | upstream | - | 39 | 1 | Bottom Tabs - Dynamic (1) | - | 1 | 0 |
| 2026-08-09 04:26 | [31294568479](https://github.com/react-navigation/react-navigation/actions/runs/31294568479) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-08-08 09:00 | [31249634806](https://github.com/react-navigation/react-navigation/actions/runs/31249634806) | ios | upstream | - | 39 | 1 | Native Stack - Prevent Remove (1) | - | 1 | 0 |
| 2026-08-08 04:22 | [31239308276](https://github.com/react-navigation/react-navigation/actions/runs/31239308276) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-08-07 19:10 | [31210320959](https://github.com/react-navigation/react-navigation/actions/runs/31210320959) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-08-07 04:38 | [31148034317](https://github.com/react-navigation/react-navigation/actions/runs/31148034317) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-08-06 09:49 | [31090680669](https://github.com/react-navigation/react-navigation/actions/runs/31090680669) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-08-05 20:04 | [31042334082](https://github.com/react-navigation/react-navigation/actions/runs/31042334082) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-08-05 14:12 | [31013967027](https://github.com/react-navigation/react-navigation/actions/runs/31013967027) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-08-05 14:12 | [31013966930](https://github.com/react-navigation/react-navigation/actions/runs/31013966930) | ios | upstream | - | 39 | 1 | Native Stack - Prevent Remove (1) | - | 1 | 0 |
| 2026-08-05 05:02 | [30976894497](https://github.com/react-navigation/react-navigation/actions/runs/30976894497) | android | upstream | - | 39 | 1 | Screen Layout (1) | - | 1 | 0 |
| 2026-08-05 05:01 | [30976832666](https://github.com/react-navigation/react-navigation/actions/runs/30976832666) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-08-04 05:02 | [30879450590](https://github.com/react-navigation/react-navigation/actions/runs/30879450590) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-08-04 05:01 | [30879372865](https://github.com/react-navigation/react-navigation/actions/runs/30879372865) | ios | upstream | - | 39 | 1 | Native Stack - Prevent Remove (1) | - | 1 | 0 |
| 2026-08-04 00:46 | [30866636153](https://github.com/react-navigation/react-navigation/actions/runs/30866636153) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-08-04 00:46 | [30866636029](https://github.com/react-navigation/react-navigation/actions/runs/30866636029) | ios | upstream | - | 39 | 1 | Bottom Tabs - Preload Flow (1) | - | 1 | 0 |
| 2026-08-03 16:28 | [30832352180](https://github.com/react-navigation/react-navigation/actions/runs/30832352180) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-08-03 16:28 | [30832351137](https://github.com/react-navigation/react-navigation/actions/runs/30832351137) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-08-03 11:02 | [30807945335](https://github.com/react-navigation/react-navigation/actions/runs/30807945335) | android | upstream | - | 39 | 2 | Screen Layout (1), Bottom Tabs - Preload Flow (2) | - | 3 | 0 |
| 2026-08-03 11:02 | [30807945309](https://github.com/react-navigation/react-navigation/actions/runs/30807945309) | ios | upstream | - | 39 | 1 | Stack - Preload Flow (1) | - | 1 | 0 |
| 2026-08-03 05:12 | [30786478984](https://github.com/react-navigation/react-navigation/actions/runs/30786478984) | android | upstream | - | 39 | 1 | Native Stack - Card + Modal (1) | - | 1 | 0 |
| 2026-08-03 05:10 | [30786398808](https://github.com/react-navigation/react-navigation/actions/runs/30786398808) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-08-02 17:23 | [30758758104](https://github.com/react-navigation/react-navigation/actions/runs/30758758104) | android | upstream | - | 39 | 1 | Bottom Tabs - Preload Flow (1) | - | 1 | 0 |
| 2026-08-02 17:23 | [30758758098](https://github.com/react-navigation/react-navigation/actions/runs/30758758098) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-08-02 05:03 | [30733450711](https://github.com/react-navigation/react-navigation/actions/runs/30733450711) | android | upstream | - | 39 | 1 | Native Stack - Card + Modal (1) | - | 1 | 0 |
| 2026-08-02 05:02 | [30733409614](https://github.com/react-navigation/react-navigation/actions/runs/30733409614) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-08-01 05:04 | [30685120778](https://github.com/react-navigation/react-navigation/actions/runs/30685120778) | android | upstream | - | 39 | 0 | - | - | 0 | 0 |
| 2026-08-01 05:02 | [30685077227](https://github.com/react-navigation/react-navigation/actions/runs/30685077227) | ios | upstream | - | 39 | 1 | Native Stack - Basic (1) | - | 1 | 0 |
| 2026-07-31 21:37 | [30667229542](https://github.com/react-navigation/react-navigation/actions/runs/30667229542) | ios | upstream | - | 39 | 1 | Native Stack - Preload Flow (1) | - | 1 | 0 |
| 2026-07-31 21:37 | [30667229447](https://github.com/react-navigation/react-navigation/actions/runs/30667229447) | android | upstream | - | 39 | 1 | Stack - Prevent Remove (1) | - | 1 | 0 |
| 2026-07-31 05:09 | [30606027234](https://github.com/react-navigation/react-navigation/actions/runs/30606027234) | android | upstream | - | 39 | 1 | Tab View - Scrollable Tab Bar (1) | - | 1 | 0 |
| 2026-07-31 05:08 | [30605960099](https://github.com/react-navigation/react-navigation/actions/runs/30605960099) | ios | upstream | - | 39 | 0 | - | - | 0 | 0 |
