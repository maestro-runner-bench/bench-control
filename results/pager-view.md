# pager-view

Upstream has no e2e CI to compare against.

Times in minutes. *Run* is the whole workflow run (builds included); *job* is one job; *tests* is its test step only; *queue* is the wait for a runner.

## Summary

| Project | Platform | Flavour | Side | Build | Runs | Median e2e (min) | Green runs | Runs with no first-attempt failure | First-attempt failures / run | Final failures / run | Runs needing a retry job | Runner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pager-view | android | - | ours | 6904d0f | 14 | 19.8 | 0/14 | 0/14 | 9.21 | 8.86 | 0/14 | ubuntu-latest |
| pager-view | android | - | ours | older | 1 | 0.3 | 0/1 | - | - | - | 0/1 | ubuntu-latest |
| pager-view | ios | - | ours | 6904d0f | 15 | 8.8 | 0/15 | 0/15 | 4.07 | 4.00 | 0/15 | macos-26 |

## Runs: maestro-runner (bench fork)

| Started (UTC) | Run | Build | Run time | Job | Job time | Tests | Queue | Result |
|---|---|---|---|---|---|---|---|---|
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
| android | 6904d0f | 14 | 19.8 | 0% | 8.21 | 0% | 16.1 | 100% | ensure-ltr ×14, ensure-rtl ×14, verify-horizontal-rtl-swipe ×14 / - |
| ios | 6904d0f | 15 | 8.8 | 0% | 3.07 | 0% | 6.1 | 100% | ensure-ltr ×15, ensure-rtl ×15, verify-horizontal-rtl-swipe ×15 / - |

### Per run

| Started (UTC) | Run | Platform | Side | Build | Flows | Failed at least once | Passed on retry (failed attempts) | Failed at the end | Extra flow runs | Retry jobs |
|---|---|---|---|---|---|---|---|---|---|---|
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
