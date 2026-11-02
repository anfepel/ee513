# Raw captures

The A2–A4 raw files are too big for git (about 660 MB), so they live in the GitHub Release as `captures.zip`. Unzip it at the top of the repo and it puts each folder back where `config.json` expects it:

| Folder | Files | What | Captured |
|---|---|---|---|
| `A2/calib_target_img` | 19 | checkerboard, 9 × 6 inner corners, 20.0 ± 0.5 mm squares, varied tilts | Oct 12 |
| `A2/slanted_edge_taget_img` | 10 | slanted-edge target, phone and target fixed, ISO 200, 1/120 s | Oct 12 |
| `A3/flat_field_pairs` | 20 | flat fields, consecutive files form a pair, ISO 64, 1/8 s | Oct 20 |
| `A3/dark_field` | 4 | lens covered, ISO 64, 2 ms, 40 ms and 1 s (×2) | Oct 20 |
| `A4/color_chart_imgs` | 12 | three ColorChecker Minis under three lights, plus a white sheet per light, ISO 400 | Oct 22 |

(`slanted_edge_taget_img` is misspelled, but it's the folder name the notebooks use, so I left it.)

The Exercise 1 captures in `A1/` are already in git from week 1.
