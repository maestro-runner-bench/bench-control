# pager-view

Upstream has no e2e CI to compare against.

Times in minutes. *Run* is the whole workflow run (builds included); *job* is one job; *tests* is its test step only; *queue* is the wait for a runner.

## Summary

| Project | Platform | Flavour | Side | Build | Runs | Median e2e (min) | Green runs | Runs with no first-attempt failure | First-attempt failures / run | Final failures / run | Runs needing a retry job | Runner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pager-view | android | - | ours | 6904d0f | 3 | 20.0 | 0/3 | 0/3 | 9.33 | 9.00 | 0/3 | ubuntu-latest |
| pager-view | android | - | ours | older | 1 | 0.3 | 0/1 | - | - | - | 0/1 | ubuntu-latest |
| pager-view | android | - | ours | 49360bb | 1 | 20.1 | 0/1 | 0/1 | 9.00 | 9.00 | 0/1 | ubuntu-latest |
| pager-view | ios | - | ours | 6904d0f | 4 | 8.2 | 0/4 | 0/4 | 4.00 | 4.00 | 0/4 | macos-26 |

## Runs: maestro-runner (bench fork)

| Started (UTC) | Run | Build | Run time | Job | Job time | Tests | Queue | Result |
|---|---|---|---|---|---|---|---|---|
| 2026-10-03 10:23 | [37116242900](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37116242900) | 6904d0f | 37.4 | e2e-android | 21.3 | 20.0 | 0.0 | 12/21 |
|  | | |  | e2e-ios | 37.2 | 8.2 | 0.1 | 17/21 |
| 2026-10-02 23:53 | [37079664391](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37079664391) | 6904d0f | 51.1 | e2e-android | 21.9 | 20.6 | 0.0 | 12/21, 1 passed on retry |
|  | | |  | e2e-ios | 38.5 | 8.2 | 12.6 | 17/21 |
| 2026-10-02 20:22 | [37060147064](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37060147064) | - | 37.6 | e2e-android | 1.8 | 0.3 | 0.0 | failure |
|  | | |  | e2e-ios | 37.4 | 8.0 | 0.1 | 17/21 |
| 2026-10-02 17:22 | [37040250840](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37040250840) | 6904d0f | 33.6 | e2e-android | 19.3 | 18.1 | 0.0 | 12/21 |
|  | | |  | e2e-ios | 33.4 | 9.6 | 0.1 | 17/21 |
| 2026-10-02 14:45 | [37022061725](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37022061725) | - | 21.5 | e2e-android | 21.5 | 20.1 | 0.0 | 12/21 |
|  | | |  | e2e-ios | 15.0 | - | 0.0 | cancelled before tests |

## Retried test cases

Per run, from each job's log: a flow *failed at least once* if any of its attempts failed, inside its job (maestro-runner `--retries`, React Native's iOS per-flow attempts, agent-device, Expo's rounds) or in a retry job (React Native's retry_1/retry_2); it *passed on retry* if it then passed. *Extra flow runs* counts every run of a flow beyond its first, including whole-suite reruns of flows that had passed. Runs whose logs had expired are left out.

| Platform | Side | Build | Runs | Runs where every flow passed first time | Flows that failed at least once / run (avg, max) | Flows passed only on retry / run | Runs ending with a failed flow | Extra flow runs / run | Runs needing a retry job | Flows / run | Most often failing flows |
|---|---|---|---|---|---|---|---|---|---|---|---|
| android | ours | 49360bb | 1 | 0/1 | 8.00, 8 | 0.00 | 1/1 | 16.00 | 0/1 | 16 | nested_pagerView_example ×1, ensure-ltr ×1, ensure-rtl ×1 |
| android | ours | 6904d0f | 3 | 0/3 | 8.33, 9 | 0.33 | 3/3 | 16.33 | 0/3 | 16 | nested_pagerView_example ×3, ensure-ltr ×3, ensure-rtl ×3 |
| ios | ours | 6904d0f | 4 | 0/4 | 3.00, 3 | 0.00 | 4/4 | 6.00 | 0/4 | 16 | ensure-ltr ×4, ensure-rtl ×4, verify-horizontal-rtl-swipe ×4 |

### Per run

| Started (UTC) | Run | Platform | Side | Build | Flows | Failed at least once | Passed on retry (failed attempts) | Failed at the end | Extra flow runs | Retry jobs |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-03 10:23 | [37116242900](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37116242900) | ios | ours | 6904d0f | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-03 10:23 | [37116242900](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37116242900) | android | ours | 6904d0f | 16 | 8 | - | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 16 | 0 |
| 2026-10-02 23:53 | [37079664391](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37079664391) | ios | ours | 6904d0f | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-02 23:53 | [37079664391](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37079664391) | android | ours | 6904d0f | 16 | 9 | scrollable_pagerView_example (1) | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 17 | 0 |
| 2026-10-02 20:22 | [37060147064](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37060147064) | ios | ours | 6904d0f | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-02 17:22 | [37040250840](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37040250840) | ios | ours | 6904d0f | 16 | 3 | - | ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe | 6 | 0 |
| 2026-10-02 17:22 | [37040250840](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37040250840) | android | ours | 6904d0f | 16 | 8 | - | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 16 | 0 |
| 2026-10-02 14:45 | [37022061725](https://github.com/maestro-runner-bench/react-native-pager-view/actions/runs/37022061725) | android | ours | 49360bb | 16 | 8 | - | nested_pagerView_example, ensure-ltr, ensure-rtl, verify-horizontal-rtl-swipe, tab_view_inside_scroll_view_example, issue_1096_keyboard_shrink_repro, issue_1098_nested_pager_repro, issue_1142_search_bar_inset_repro | 16 | 0 |
