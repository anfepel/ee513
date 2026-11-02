# EE 513: Image Formation and Computational Imaging

EE513 PSU, Fall 2026. Andrei Perez.

Everything here is measured on an iPhone 17 Pro Max, main camera at 1×, from raw Bayer DNGs. Each exercise measured one thing. Project 1 pulls those measurements into a single datasheet with uncertainties.

| Folder | What | Done | Main result |
|---|---|---|---|
| [`A1/`](A1) | Exercise 1: environment smoke test, first raw files, first calibration | Oct 6 | the toolchain works, and the camera writes true Bayer raw |
| [`A2/`](A2) | Exercise 2: camera calibration, pixel pitch, slanted-edge MTF | Oct 15 | RMS 0.665 px; centre MTF50 0.060 cy/µm, against 0.197 predicted for a diffraction-limited lens |
| [`A3/`](A3) | Exercise 3: photon transfer curve, read noise, dark current | Oct 20 | K = 0.273 DN/e⁻, read noise 6.7 e⁻, 10.9 stops |
| [`A4/`](A4) | Exercise 4: white balance, colour matrix, ΔE | Oct 28 | mean ΔE<sub>00</sub> 11.7 -> 2.45 |
| [`Project1/`](Project1) | Project 1: the full camera characterization | Nov 2 | see [Project1/README.md](Project1/README.md) |

The exercise notebooks were written on the dates above, but I only moved them into this repo for the project submission.
The commit messages give each exercise's actual dates.

## Setup

```bash
uv sync          # provided by EE513 instructor
```

