# Retried test cases

Per run, from each job's log: a flow *failed at least once* if any of its attempts failed, inside its job (maestro-runner `--retries`, React Native's iOS per-flow attempts, agent-device, Expo's rounds) or in a retry job (React Native's retry_1/retry_2); it *passed on retry* if it then passed. *Extra flow runs* counts every run of a flow beyond its first, including whole-suite reruns of flows that had passed. Runs whose logs had expired are left out.

## enriched-html

Each cell: **ours vs upstream**; the better one in bold. Ours is the newest maestro-runner build.

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing (ours / upstream) |
|---|---|---|---|---|---|---|---|---|---|
| android | e8a87b5 | 8 | 26.4 | 0% | 8.12 | 0% | 0.0 | 100% | checkbox_toggle ×8, line_overlapping ×8, mention_popup_closing_on_cursor_travel ×8 / - |
| ios | 6904d0f | 4 | 29.5 | 0% | 4.50 | 0% | 0.0 | 100% | image_position_stability ×4, inline_code_paste_into_codeblock ×4, links_visual ×4 / - |

Ours on earlier maestro-runner builds:

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing |
|---|---|---|---|---|---|---|---|---|---|
| android | 6904d0f | 18 | 29.6 | 0% | 8.67 | 0% | 0.0 | 100% | checkbox_toggle ×18, line_overlapping ×18, mention_popup_closing_on_cursor_travel ×18 |

## expo

Each cell: **ours vs upstream**; the better one in bold. Ours is the newest maestro-runner build.

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing (ours / upstream) |
|---|---|---|---|---|---|---|---|---|---|
| android | e8a87b5 | 6 vs 48 | 17.9 vs **14.9** | **50%** vs 29% | 3.00 vs **1.67** | 0% vs 0% | 24.0 vs **6.7** | 50% vs **12%** | test ×3, fullscreen-test ×3, picture-in-picture-test.android ×3 / fullscreen-test ×24, maestro-generated ×19, picture-in-picture-test.android ×18 |
| ios | e8a87b5 | 7 vs 43 | **11.2** vs 15.0 | **86%** vs 51% | **0.14** vs 0.81 | 0% vs 0% | **0.1** vs 1.3 | **0%** vs 21% | test ×1 / fullscreen-test ×18, test ×9, playback-test ×8 |

Ours on earlier maestro-runner builds:

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing |
|---|---|---|---|---|---|---|---|---|---|
| android | 6904d0f | 6 | 12.4 | 0% | 1.50 | 0% | 4.3 | 0% | fullscreen-test ×5, picture-in-picture-test.android ×2, maestro-generated ×1 |
| ios | 6904d0f | 5 | 9.6 | 20% | 0.80 | 0% | 0.8 | 0% | fullscreen-test ×2, test ×1, playback-test ×1 |

## pager-view

Each cell: **ours vs upstream**; the better one in bold. Ours is the newest maestro-runner build.

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing (ours / upstream) |
|---|---|---|---|---|---|---|---|---|---|
| android | e8a87b5 | 7 | 19.9 | 0% | 9.29 | 0% | 18.3 | 100% | nested_pagerView_example ×7, ensure-ltr ×7, ensure-rtl ×7 / - |
| ios | e8a87b5 | 7 | 8.8 | 0% | 3.14 | 0% | 6.0 | 100% | ensure-rtl ×7, verify-horizontal-rtl-swipe ×7, ensure-ltr ×6 / - |

Ours on earlier maestro-runner builds:

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing |
|---|---|---|---|---|---|---|---|---|---|
| android | 6904d0f | 16 | 19.8 | 0% | 8.19 | 0% | 16.1 | 100% | ensure-ltr ×16, ensure-rtl ×16, verify-horizontal-rtl-swipe ×16 |
| ios | 6904d0f | 17 | 8.8 | 0% | 3.06 | 0% | 6.1 | 100% | ensure-ltr ×17, ensure-rtl ×17, verify-horizontal-rtl-swipe ×17 |

## react-native

Each cell: **ours vs upstream**; the better one in bold. Ours is the newest maestro-runner build.

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing (ours / upstream) |
|---|---|---|---|---|---|---|---|---|---|
| android debug rntester | e8a87b5 | 5 vs 59 | **11.5** vs 18.9 | 80% vs **93%** | 5.00 vs **1.69** | **0%** vs 8% | **0.0** vs 2.5 | 20% vs **3%** | alert ×1, animated-fade-in-view ×1, appearance ×1 / alert ×4, animated-fade-in-view ×4, appearance ×4 |
| android debug templateapp | e8a87b5 | 5 vs 59 | **2.7** vs 3.3 | **100%** vs 90% | **0.00** vs 0.10 | **0%** vs 10% | **0.0** vs 0.1 | **0%** vs 3% | - / start ×6 |
| android release rntester | e8a87b5 | 5 vs 59 | **15.1** vs 28.1 | **100%** vs 93% | **0.00** vs 3.32 | **0%** vs 7% | **0.0** vs 5.0 | **0%** vs 3% | - / alert ×4, animated-fade-in-view ×4, appearance ×4 |
| android release templateapp | e8a87b5 | 5 vs 59 | **2.3** vs 2.5 | **100%** vs 92% | **0.00** vs 0.08 | 20% vs **10%** | **0.0** vs 0.1 | **0%** vs 3% | - / start ×5 |
| ios debug rntester | e8a87b5 | 7 vs 59 | **23.8** vs 85.0 | **100%** vs 15% | **0.00** vs 1.47 | **0%** vs 34% | **0.0** vs 23.3 | **0%** vs 3% | - / sectionlist-viewability ×29, scrollview-minindex-maintainvisible ×6, flatlist-viewability ×4 |
| ios debug templateapp | e8a87b5 | 5 vs 56 | **8.6** vs 10.4 | 60% vs **88%** | 0.40 vs **0.12** | 0% vs 0% | 0.4 vs **0.1** | 0% vs 0% | start ×2 / start ×7 |
| ios release rntester | e8a87b5 | 7 vs 59 | **23.6** vs 84.6 | **100%** vs 47% | **0.00** vs 0.63 | **0%** vs 36% | **0.0** vs 24.0 | 0% vs 0% | - / sectionlist-viewability ×30, scrollview-minindex-maintainvisible ×2, modal ×1 |
| ios release templateapp | e8a87b5 | 5 vs 56 | **5.6** vs 9.4 | 100% vs 100% | 0.00 vs 0.00 | 0% vs 0% | 0.0 vs 0.0 | 0% vs 0% | - / - |

Ours on earlier maestro-runner builds:

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing |
|---|---|---|---|---|---|---|---|---|---|
| android debug rntester | 6904d0f | 14 | 11.9 | 86% | 3.57 | 14% | 3.6 | 0% | alert ×2, animated-fade-in-view ×2, appearance ×2 |
| android debug templateapp | 6904d0f | 14 | 2.7 | 100% | 0.00 | 0% | 0.0 | 0% | - |
| android release rntester | 6904d0f | 14 | 15.6 | 93% | 0.07 | 0% | 0.1 | 0% | image-getsize-local-drawables ×1 |
| android release templateapp | 6904d0f | 14 | 2.1 | 93% | 0.07 | 7% | 0.4 | 0% | start ×1 |
| ios debug rntester | 6904d0f | 14 | 22.4 | 86% | 0.14 | 0% | 0.1 | 0% | flatlist-complex-mutations-maintainvisible ×1, image ×1 |
| ios debug templateapp | 6904d0f | 14 | 8.1 | 93% | 0.07 | 0% | 0.1 | 0% | start ×1 |
| ios release rntester | 6904d0f | 14 | 21.5 | 79% | 0.29 | 0% | 0.3 | 0% | flatlist-orientation-maintainvisible ×2, image ×2 |
| ios release templateapp | 6904d0f | 14 | 5.8 | 100% | 0.00 | 0% | 0.0 | 0% | - |

## react-navigation

Each cell: **ours vs upstream**; the better one in bold. Ours is the newest maestro-runner build.

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing (ours / upstream) |
|---|---|---|---|---|---|---|---|---|---|
| android | e8a87b5 | 6 vs 51 | 24.1 vs **23.9** | **100%** vs 69% | **0.00** vs 0.35 | 0% vs 0% | **0.0** vs 0.4 | 0% vs 0% | - / Tab View - Scrollable Tab Bar ×7, Bottom Tabs - Preload Flow ×5, Screen Layout ×2 |
| ios | e8a87b5 | 6 vs 62 | **18.2** vs 23.7 | **100%** vs 61% | **0.00** vs 0.42 | 0% vs 0% | **0.0** vs 0.5 | 0% vs 0% | - / Tab View - Scrollable Tab Bar ×4, Native Stack - Prevent Remove ×4, Screen Layout ×3 |

Ours on earlier maestro-runner builds:

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing |
|---|---|---|---|---|---|---|---|---|---|
| android | 6904d0f | 17 | 26.2 | 82% | 0.24 | 0% | 0.3 | 0% | Tab View - Scrollable Tab Bar ×2, Tab View - Coverflow ×1, Tab View - Custom Tab Bar ×1 |
| ios | 6904d0f | 17 | 19.0 | 82% | 0.18 | 0% | 0.2 | 0% | Screen Layout ×2, Material Top Tabs - Basic ×1 |
