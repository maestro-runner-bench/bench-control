# enriched-html

Upstream has no e2e CI to compare against.

Times in minutes. *Run* is the whole workflow run (builds included); *job* is one job; *tests* is its test step only; *queue* is the wait for a runner.

## Summary

| Project | Platform | Flavour | Side | Build | Runs | Median e2e (min) | Green runs | Runs with no first-attempt failure | First-attempt failures / run | Final failures / run | Runs needing a retry job | Runner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| enriched-html | android | - | ours | e8a87b5 | 23 | 29.1 | 0/23 | 0/22 | 8.68 | 6.73 | 0/23 | ubuntu-latest |
| enriched-html | android | - | ours | 6904d0f | 18 | 29.4 | 0/18 | 0/18 | 8.67 | 7.00 | 0/18 | ubuntu-latest |
| enriched-html | ios | - | ours | e8a87b5 | 23 | 3.4 | 0/23 | - | - | - | 0/23 | macos-26 |
| enriched-html | ios | - | ours | 6904d0f | 18 | 3.9 | 0/18 | 0/4 | 4.50 | 2.50 | 0/18 | macos-26 |

## Runs: maestro-runner (bench fork)

| Started (UTC) | Run | Build | Run time | Job | Job time | Tests | Queue | Result |
|---|---|---|---|---|---|---|---|---|
| 2026-10-07 21:57 | [37693022526](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37693022526) | e8a87b5 | 31.0 | e2e-android | 30.9 | 30.2 | 0.0 | 40/49, 2 passed on retry |
|  | | |  | e2e-ios | 6.3 | 3.0 | 0.1 | failure |
| 2026-10-07 16:47 | [37654749259](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37654749259) | e8a87b5 | 6.9 | e2e-android | 6.7 | 5.2 | 0.0 | failure |
|  | | |  | e2e-ios | 5.8 | 3.4 | 0.1 | failure |
| 2026-10-07 11:31 | [37614619119](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37614619119) | e8a87b5 | 25.5 | e2e-android | 21.2 | 20.6 | 0.0 | 42/49, 2 passed on retry |
|  | | |  | e2e-ios | 5.3 | 2.9 | 20.1 | failure |
| 2026-10-07 06:09 | [37580028484](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37580028484) | e8a87b5 | 29.7 | e2e-android | 29.6 | 29.0 | 0.0 | 43/49, 2 passed on retry |
|  | | |  | e2e-ios | 6.5 | 4.2 | 0.1 | failure |
| 2026-10-07 03:40 | [37567802301](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37567802301) | e8a87b5 | 30.9 | e2e-android | 30.9 | 30.1 | 0.0 | 42/49, 2 passed on retry |
|  | | |  | e2e-ios | 8.1 | 3.2 | 0.2 | failure |
| 2026-10-07 01:04 | [37555296454](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37555296454) | e8a87b5 | 30.5 | e2e-android | 30.4 | 29.7 | 0.1 | 42/49, 2 passed on retry |
|  | | |  | e2e-ios | 7.6 | 5.2 | 0.1 | failure |
| 2026-10-06 22:35 | [37541526189](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37541526189) | e8a87b5 | 29.4 | e2e-android | 29.3 | 28.6 | 0.0 | 41/49, 2 passed on retry |
|  | | |  | e2e-ios | 7.0 | 4.3 | 0.2 | failure |
| 2026-10-06 19:49 | [37521781480](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37521781480) | e8a87b5 | 31.1 | e2e-android | 31.1 | 30.3 | 0.0 | 40/49, 1 passed on retry |
|  | | |  | e2e-ios | 7.4 | 2.7 | 0.2 | failure |
| 2026-10-06 19:49 | [37521781643](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37521781643) | e8a87b5 | 30.0 | e2e-android | 29.9 | 29.1 | 0.1 | 42/49, 2 passed on retry |
|  | | |  | e2e-ios | 6.0 | 3.3 | 0.2 | failure |
| 2026-10-06 16:58 | [37499888106](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37499888106) | e8a87b5 | 30.5 | e2e-android | 30.4 | 29.7 | 0.0 | 42/49, 2 passed on retry |
|  | | |  | e2e-ios | 5.6 | 3.5 | 0.2 | failure |
| 2026-10-06 14:01 | [37475495516](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37475495516) | e8a87b5 | 30.7 | e2e-android | 30.6 | 29.9 | 0.0 | 44/49, 2 passed on retry |
|  | | |  | e2e-ios | 6.7 | 4.5 | 0.1 | failure |
| 2026-10-06 11:10 | [37454639812](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37454639812) | e8a87b5 | 30.3 | e2e-android | 30.2 | 29.6 | 0.0 | 42/49, 2 passed on retry |
|  | | |  | e2e-ios | 3.8 | 2.1 | 9.4 | failure |
| 2026-10-06 08:24 | [37435931809](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37435931809) | e8a87b5 | 30.0 | e2e-android | 29.9 | 29.1 | 0.1 | 42/49, 2 passed on retry |
|  | | |  | e2e-ios | 6.0 | 2.8 | 0.1 | failure |
| 2026-10-06 05:54 | [37420931877](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37420931877) | e8a87b5 | 22.6 | e2e-android | 22.6 | 21.8 | 0.0 | 43/49, 2 passed on retry |
|  | | |  | e2e-ios | 6.1 | 3.3 | 0.2 | failure |
| 2026-10-06 03:15 | [37408094968](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37408094968) | e8a87b5 | 25.9 | e2e-android | 25.8 | 24.9 | 0.0 | 42/49, 2 passed on retry |
|  | | |  | e2e-ios | 8.0 | 4.9 | 0.1 | failure |
| 2026-10-06 00:45 | [37395610455](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37395610455) | e8a87b5 | 29.9 | e2e-android | 29.9 | 29.1 | 0.1 | 43/49, 2 passed on retry |
|  | | |  | e2e-ios | 5.4 | 2.9 | 0.2 | failure |
| 2026-10-05 22:19 | [37381768703](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37381768703) | e8a87b5 | 21.3 | e2e-android | 21.1 | 20.5 | 0.0 | 43/49, 2 passed on retry |
|  | | |  | e2e-ios | 7.5 | 5.2 | 0.2 | failure |
| 2026-10-05 20:35 | [37370721142](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37370721142) | - | 15.1 | e2e-android | 15.0 | - | 0.0 | cancelled before tests |
|  | | |  | e2e-ios | 15.0 | - | 0.0 | cancelled before tests |
| 2026-10-05 19:01 | [37360409858](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37360409858) | e8a87b5 | 31.0 | e2e-android | 30.9 | 30.2 | 0.1 | 44/49, 2 passed on retry |
|  | | |  | e2e-ios | 6.6 | 4.5 | 0.2 | failure |
| 2026-10-05 15:55 | [37336677288](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37336677288) | e8a87b5 | 30.2 | e2e-android | 30.2 | 29.6 | 0.0 | 43/49, 2 passed on retry |
|  | | |  | e2e-ios | 7.0 | 3.2 | 0.1 | failure |
| 2026-10-05 12:59 | [37313344060](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37313344060) | e8a87b5 | 22.1 | e2e-android | 22.1 | 21.4 | 0.0 | 42/49, 2 passed on retry |
|  | | |  | e2e-ios | 5.8 | 3.8 | 0.1 | failure |
| 2026-10-05 12:59 | [37313343268](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37313343268) | e8a87b5 | 23.6 | e2e-android | 23.6 | 22.9 | 0.0 | 43/49, 2 passed on retry |
|  | | |  | e2e-ios | 5.6 | 1.9 | 0.2 | failure |
| 2026-10-05 09:27 | [37290128409](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37290128409) | e8a87b5 | 29.6 | e2e-android | 29.5 | 28.8 | 0.1 | 44/49, 2 passed on retry |
|  | | |  | e2e-ios | 8.3 | 5.0 | 7.4 | failure |
| 2026-10-05 06:01 | [37270361067](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37270361067) | e8a87b5 | 24.8 | e2e-android | 24.7 | 24.0 | 0.0 | 41/49, 2 passed on retry |
|  | | |  | e2e-ios | 6.7 | 3.8 | 0.1 | failure |
| 2026-10-05 05:15 | [37267000881](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37267000881) | 6904d0f | 31.4 | e2e-android | 31.3 | 30.7 | 0.0 | 42/49, 2 passed on retry |
|  | | |  | e2e-ios | 4.3 | 2.5 | 0.1 | failure |
| 2026-10-05 03:12 | [37258519516](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37258519516) | 6904d0f | 30.5 | e2e-android | 30.4 | 29.8 | 0.0 | 42/49, 2 passed on retry |
|  | | |  | e2e-ios | 5.5 | 3.2 | 0.1 | failure |
| 2026-10-05 01:04 | [37249950607](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37249950607) | 6904d0f | 30.2 | e2e-android | 30.1 | 29.4 | 0.0 | 41/49, 2 passed on retry |
|  | | |  | e2e-ios | 3.9 | 2.4 | 0.1 | failure |
| 2026-10-04 23:01 | [37242209804](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37242209804) | 6904d0f | 30.0 | e2e-android | 29.9 | 29.1 | 0.1 | 42/49, 2 passed on retry |
|  | | |  | e2e-ios | 6.0 | 3.0 | 0.1 | failure |
| 2026-10-04 21:13 | [37235202377](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37235202377) | 6904d0f | 29.7 | e2e-android | 29.6 | 28.9 | 0.1 | 43/49, 2 passed on retry |
|  | | |  | e2e-ios | 6.0 | 3.2 | 0.1 | failure |
| 2026-10-04 19:09 | [37227189106](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37227189106) | 6904d0f | 29.9 | e2e-android | 29.8 | 29.2 | 0.1 | 44/49, 2 passed on retry |
|  | | |  | e2e-ios | 3.9 | 1.6 | 0.1 | failure |
| 2026-10-04 17:06 | [37219236188](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37219236188) | 6904d0f | 27.2 | e2e-android | 27.1 | 26.4 | 0.0 | 42/49, 2 passed on retry |
|  | | |  | e2e-ios | 8.1 | 5.8 | 0.1 | failure |
| 2026-10-04 15:02 | [37211542183](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37211542183) | 6904d0f | 30.7 | e2e-android | 30.4 | 29.7 | 0.2 | 43/49, 2 passed on retry |
|  | | |  | e2e-ios | 7.6 | 3.7 | 0.1 | failure |
| 2026-10-04 12:39 | [37202868394](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37202868394) | 6904d0f | 31.2 | e2e-android | 31.1 | 30.4 | 0.1 | 41/49, 2 passed on retry |
|  | | |  | e2e-ios | 8.1 | 4.5 | 0.1 | failure |
| 2026-10-04 10:16 | [37194819023](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37194819023) | 6904d0f | 29.8 | e2e-android | 29.7 | 29.0 | 0.1 | 44/49, 2 passed on retry |
|  | | |  | e2e-ios | 5.2 | 3.0 | 0.1 | failure |
| 2026-10-04 08:12 | [37188173907](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37188173907) | 6904d0f | 30.4 | e2e-android | 30.3 | 29.7 | 0.0 | 43/49, 2 passed on retry |
|  | | |  | e2e-ios | 4.7 | 3.1 | 2.2 | failure |
| 2026-10-04 06:41 | [37183542307](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37183542307) | 6904d0f | 90.2 | e2e-android | 90.2 | 89.5 | 0.0 | cancelled during tests (time limit or by hand) |
|  | | |  | e2e-ios | 7.4 | 4.2 | 0.4 | failure |
| 2026-10-04 05:30 | [37180071707](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37180071707) | 6904d0f | 30.5 | e2e-android | 30.4 | 29.8 | 0.0 | 39/49, 2 passed on retry |
|  | | |  | e2e-ios | 6.3 | 4.2 | 0.1 | failure |
| 2026-10-03 18:40 | [37145059263](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37145059263) | 6904d0f | 22.5 | e2e-android | 22.4 | 21.8 | 0.0 | 42/49, 2 passed on retry |
|  | | |  | e2e-ios | 7.3 | 4.8 | 0.2 | failure |
| 2026-10-03 14:53 | [37131276940](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37131276940) | 6904d0f | 34.9 | e2e-android | 24.2 | 23.5 | 0.0 | 43/49, 2 passed on retry |
|  | | |  | e2e-ios | 34.6 | 29.6 | 0.2 | 45/48, 2 passed on retry |
| 2026-10-03 10:23 | [37116239902](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37116239902) | 6904d0f | 30.2 | e2e-android | 30.1 | 29.6 | 0.0 | 44/49, 2 passed on retry |
|  | | |  | e2e-ios | 24.3 | 21.1 | 0.1 | 45/48, 2 passed on retry |
| 2026-10-02 23:32 | [37078043564](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37078043564) | 6904d0f | 90.3 | e2e-android | 90.2 | 89.3 | 0.0 | cancelled during tests (time limit or by hand) |
|  | | |  | e2e-ios | 33.3 | 29.4 | 0.3 | 46/48, 2 passed on retry |
| 2026-10-02 20:05 | [37058371404](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37058371404) | 6904d0f | 90.2 | e2e-android | 90.1 | 89.4 | 0.0 | cancelled during tests (time limit or by hand) |
|  | | |  | e2e-ios | 45.1 | 38.7 | 0.1 | 46/48, 2 passed on retry |

## Trend

![enriched-html-android](charts/enriched-html-android.svg)

![enriched-html-ios](charts/enriched-html-ios.svg)


## Retried test cases

Per run, from each job's log: a flow *failed at least once* if any of its attempts failed, inside its job (maestro-runner `--retries`, React Native's iOS per-flow attempts, agent-device, Expo's rounds) or in a retry job (React Native's retry_1/retry_2); it *passed on retry* if it then passed. *Extra flow runs* counts every run of a flow beyond its first, including whole-suite reruns of flows that had passed. Runs whose logs had expired are left out.

Each cell: **ours vs upstream**; the better one in bold. Ours is the newest maestro-runner build.

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing (ours / upstream) |
|---|---|---|---|---|---|---|---|---|---|
| android | e8a87b5 | 22 | 29.1 | 0% | 8.73 | 0% | 0.0 | 100% | checkbox_toggle ×22, line_overlapping ×22, mention_popup_closing_on_cursor_travel ×22 / - |
| ios | 6904d0f | 4 | 29.5 | 0% | 4.50 | 0% | 0.0 | 100% | image_position_stability ×4, inline_code_paste_into_codeblock ×4, links_visual ×4 / - |

Ours on earlier maestro-runner builds:

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing |
|---|---|---|---|---|---|---|---|---|---|
| android | 6904d0f | 18 | 29.6 | 0% | 8.67 | 0% | 0.0 | 100% | checkbox_toggle ×18, line_overlapping ×18, mention_popup_closing_on_cursor_travel ×18 |

### Per run

| Started (UTC) | Run | Platform | Side | Build | Flows | Failed at least once | Passed on retry (failed attempts) | Failed at the end | Extra flow runs | Retry jobs |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-07 21:57 | [37693022526](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37693022526) | android | ours | e8a87b5 | 50 | 11 | - | checkbox_toggle, extending_paragraph_style_on_paste_after_copy, extending_paragraph_style_on_paste_after_cut, inline_code_paste_into_codeblock, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, custom_styles_display, ellipsize_mode | 0 | 0 |
| 2026-10-07 11:31 | [37614619119](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37614619119) | android | ours | e8a87b5 | 50 | 9 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, alignment_visual, custom_styles_display, ellipsize_mode | 0 | 0 |
| 2026-10-07 06:09 | [37580028484](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37580028484) | android | ours | e8a87b5 | 50 | 8 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, custom_styles_display, ellipsize_mode | 0 | 0 |
| 2026-10-07 03:40 | [37567802301](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37567802301) | android | ours | e8a87b5 | 50 | 9 | - | checkbox_toggle, line_overlapping, links_visual, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, custom_styles_display, ellipsize_mode | 0 | 0 |
| 2026-10-07 01:04 | [37555296454](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37555296454) | android | ours | e8a87b5 | 50 | 9 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, alignment_visual, custom_styles_display, ellipsize_mode | 0 | 0 |
| 2026-10-06 22:35 | [37541526189](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37541526189) | android | ours | e8a87b5 | 50 | 10 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, scrolling_after_typing, alignment_visual, ellipsize_mode, empty_list_elements_display | 0 | 0 |
| 2026-10-06 19:49 | [37521781480](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37521781480) | android | ours | e8a87b5 | 50 | 11 | - | checkbox_toggle, extending_paragraph_style_on_paste_after_copy, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, custom_styles_display, ellipsize_mode, paragraph_styles_display, font_scaling | 0 | 0 |
| 2026-10-06 19:49 | [37521781643](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37521781643) | android | ours | e8a87b5 | 50 | 9 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, ellipsize_mode, empty_list_elements_display, paragraph_styles_display | 0 | 0 |
| 2026-10-06 16:58 | [37499888106](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37499888106) | android | ours | e8a87b5 | 50 | 9 | - | checkbox_toggle, extending_paragraph_style_on_paste_after_cut, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, custom_styles_display, ellipsize_mode | 0 | 0 |
| 2026-10-06 14:01 | [37475495516](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37475495516) | android | ours | e8a87b5 | 50 | 7 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, ellipsize_mode | 0 | 0 |
| 2026-10-06 11:10 | [37454639812](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37454639812) | android | ours | e8a87b5 | 50 | 9 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, custom_styles_display, ellipsize_mode, paragraph_styles_display | 0 | 0 |
| 2026-10-06 08:24 | [37435931809](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37435931809) | android | ours | e8a87b5 | 50 | 9 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, custom_styles_display, ellipsize_mode, empty_list_elements_display | 0 | 0 |
| 2026-10-06 05:54 | [37420931877](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37420931877) | android | ours | e8a87b5 | 50 | 8 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, custom_styles_display, ellipsize_mode | 0 | 0 |
| 2026-10-06 03:15 | [37408094968](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37408094968) | android | ours | e8a87b5 | 50 | 9 | - | checkbox_toggle, extending_paragraph_style_on_paste_after_copy, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, custom_styles_display, ellipsize_mode | 0 | 0 |
| 2026-10-06 00:45 | [37395610455](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37395610455) | android | ours | e8a87b5 | 50 | 8 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, alignment_visual, ellipsize_mode | 0 | 0 |
| 2026-10-05 22:19 | [37381768703](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37381768703) | android | ours | e8a87b5 | 50 | 8 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, custom_styles_display, ellipsize_mode | 0 | 0 |
| 2026-10-05 19:01 | [37360409858](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37360409858) | android | ours | e8a87b5 | 50 | 7 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, ellipsize_mode | 0 | 0 |
| 2026-10-05 15:55 | [37336677288](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37336677288) | android | ours | e8a87b5 | 50 | 8 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, custom_styles_display, ellipsize_mode | 0 | 0 |
| 2026-10-05 12:59 | [37313344060](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37313344060) | android | ours | e8a87b5 | 50 | 9 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, alignment_visual, custom_styles_display, ellipsize_mode | 0 | 0 |
| 2026-10-05 12:59 | [37313343268](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37313343268) | android | ours | e8a87b5 | 50 | 8 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, custom_styles_display, ellipsize_mode | 0 | 0 |
| 2026-10-05 09:27 | [37290128409](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37290128409) | android | ours | e8a87b5 | 50 | 7 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, ellipsize_mode | 0 | 0 |
| 2026-10-05 06:01 | [37270361067](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37270361067) | android | ours | e8a87b5 | 50 | 10 | - | checkbox_toggle, extending_paragraph_style_on_paste_after_cut, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, alignment_visual, custom_styles_display, ellipsize_mode | 0 | 0 |
| 2026-10-05 05:15 | [37267000881](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37267000881) | android | ours | 6904d0f | 50 | 9 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, custom_styles_display, ellipsize_mode, empty_list_elements_display | 0 | 0 |
| 2026-10-05 03:12 | [37258519516](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37258519516) | android | ours | 6904d0f | 50 | 9 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, custom_styles_display, ellipsize_mode, paragraph_styles_display | 0 | 0 |
| 2026-10-05 01:04 | [37249950607](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37249950607) | android | ours | 6904d0f | 50 | 10 | - | checkbox_toggle, inline_styles_removal, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, custom_styles_display, ellipsize_mode, paragraph_styles_display | 0 | 0 |
| 2026-10-04 23:01 | [37242209804](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37242209804) | android | ours | 6904d0f | 50 | 9 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, custom_styles_display, ellipsize_mode, paragraph_styles_display | 0 | 0 |
| 2026-10-04 21:13 | [37235202377](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37235202377) | android | ours | 6904d0f | 50 | 8 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, custom_styles_display, ellipsize_mode | 0 | 0 |
| 2026-10-04 19:09 | [37227189106](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37227189106) | android | ours | 6904d0f | 50 | 7 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, ellipsize_mode | 0 | 0 |
| 2026-10-04 17:06 | [37219236188](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37219236188) | android | ours | 6904d0f | 50 | 9 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, alignment_visual, ellipsize_mode, empty_list_elements_display | 0 | 0 |
| 2026-10-04 15:02 | [37211542183](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37211542183) | android | ours | 6904d0f | 50 | 8 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, custom_styles_display, ellipsize_mode | 0 | 0 |
| 2026-10-04 12:39 | [37202868394](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37202868394) | android | ours | 6904d0f | 50 | 10 | - | checkbox_toggle, extending_paragraph_style_on_paste_after_cut, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, alignment_visual, ellipsize_mode, paragraph_styles_display | 0 | 0 |
| 2026-10-04 10:16 | [37194819023](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37194819023) | android | ours | 6904d0f | 50 | 7 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, ellipsize_mode | 0 | 0 |
| 2026-10-04 08:12 | [37188173907](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37188173907) | android | ours | 6904d0f | 50 | 8 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, custom_styles_display, ellipsize_mode | 0 | 0 |
| 2026-10-04 06:41 | [37183542307](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37183542307) | android | ours | 6904d0f | 49 | 8 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, ellipsize_mode, external_html_parsing | 0 | 0 |
| 2026-10-04 05:30 | [37180071707](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37180071707) | android | ours | 6904d0f | 50 | 12 | - | checkbox_toggle, extending_paragraph_style_on_paste_after_cut, inline_code_paste_into_codeblock, inline_styles_removal, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, alignment_visual, custom_styles_display, ellipsize_mode | 0 | 0 |
| 2026-10-03 18:40 | [37145059263](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37145059263) | android | ours | 6904d0f | 50 | 9 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, custom_styles_display, ellipsize_mode, empty_list_elements_display | 0 | 0 |
| 2026-10-03 14:53 | [37131276940](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37131276940) | ios | ours | 6904d0f | 49 | 5 | - | checkbox_toggle, image_position_stability, inline_code_paste_into_codeblock, links_visual, paragraph_styles_display | 0 | 0 |
| 2026-10-03 14:53 | [37131276940](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37131276940) | android | ours | 6904d0f | 50 | 8 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, custom_styles_display, ellipsize_mode | 0 | 0 |
| 2026-10-03 10:23 | [37116239902](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37116239902) | ios | ours | 6904d0f | 49 | 5 | - | image_position_stability, inline_code_paste_into_codeblock, links_visual, scrolling_with_paragraph_styles, paragraph_styles_display | 0 | 0 |
| 2026-10-03 10:23 | [37116239902](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37116239902) | android | ours | 6904d0f | 50 | 7 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, ellipsize_mode | 0 | 0 |
| 2026-10-02 23:32 | [37078043564](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37078043564) | android | ours | 6904d0f | 49 | 10 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, alignment_visual, custom_styles_display, ellipsize_mode, empty_list_elements_display | 0 | 0 |
| 2026-10-02 23:32 | [37078043564](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37078043564) | ios | ours | 6904d0f | 49 | 4 | - | image_position_stability, inline_code_paste_into_codeblock, links_visual, paragraph_styles_display | 0 | 0 |
| 2026-10-02 20:05 | [37058371404](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37058371404) | ios | ours | 6904d0f | 49 | 4 | - | image_position_stability, inline_code_paste_into_codeblock, links_visual, paragraph_styles_display | 0 | 0 |
| 2026-10-02 20:05 | [37058371404](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37058371404) | android | ours | 6904d0f | 49 | 8 | - | checkbox_toggle, inline_code_paste_into_codeblock, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, ellipsize_mode | 0 | 0 |
