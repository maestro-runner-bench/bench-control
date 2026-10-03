# Retried test cases

Per run, from each job's log: a flow *failed at least once* if any of its attempts failed, inside its job (maestro-runner `--retries`, React Native's iOS per-flow attempts, agent-device, Expo's rounds) or in a retry job (React Native's retry_1/retry_2); it *passed on retry* if it then passed. *Extra flow runs* counts every run of a flow beyond its first, including whole-suite reruns of flows that had passed. Runs whose logs had expired are left out.

## enriched-html

| Platform | Side | Build | Runs | Runs where every flow passed first time | Flows that failed at least once / run (avg, max) | Flows passed only on retry / run | Runs ending with a failed flow | Extra flow runs / run | Runs needing a retry job | Flows / run | Most often failing flows |
|---|---|---|---|---|---|---|---|---|---|---|---|
| android | ours | - | 3 | 0/3 | 29.67, 50 | 0.00 | 3/3 | 0.00 | 0/3 | 50 | checkbox_toggle ×3, extending_paragraph_style_on_paste_after_cut ×3, line_overlapping ×3 |
| android | ours | 49360bb | 1 | 0/1 | 43.00, 43 | 0.00 | 1/1 | 0.00 | 0/1 | 50 | checkbox_toggle ×1, extending_paragraph_style_on_paste_after_copy ×1, extending_paragraph_style_on_paste_after_cut ×1 |
| android | ours | 6904d0f | 4 | 0/4 | 8.50, 10 | 0.00 | 4/4 | 0.00 | 0/4 | 50 | checkbox_toggle ×4, line_overlapping ×4, mention_popup_closing_on_cursor_travel ×4 |
| ios | ours | - | 3 | 0/3 | 19.00, 49 | 0.00 | 3/3 | 0.00 | 0/3 | 49 | image_position_stability ×3, inline_code_paste_into_codeblock ×3, links_visual ×3 |
| ios | ours | 49360bb | 1 | 0/1 | 5.00, 5 | 0.00 | 1/1 | 0.00 | 0/1 | 49 | checkbox_toggle ×1, image_position_stability ×1, inline_code_paste_into_codeblock ×1 |
| ios | ours | 6904d0f | 4 | 0/4 | 4.50, 5 | 0.00 | 4/4 | 0.00 | 0/4 | 49 | image_position_stability ×4, inline_code_paste_into_codeblock ×4, links_visual ×4 |

## expo

| Platform | Side | Build | Runs | Runs where every flow passed first time | Flows that failed at least once / run (avg, max) | Flows passed only on retry / run | Runs ending with a failed flow | Extra flow runs / run | Runs needing a retry job | Flows / run | Most often failing flows |
|---|---|---|---|---|---|---|---|---|---|---|---|
| android | ours | - | 4 | 0/4 | 4.75, 6 | 1.00 | 3/4 | 34.25 | 0/4 | 6 | fullscreen-test ×4, test ×3, picture-in-picture-test.android ×3 |
| android | ours | 6904d0f | 3 | 0/3 | 1.33, 2 | 1.33 | 0/3 | 4.00 | 0/3 | 7 | fullscreen-test ×2, picture-in-picture-test.android ×1, player-output-test ×1 |
| android | upstream | - | 44 | 14/44 | 1.61, 5 | 1.32 | 6/44 | 6.75 | 0/44 | 7 | fullscreen-test ×21, maestro-generated ×17, picture-in-picture-test.android ×17 |
| ios | ours | - | 4 | 1/4 | 1.75, 3 | 0.25 | 3/4 | 3.25 | 0/4 | 4 | test ×4, playback-test ×3, player-output-test ×3 |
| ios | ours | 6904d0f | 2 | 0/2 | 1.00, 1 | 1.00 | 0/2 | 1.00 | 0/2 | 5 | test ×1, playback-test ×1 |
| ios | upstream | - | 40 | 20/40 | 0.85, 4 | 0.70 | 9/40 | 1.35 | 0/40 | 5 | fullscreen-test ×17, test ×9, playback-test ×8 |

## pager-view

| Platform | Side | Build | Runs | Runs where every flow passed first time | Flows that failed at least once / run (avg, max) | Flows passed only on retry / run | Runs ending with a failed flow | Extra flow runs / run | Runs needing a retry job | Flows / run | Most often failing flows |
|---|---|---|---|---|---|---|---|---|---|---|---|
| android | ours | 49360bb | 1 | 0/1 | 8.00, 8 | 0.00 | 1/1 | 16.00 | 0/1 | 16 | nested_pagerView_example ×1, ensure-ltr ×1, ensure-rtl ×1 |
| android | ours | 6904d0f | 3 | 0/3 | 8.33, 9 | 0.33 | 3/3 | 16.33 | 0/3 | 16 | nested_pagerView_example ×3, ensure-ltr ×3, ensure-rtl ×3 |
| ios | ours | 6904d0f | 4 | 0/4 | 3.00, 3 | 0.00 | 4/4 | 6.00 | 0/4 | 16 | ensure-ltr ×4, ensure-rtl ×4, verify-horizontal-rtl-swipe ×4 |

## react-native

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

## react-navigation

| Platform | Side | Build | Runs | Runs where every flow passed first time | Flows that failed at least once / run (avg, max) | Flows passed only on retry / run | Runs ending with a failed flow | Extra flow runs / run | Runs needing a retry job | Flows / run | Most often failing flows |
|---|---|---|---|---|---|---|---|---|---|---|---|
| android | ours | - | 2 | 2/2 | 0.00, 0 | 0.00 | 0/2 | 0.00 | 0/2 | 39 | - |
| android | ours | 6904d0f | 3 | 3/3 | 0.00, 0 | 0.00 | 0/3 | 0.00 | 0/3 | 39 | - |
| android | ours | d51beed | 2 | 2/2 | 0.00, 0 | 0.00 | 0/2 | 0.00 | 0/2 | 10 | - |
| android | upstream | - | 47 | 31/47 | 0.38, 2 | 0.38 | 0/47 | 0.45 | 0/47 | 39 | Tab View - Scrollable Tab Bar ×7, Bottom Tabs - Preload Flow ×5, Screen Layout ×2 |
| ios | ours | - | 3 | 2/3 | 0.33, 1 | 0.33 | 0/3 | 0.33 | 0/3 | 39 | Screen Layout ×1 |
| ios | ours | 6904d0f | 3 | 2/3 | 0.33, 1 | 0.33 | 0/3 | 0.33 | 0/3 | 39 | Material Top Tabs - Basic ×1 |
| ios | upstream | - | 31 | 19/31 | 0.42, 2 | 0.42 | 0/31 | 0.48 | 0/31 | 39 | Screen Layout ×3, Tab View - Scrollable Tab Bar ×3, Stack - Prevent Remove ×2 |
