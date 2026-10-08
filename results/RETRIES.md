# Retried test cases

Per run, from each job's log: a flow *failed at least once* if any of its attempts failed, inside its job (maestro-runner `--retries`, React Native's iOS per-flow attempts, agent-device, Expo's rounds) or in a retry job (React Native's retry_1/retry_2); it *passed on retry* if it then passed. *Extra flow runs* counts every run of a flow beyond its first, including whole-suite reruns of flows that had passed. Runs whose logs had expired are left out.

## enriched-html

Each cell: **ours vs upstream**; the better one in bold. Ours is the newest maestro-runner build.

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing (ours / upstream) |
|---|---|---|---|---|---|---|---|---|---|
| android | e8a87b5 | 22 | 29.1 | 0% | 8.73 | 0% | 0.0 | 100% | checkbox_toggle ×22, line_overlapping ×22, mention_popup_closing_on_cursor_travel ×22 / - |
| ios | 6904d0f | 4 | 29.5 | 0% | 4.50 | 0% | 0.0 | 100% | image_position_stability ×4, inline_code_paste_into_codeblock ×4, links_visual ×4 / - |

Ours on earlier maestro-runner builds:

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing |
|---|---|---|---|---|---|---|---|---|---|
| android | 6904d0f | 18 | 29.6 | 0% | 8.67 | 0% | 0.0 | 100% | checkbox_toggle ×18, line_overlapping ×18, mention_popup_closing_on_cursor_travel ×18 |

## expo

Each cell: **ours vs upstream**; the better one in bold. Ours is the newest maestro-runner build.

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing (ours / upstream) |
|---|---|---|---|---|---|---|---|---|---|
| android | e8a87b5 | 20 vs 59 | 28.2 vs **15.4** | 15% vs **27%** | 4.35 vs **2.05** | 0% vs 0% | 33.8 vs **10.5** | 70% vs **20%** | fullscreen-test ×15, test ×14, picture-in-picture-test.android ×14 / fullscreen-test ×32, picture-in-picture-test.android ×25, maestro-generated ×21 |
| ios | e8a87b5 | 19 vs 50 | **11.2** vs 16.0 | **68%** vs 46% | **0.32** vs 0.82 | 0% vs 0% | **0.3** vs 1.2 | **0%** vs 18% | fullscreen-test ×4, test ×2 / fullscreen-test ×24, test ×9, playback-test ×8 |

Ours on earlier maestro-runner builds:

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing |
|---|---|---|---|---|---|---|---|---|---|
| android | 6904d0f | 6 | 12.4 | 0% | 1.50 | 0% | 4.3 | 0% | fullscreen-test ×5, picture-in-picture-test.android ×2, maestro-generated ×1 |
| ios | 6904d0f | 5 | 9.6 | 20% | 0.80 | 0% | 0.8 | 0% | fullscreen-test ×2, test ×1, playback-test ×1 |

## pager-view

Each cell: **ours vs upstream**; the better one in bold. Ours is the newest maestro-runner build.

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing (ours / upstream) |
|---|---|---|---|---|---|---|---|---|---|
| android | e8a87b5 | 17 | 20.0 | 0% | 8.65 | 0% | 17.1 | 100% | nested_pagerView_example ×17, ensure-ltr ×17, ensure-rtl ×17 / - |
| ios | e8a87b5 | 18 | 10.1 | 0% | 3.17 | 0% | 6.1 | 100% | ensure-rtl ×18, verify-horizontal-rtl-swipe ×18, ensure-ltr ×16 / - |

Ours on earlier maestro-runner builds:

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing |
|---|---|---|---|---|---|---|---|---|---|
| android | 6904d0f | 16 | 19.8 | 0% | 8.19 | 0% | 16.1 | 100% | ensure-ltr ×16, ensure-rtl ×16, verify-horizontal-rtl-swipe ×16 |
| ios | 6904d0f | 17 | 8.8 | 0% | 3.06 | 0% | 6.1 | 100% | ensure-ltr ×17, ensure-rtl ×17, verify-horizontal-rtl-swipe ×17 |

## react-native

Each cell: **ours vs upstream**; the better one in bold. Ours is the newest maestro-runner build.

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing (ours / upstream) |
|---|---|---|---|---|---|---|---|---|---|
| android debug rntester | e8a87b5 | 18 vs 89 | **11.5** vs 18.8 | 94% vs **96%** | 1.39 vs **1.12** | **0%** vs 6% | **0.0** vs 1.7 | 6% vs **2%** | alert ×1, animated-fade-in-view ×1, appearance ×1 / alert ×4, animated-fade-in-view ×4, appearance ×4 |
| android debug templateapp | e8a87b5 | 18 vs 88 | **2.7** vs 3.3 | **94%** vs 92% | **0.06** vs 0.08 | **6%** vs 8% | 0.3 vs **0.1** | **0%** vs 2% | start ×1 / start ×7 |
| android release rntester | e8a87b5 | 18 vs 89 | **15.1** vs 28.1 | **100%** vs 92% | **0.00** vs 3.85 | **0%** vs 8% | **0.0** vs 5.0 | **0%** vs 2% | - / alert ×7, animated-fade-in-view ×7, appearance ×7 |
| android release templateapp | e8a87b5 | 18 vs 88 | **2.2** vs 2.5 | **100%** vs 93% | **0.00** vs 0.07 | **6%** vs 8% | **0.0** vs 0.1 | **0%** vs 2% | - / start ×6 |
| ios debug rntester | e8a87b5 | 21 vs 88 | **26.8** vs 83.4 | **71%** vs 16% | 3.81 vs **1.35** | **19%** vs 39% | 61.9 vs **20.6** | 19% vs **15%** | flatlist-append-maintainvisible ×4, flatlist-delete-anchor-maintainvisible ×4, flatlist-empty-list-maintainvisible ×4 / sectionlist-viewability ×35, flatlist-append-maintainvisible ×11, scrollview-minindex-maintainvisible ×7 |
| ios debug templateapp | e8a87b5 | 18 vs 85 | **8.4** vs 10.4 | 83% vs **88%** | 0.17 vs **0.12** | 0% vs 0% | 0.2 vs **0.1** | 0% vs 0% | start ×3 / start ×10 |
| ios release rntester | e8a87b5 | 21 vs 88 | **23.8** vs 81.6 | **76%** vs 44% | 3.67 vs **0.65** | **19%** vs 40% | 61.8 vs **21.0** | 19% vs **12%** | flatlist-horizontal-inverted-recycle-maintainvisible ×5, flatlist-append-maintainvisible ×4, flatlist-delete-anchor-maintainvisible ×4 / sectionlist-viewability ×37, flatlist-append-maintainvisible ×11, scrollview-minindex-maintainvisible ×2 |
| ios release templateapp | e8a87b5 | 18 vs 85 | **6.3** vs 9.5 | 100% vs 100% | 0.00 vs 0.00 | 0% vs 0% | 0.0 vs 0.0 | 0% vs 0% | - / - |

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
| android | e8a87b5 | 20 vs 54 | 25.4 vs **23.9** | **90%** vs 70% | **0.10** vs 0.33 | 0% vs 0% | **0.1** vs 0.4 | 0% vs 0% | Tab View - Custom Tab Bar ×1, Showcase - Material Top Tabs ×1 / Tab View - Scrollable Tab Bar ×7, Bottom Tabs - Preload Flow ×5, Screen Layout ×2 |
| ios | e8a87b5 | 20 vs 67 | **18.3** vs 24.0 | **90%** vs 60% | **0.10** vs 0.45 | 0% vs 0% | **0.1** vs 0.5 | 0% vs 0% | Auth Flow ×2 / Tab View - Scrollable Tab Bar ×4, Native Stack - Prevent Remove ×4, Screen Layout ×3 |

Ours on earlier maestro-runner builds:

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing |
|---|---|---|---|---|---|---|---|---|---|
| android | 6904d0f | 17 | 26.2 | 82% | 0.24 | 0% | 0.3 | 0% | Tab View - Scrollable Tab Bar ×2, Tab View - Coverflow ×1, Tab View - Custom Tab Bar ×1 |
| ios | 6904d0f | 17 | 19.0 | 82% | 0.18 | 0% | 0.2 | 0% | Screen Layout ×2, Material Top Tabs - Basic ×1 |
