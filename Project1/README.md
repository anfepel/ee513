# Project 1: characterizing my iPhone 17 Pro Max main camera

EE 513, Fall 2026 · Andrei Perez

Apple's spec sheet for this camera says 48 MP, 24 mm, f/1.78 and nothing else. For Project 1 I measured the rest from raw captures: distortion, sharpness across the frame, the noise model, dynamic range and colour accuracy. Every number below comes with an uncertainty and a note on how I got it.

All captures are from the main camera at 1× (`iPhone 17 Pro Max back camera 6.765mm f/1.78`), saved as Bayer DNG with Lightroom on iOS. The DNGs are BGGR, 12-bit, black level 528, 4032 × 3024. That is the binned 12 MP output of the 48 MP sensor. The `lens_id` of all 65 files was checked to make sure they came from the same camera.

## Results

| | Quantity | Value | Notes |
|---|---|---|---|
| Geometry | f<sub>x</sub>, f<sub>y</sub> | 2924.8 ± 14.1, 2927.4 ± 13.6 px | 17 of 19 views detected |
| | f | 7.08 ± 0.15 mm | EXIF says 6.765 mm; see the report |
| | c<sub>x</sub>, c<sub>y</sub> | 2024.1 ± 4.3, 1513.5 ± 4.0 px | image centre is 2016, 1512 |
| | k<sub>1</sub>, k<sub>2</sub> | +0.182 ± 0.006, −0.522 ± 0.038 | k<sub>3</sub> fixed at 0 |
| | p<sub>1</sub>, p<sub>2</sub> | −0.0023 ± 0.0006, −0.0008 ± 0.0006 | |
| | RMS reprojection | 0.665 ± 0.055 px | |
| MTF | MTF50, centre | 0.285 ± 0.021 cy/px (59 ± 4 cy/mm) | green plane, Nyquist = 0.5 |
| | MTF50, outer squares | 0.170 to 0.234 cy/px | 0.72 ± 0.02 of the centre |
| | MTF at Nyquist, centre | 0.205 ± 0.026 | a diffraction-limited lens would give 0.78 |
| Noise, ISO 64 | gain K | 0.273 ± 0.014 DN/e⁻ | |
| | read noise | 6.7 ± 0.6 e⁻ | |
| | full scale | 13,080 ± 680 e⁻ | where the ADC clips |
| | dark current | 8.4 ± 0.4 e⁻/s | only 3 exposure times |
| Dynamic range | | 10.93 ± 0.09 stops | floor = read noise (10.83 with the floor at SNR = 1) |
| Colour | mean ΔE<sub>00</sub> | 11.74 → 2.45 ± 0.11 | before/after the colour matrix; worst patch 5.2 (purplish blue) |

The ± values are 1σ:
- **Geometry:** the larger of OpenCV's estimate and a leave-one-view-out jackknife. The jackknife was the larger one, by about 5×, for f<sub>x</sub>.
- **MTF:** the spread over 10 repeated captures.
- **Noise:** from the fit.
- **Colour:** the spread over three charts.

The MTF is in cycles per pixel of the raw green plane. That plane is sampled every second pixel, so divide by 2 to get cycles per sensor pixel.

`results.json` uses the course template. The full results (each edge, each patch, each PTC point) are in `results/results_full.json`.

### Against the camera's own metadata

Apple doesn't publish noise or colour figures, but every DNG carries some of Apple's own calibration. I compared against that:

- **Noise profile.** It implies K = 0.316 DN/e⁻ and a read noise of 11.2 e⁻. I get 0.273 DN/e⁻ and 6.7 e⁻. Apple's numbers match my data only at high signal (more in the report).
- **Colour matrix (ForwardMatrix).** It gives ΔE<sub>00</sub> = 6.3 on my charts, against 2.45 for my fitted matrix.
- **Lens-shading correction.** Its centre is 7 px from my principal point, which is an independent check on the calibration.

## What's in here

- `report/`: the submitted report (`Project1EE513.pdf`) and its LaTeX source (`Project1EE513/`, compiles on Overleaf).
- `results.json`: the headline numbers, in the course template.
- `results/`: the full results (`results_full.json`), the run log and the figures used in the report.

The measurements build on my Exercise 2–4 notebooks (`../A2`, `../A3`, `../A4`) and use the same raw files. Those are not in git (about 660 MB): download `captures.zip` from the repo's Releases page and unzip it at the top of the repo. See [`data/README.md`](data/README.md).

## Limitations

- **Distortion.** My calibration views only put board corners within 57 % of the way out to the frame corners. Inside that radius the distortion model is solid. Outside it, models that agree in the middle disagree by about 250 px at the corner, so I don't trust it there.
- **Frame corners.** The "corner" squares of the slanted-edge target sit about 40 % of the way out, not in the frame corners. Sharpness drops quickly with distance from the centre, so the real corners are softer than anything reported here.
- **Noise model.** It is for ISO 64. The apparent gain drifts by about 40 % from dark to bright, so the iPhone's raw output isn't a perfectly linear shot-plus-read-noise chain. The quoted K uncertainty is widened to cover that.
- **Dark current.** I only have three exposure times, and I didn't record the phone's temperature.
