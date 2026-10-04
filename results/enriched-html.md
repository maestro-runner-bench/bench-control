# enriched-html

Upstream has no e2e CI to compare against.

Times in minutes. *Run* is the whole workflow run (builds included); *job* is one job; *tests* is its test step only; *queue* is the wait for a runner.

## Summary

| Project | Platform | Flavour | Side | Build | Runs | Median e2e (min) | Green runs | Runs with no first-attempt failure | First-attempt failures / run | Final failures / run | Runs needing a retry job | Runner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| enriched-html | android | - | ours | 6904d0f | 6 | 24.1 | 0/6 | 0/6 | 8.50 | 7.17 | 0/6 | ubuntu-latest |
| enriched-html | android | - | ours | 49360bb | 1 | 26.4 | 0/1 | 0/1 | 42.00 | 42.00 | 0/1 | ubuntu-latest |
| enriched-html | android | - | ours | older | 4 | 23.9 | 0/4 | 0/3 | 29.00 | 28.33 | 0/4 | ubuntu-latest |
| enriched-html | ios | - | ours | 6904d0f | 6 | 29.5 | 0/6 | 0/5 | 4.60 | 2.60 | 0/6 | macos-26 |
| enriched-html | ios | - | ours | 49360bb | 1 | 31.0 | 0/1 | 0/1 | 5.00 | 3.00 | 0/1 | macos-26 |
| enriched-html | ios | - | ours | older | 4 | 33.5 | 0/3 | 0/3 | 18.67 | 17.33 | 0/4 | macos-26 |

## Runs: maestro-runner (bench fork)

| Started (UTC) | Run | Build | Run time | Job | Job time | Tests | Queue | Result |
|---|---|---|---|---|---|---|---|---|
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
| 2026-10-02 17:22 | [37040245914](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37040245914) | 6904d0f | 48.1 | e2e-android | 25.6 | 24.8 | 0.1 | 42/49, 2 passed on retry |
|  | | |  | e2e-ios | 48.0 | 42.0 | 0.1 | 45/48, 2 passed on retry |
| 2026-10-02 14:45 | [37022049656](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37022049656) | 49360bb | 40.6 | e2e-android | 27.1 | 26.4 | 0.6 | 7/49 |
|  | | |  | e2e-ios | 35.4 | 31.0 | 5.2 | 45/48, 2 passed on retry |
| 2026-10-02 12:30 | [37007084631](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37007084631) | maestro-runner 1.1.28.1 | 31.0 | e2e-android | 31.0 | 30.4 | 0.0 | 42/49, 1 passed on retry |
|  | | |  | e2e-ios | 16.3 | 12.3 | 8.2 | 0/48 |
| 2026-10-02 11:59 | [37004090179](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37004090179) | maestro-runner 1.1.28.1 | 51.2 | e2e-android | 27.8 | 27.1 | 0.0 | 0/49 |
|  | | |  | e2e-ios | 44.0 | 39.8 | 7.2 | 46/48, 2 passed on retry |
| 2026-10-02 11:07 | [36999228535](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/36999228535) | maestro-runner 1.1.28.1 | 37.4 | e2e-android | 21.4 | 20.8 | 0.0 | 20/49, 1 passed on retry |
|  | | |  | e2e-ios | 37.3 | 33.5 | 0.1 | 46/48, 2 passed on retry |
| 2026-10-02 11:03 | [36998917386](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/36998917386) | - | 4.0 | e2e-android | 1.5 | 0.7 | 0.0 | failure |
|  | | |  | e2e-ios | 3.9 | - | 0.1 | cancelled before tests |

## Trend

![enriched-html-android](charts/enriched-html-android.svg)

![enriched-html-ios](charts/enriched-html-ios.svg)


## Retried test cases

Per run, from each job's log: a flow *failed at least once* if any of its attempts failed, inside its job (maestro-runner `--retries`, React Native's iOS per-flow attempts, agent-device, Expo's rounds) or in a retry job (React Native's retry_1/retry_2); it *passed on retry* if it then passed. *Extra flow runs* counts every run of a flow beyond its first, including whole-suite reruns of flows that had passed. Runs whose logs had expired are left out.

Each cell: **ours vs upstream**; the better one in bold. Ours is the newest maestro-runner build.

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing (ours / upstream) |
|---|---|---|---|---|---|---|---|---|---|
| android | 6904d0f | 6 | 27.2 | 0% | 8.50 | 0% | 0.0 | 100% | checkbox_toggle ×6, line_overlapping ×6, mention_popup_closing_on_cursor_travel ×6 / - |
| ios | 6904d0f | 5 | 29.6 | 0% | 4.60 | 0% | 0.0 | 100% | image_position_stability ×5, inline_code_paste_into_codeblock ×5, links_visual ×5 / - |

Ours on earlier maestro-runner builds:

| Job | Build | Runs | Test time / run (min) | Every flow passed first time | Flows that failed at least once / run | Runs needing a retry job | Extra flow runs / run | Runs ending with a failed flow | Most often failing |
|---|---|---|---|---|---|---|---|---|---|
| android | 49360bb | 1 | 26.4 | 0% | 43.00 | 0% | 0.0 | 100% | checkbox_toggle ×1, extending_paragraph_style_on_paste_after_copy ×1, extending_paragraph_style_on_paste_after_cut ×1 |
| android | older | 3 | 27.1 | 0% | 29.67 | 0% | 0.0 | 100% | checkbox_toggle ×3, extending_paragraph_style_on_paste_after_cut ×3, line_overlapping ×3 |
| ios | 49360bb | 1 | 31.0 | 0% | 5.00 | 0% | 0.0 | 100% | checkbox_toggle ×1, image_position_stability ×1, inline_code_paste_into_codeblock ×1 |
| ios | older | 3 | 33.5 | 0% | 19.00 | 0% | 0.0 | 100% | image_position_stability ×3, inline_code_paste_into_codeblock ×3, links_visual ×3 |

### Per run

| Started (UTC) | Run | Platform | Side | Build | Flows | Failed at least once | Passed on retry (failed attempts) | Failed at the end | Extra flow runs | Retry jobs |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-03 18:40 | [37145059263](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37145059263) | android | ours | 6904d0f | 50 | 9 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, custom_styles_display, ellipsize_mode, empty_list_elements_display | 0 | 0 |
| 2026-10-03 14:53 | [37131276940](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37131276940) | ios | ours | 6904d0f | 49 | 5 | - | checkbox_toggle, image_position_stability, inline_code_paste_into_codeblock, links_visual, paragraph_styles_display | 0 | 0 |
| 2026-10-03 14:53 | [37131276940](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37131276940) | android | ours | 6904d0f | 50 | 8 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, custom_styles_display, ellipsize_mode | 0 | 0 |
| 2026-10-03 10:23 | [37116239902](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37116239902) | ios | ours | 6904d0f | 49 | 5 | - | image_position_stability, inline_code_paste_into_codeblock, links_visual, scrolling_with_paragraph_styles, paragraph_styles_display | 0 | 0 |
| 2026-10-03 10:23 | [37116239902](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37116239902) | android | ours | 6904d0f | 50 | 7 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, ellipsize_mode | 0 | 0 |
| 2026-10-02 23:32 | [37078043564](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37078043564) | android | ours | 6904d0f | 49 | 10 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, alignment_visual, custom_styles_display, ellipsize_mode, empty_list_elements_display | 0 | 0 |
| 2026-10-02 23:32 | [37078043564](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37078043564) | ios | ours | 6904d0f | 49 | 4 | - | image_position_stability, inline_code_paste_into_codeblock, links_visual, paragraph_styles_display | 0 | 0 |
| 2026-10-02 20:05 | [37058371404](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37058371404) | ios | ours | 6904d0f | 49 | 4 | - | image_position_stability, inline_code_paste_into_codeblock, links_visual, paragraph_styles_display | 0 | 0 |
| 2026-10-02 20:05 | [37058371404](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37058371404) | android | ours | 6904d0f | 49 | 8 | - | checkbox_toggle, inline_code_paste_into_codeblock, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, ellipsize_mode | 0 | 0 |
| 2026-10-02 17:22 | [37040245914](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37040245914) | android | ours | 6904d0f | 50 | 9 | - | checkbox_toggle, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, alignment_visual, ellipsize_mode, paragraph_styles_display | 0 | 0 |
| 2026-10-02 17:22 | [37040245914](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37040245914) | ios | ours | 6904d0f | 49 | 5 | - | image_position_stability, inline_code_paste_into_codeblock, links_visual, custom_styles_display, paragraph_styles_display | 0 | 0 |
| 2026-10-02 14:45 | [37022049656](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37022049656) | ios | ours | 49360bb | 49 | 5 | - | checkbox_toggle, image_position_stability, inline_code_paste_into_codeblock, links_visual, paragraph_styles_display | 0 | 0 |
| 2026-10-02 14:45 | [37022049656](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37022049656) | android | ours | 49360bb | 50 | 43 | - | checkbox_toggle, extending_paragraph_style_on_paste_after_copy, extending_paragraph_style_on_paste_after_cut, html_link_not_extended, image_inside_list_parsing, image_position_stability, initial_html_parsing, inline_code_blocking_styles, inline_code_paste_into_codeblock, inline_styles_merge, inline_styles_removal, inline_styles_survive_block_toggle, inline_styles_visual, line_overlapping, link_not_extended, links_visual, list_newline_insertion, mention_parsing_handles_single_quoted_attributes, mention_popup_closing_on_cursor_travel, ordered_list_renumbering, paragraph_style_removal, paragraph_style_toggle, paragraph_styles_alignment_visual, paragraph_styles_blocks_visual, paragraph_styles_headings_visual, paragraph_styles_lists_visual, paragraph_styles_no_crash, placeholder_visual, preserve_typing_attributes_on_selection_change, scrolling_after_typing, scrolling_set_value, scrolling_with_paragraph_styles, alignment_visual, custom_styles_display, ellipsize_mode, empty_list_elements_display, external_html_parsing, image_press, inline_styles_display, link_press, mention_press, paragraph_styles_display, font_scaling | 0 | 0 |
| 2026-10-02 12:30 | [37007084631](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37007084631) | android | ours | - | 50 | 9 | - | checkbox_toggle, extending_paragraph_style_on_paste_after_cut, line_overlapping, mention_popup_closing_on_cursor_travel, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, ellipsize_mode, font_scaling | 0 | 0 |
| 2026-10-02 12:30 | [37007084631](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37007084631) | ios | ours | - | 49 | 49 | - | checkbox_toggle, codeblock_br_preservation, codeblock_no_link_detection, codeblock_style_blocking, conflicting_paragraph_merge, core_controls_smoke, empty_element_parsing, empty_html_block_parsing, empty_lists_parsing, html_link_not_extended, image_inside_list_parsing, image_position_stability, initial_html_parsing, inline_code_blocking_styles, inline_code_paste_into_codeblock, inline_styles_merge, inline_styles_removal, inline_styles_survive_block_toggle, inline_styles_visual, line_overlapping, link_not_extended, links_visual, list_newline_insertion, mention_parsing_handles_single_quoted_attributes, mention_popup_closing_on_cursor_travel, ordered_list_renumbering, paragraph_style_removal, paragraph_style_toggle, paragraph_styles_alignment_visual, paragraph_styles_blocks_visual, paragraph_styles_headings_visual, paragraph_styles_lists_visual, paragraph_styles_no_crash, placeholder_visual, preserve_typing_attributes_on_selection_change, scrolling_after_typing, scrolling_set_value, scrolling_with_paragraph_styles, alignment_visual, custom_styles_display, ellipsize_mode, empty_list_elements_display, external_html_parsing, image_press, inline_styles_display, link_press, mention_press, paragraph_styles_display, font_scaling | 0 | 0 |
| 2026-10-02 11:59 | [37004090179](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37004090179) | android | ours | - | 50 | 50 | - | checkbox_toggle, codeblock_no_link_detection, codeblock_style_blocking, conflicting_paragraph_merge, core_controls_smoke, empty_element_parsing, empty_html_block_parsing, empty_lists_parsing, extending_paragraph_style_on_paste_after_copy, extending_paragraph_style_on_paste_after_cut, html_link_not_extended, image_inside_list_parsing, image_position_stability, initial_html_parsing, inline_code_blocking_styles, inline_code_paste_into_codeblock, inline_styles_merge, inline_styles_removal, inline_styles_survive_block_toggle, inline_styles_visual, line_overlapping, link_not_extended, links_visual, list_newline_insertion, mention_parsing_handles_single_quoted_attributes, mention_popup_closing_on_cursor_travel, ordered_list_renumbering, paragraph_style_removal, paragraph_style_toggle, paragraph_styles_alignment_visual, paragraph_styles_blocks_visual, paragraph_styles_headings_visual, paragraph_styles_lists_visual, paragraph_styles_no_crash, placeholder_visual, preserve_typing_attributes_on_selection_change, scrolling_after_typing, scrolling_set_value, scrolling_with_paragraph_styles, alignment_visual, custom_styles_display, ellipsize_mode, empty_list_elements_display, external_html_parsing, image_press, inline_styles_display, link_press, mention_press, paragraph_styles_display, font_scaling | 0 | 0 |
| 2026-10-02 11:59 | [37004090179](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/37004090179) | ios | ours | - | 49 | 4 | - | image_position_stability, inline_code_paste_into_codeblock, links_visual, paragraph_styles_display | 0 | 0 |
| 2026-10-02 11:07 | [36999228535](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/36999228535) | ios | ours | - | 49 | 4 | - | image_position_stability, inline_code_paste_into_codeblock, links_visual, paragraph_styles_display | 0 | 0 |
| 2026-10-02 11:07 | [36999228535](https://github.com/maestro-runner-bench/react-native-enriched-html/actions/runs/36999228535) | android | ours | - | 50 | 30 | - | checkbox_toggle, codeblock_no_link_detection, codeblock_style_blocking, conflicting_paragraph_merge, extending_paragraph_style_on_paste_after_copy, extending_paragraph_style_on_paste_after_cut, html_link_not_extended, image_position_stability, inline_styles_merge, inline_styles_removal, inline_styles_survive_block_toggle, inline_styles_visual, line_overlapping, link_not_extended, links_visual, list_newline_insertion, mention_popup_closing_on_cursor_travel, ordered_list_renumbering, paragraph_style_removal, paragraph_style_toggle, paragraph_styles_alignment_visual, paragraph_styles_blocks_visual, paragraph_styles_headings_visual, paragraph_styles_lists_visual, paragraph_styles_no_crash, preserve_typing_attributes_on_selection_change, scrolling_after_typing, scrolling_with_paragraph_styles, custom_styles_display, ellipsize_mode | 0 | 0 |
