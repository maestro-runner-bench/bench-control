# Retried test cases

Per run, from each job's log: a flow *failed at least once* if any of its attempts failed, inside its job (maestro-runner `--retries`, React Native's iOS per-flow attempts, agent-device, Expo's rounds) or in a retry job (React Native's retry_1/retry_2); it *passed on retry* if it then passed. *Extra flow runs* counts every run of a flow beyond its first, including whole-suite reruns of flows that had passed. Runs whose logs had expired are left out.

## enriched-html

Each cell: **ours vs upstream**; the better one in bold. Ours is the newest maestro-runner build.

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing (ours / upstream) |
|---|---|---|---|---|---|---|---|---|---|
| android | 6904d0f | 16 | 29.5 | 0% | 8.62 | 0% | 0.0 | 100% | checkbox_toggle ×16, line_overlapping ×16, mention_popup_closing_on_cursor_travel ×16 / - |
| ios | 6904d0f | 4 | 29.5 | 0% | 4.50 | 0% | 0.0 | 100% | image_position_stability ×4, inline_code_paste_into_codeblock ×4, links_visual ×4 / - |

## expo

Each cell: **ours vs upstream**; the better one in bold. Ours is the newest maestro-runner build.

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing (ours / upstream) |
|---|---|---|---|---|---|---|---|---|---|
| android | 6904d0f | 6 vs 44 | **12.4** vs 14.9 | 0% vs **32%** | **1.50** vs 1.61 | 0% vs 0% | **4.3** vs 6.8 | **0%** vs 14% | fullscreen-test ×5, picture-in-picture-test.android ×2, maestro-generated ×1 / fullscreen-test ×21, maestro-generated ×17, picture-in-picture-test.android ×17 |
| ios | 6904d0f | 5 vs 40 | **9.6** vs 15.5 | 20% vs **50%** | **0.80** vs 0.85 | 0% vs 0% | **0.8** vs 1.4 | **0%** vs 22% | fullscreen-test ×2, test ×1, playback-test ×1 / fullscreen-test ×17, test ×9, playback-test ×8 |

## pager-view

Each cell: **ours vs upstream**; the better one in bold. Ours is the newest maestro-runner build.

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing (ours / upstream) |
|---|---|---|---|---|---|---|---|---|---|
| android | 6904d0f | 14 | 19.8 | 0% | 8.21 | 0% | 16.1 | 100% | ensure-ltr ×14, ensure-rtl ×14, verify-horizontal-rtl-swipe ×14 / - |
| ios | 6904d0f | 15 | 8.8 | 0% | 3.07 | 0% | 6.1 | 100% | ensure-ltr ×15, ensure-rtl ×15, verify-horizontal-rtl-swipe ×15 / - |

## react-native

Each cell: **ours vs upstream**; the better one in bold. Ours is the newest maestro-runner build.

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing (ours / upstream) |
|---|---|---|---|---|---|---|---|---|---|
| android debug rntester | 6904d0f | 12 vs 59 | **11.9** vs 18.9 | 83% vs **93%** | 4.17 vs **1.69** | 17% vs **8%** | 4.2 vs **2.5** | **0%** vs 3% | alert ×2, animated-fade-in-view ×2, appearance ×2 / alert ×4, animated-fade-in-view ×4, appearance ×4 |
| android debug templateapp | 6904d0f | 12 vs 59 | **2.7** vs 3.3 | **100%** vs 90% | **0.00** vs 0.10 | **0%** vs 10% | **0.0** vs 0.1 | **0%** vs 3% | - / start ×6 |
| android release rntester | 6904d0f | 12 vs 59 | **15.6** vs 28.1 | **100%** vs 93% | **0.00** vs 3.32 | **0%** vs 7% | **0.0** vs 5.0 | **0%** vs 3% | - / alert ×4, animated-fade-in-view ×4, appearance ×4 |
| android release templateapp | 6904d0f | 12 vs 59 | **2.1** vs 2.5 | 92% vs 92% | 0.08 vs 0.08 | **8%** vs 10% | 0.4 vs **0.1** | **0%** vs 3% | start ×1 / start ×5 |
| ios debug rntester | 6904d0f | 12 vs 59 | **22.0** vs 85.0 | **83%** vs 15% | **0.17** vs 1.47 | **0%** vs 34% | **0.2** vs 23.3 | **0%** vs 3% | flatlist-complex-mutations-maintainvisible ×1, image ×1 / sectionlist-viewability ×29, scrollview-minindex-maintainvisible ×6, flatlist-viewability ×4 |
| ios debug templateapp | 6904d0f | 12 vs 56 | **8.1** vs 10.4 | **92%** vs 88% | **0.08** vs 0.12 | 0% vs 0% | 0.1 vs 0.1 | 0% vs 0% | start ×1 / start ×7 |
| ios release rntester | 6904d0f | 12 vs 59 | **21.6** vs 84.6 | **83%** vs 47% | **0.17** vs 0.63 | **0%** vs 36% | **0.2** vs 24.0 | 0% vs 0% | image ×1, flatlist-orientation-maintainvisible ×1 / sectionlist-viewability ×30, scrollview-minindex-maintainvisible ×2, modal ×1 |
| ios release templateapp | 6904d0f | 12 vs 56 | **6.0** vs 9.4 | 100% vs 100% | 0.00 vs 0.00 | 0% vs 0% | 0.0 vs 0.0 | 0% vs 0% | - / - |

## react-navigation

Each cell: **ours vs upstream**; the better one in bold. Ours is the newest maestro-runner build.

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing (ours / upstream) |
|---|---|---|---|---|---|---|---|---|---|
| android | 6904d0f | 15 vs 48 | 25.8 vs **23.7** | **80%** vs 67% | **0.27** vs 0.38 | 0% vs 0% | **0.3** vs 0.4 | 0% vs 0% | Tab View - Scrollable Tab Bar ×2, Tab View - Coverflow ×1, Tab View - Custom Tab Bar ×1 / Tab View - Scrollable Tab Bar ×7, Bottom Tabs - Preload Flow ×5, Screen Layout ×2 |
| ios | 6904d0f | 15 vs 32 | **19.0** vs 24.8 | **80%** vs 62% | **0.20** vs 0.41 | 0% vs 0% | **0.2** vs 0.5 | 0% vs 0% | Screen Layout ×2, Material Top Tabs - Basic ×1 / Screen Layout ×3, Tab View - Scrollable Tab Bar ×3, Stack - Prevent Remove ×2 |
