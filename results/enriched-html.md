# enriched-html

Upstream has no e2e CI to compare against.

Times in minutes. *Run* is the whole workflow run (builds included); *job* is one job; *tests* is its test step only; *queue* is the wait for a runner.

## Summary

| Project | Platform | Flavour | Side | Build | Runs | Median e2e (min) | Green runs | Runs with no first-attempt failure | First-attempt failures / run | Final failures / run | Runs needing a retry job | Runner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| enriched-html | android | - | ours | 6904d0f | 16 | 29.2 | 0/16 | 0/16 | 8.62 | 7.00 | 0/16 | ubuntu-latest |
| enriched-html | ios | - | ours | 6904d0f | 16 | 4.2 | 0/16 | 0/4 | 4.50 | 2.50 | 0/16 | macos-26 |

## Runs: maestro-runner (bench fork)

| Started (UTC) | Run | Build | Run time | Job | Job time | Tests | Queue | Result |
|---|---|---|---|---|---|---|---|---|
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
| android | 6904d0f | 16 | 29.5 | 0% | 8.62 | 0% | 0.0 | 100% | checkbox_toggle ×16, line_overlapping ×16, mention_popup_closing_on_cursor_travel ×16 / - |
| ios | 6904d0f | 4 | 29.5 | 0% | 4.50 | 0% | 0.0 | 100% | image_position_stability ×4, inline_code_paste_into_codeblock ×4, links_visual ×4 / - |

### Per run

| Started (UTC) | Run | Platform | Side | Build | Flows | Failed at least once | Passed on retry (failed attempts) | Failed at the end | Extra flow runs | Retry jobs |
|---|---|---|---|---|---|---|---|---|---|---|
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
