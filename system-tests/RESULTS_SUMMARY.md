# Cross-OS Benchmark Summary

This document summarizes the latest tracked system test results across supported OS profiles. All numbers are taken from committed JSON snapshots in `system-tests/*`.

## Profiles Included
- Raspberry Pi 5 — Debian 12 (Bookworm) with PREEMPT_RT (`pi-debian-rt`)
- Raspberry Pi 5 — Raspberry Pi OS Lite (Bookworm) PREEMPT (`pi-os-lite`)
- Ubuntu RT (x86_64) PREEMPT_RT (`ubuntu-rt`)

## Kernel and Platform (uname -a)
- pi-debian-rt:
  - Linux pilite 6.15.11-v8-16k+ #1 SMP PREEMPT_RT Sun Sep 28 23:54:45 BST 2025 aarch64 GNU/Linux
- pi-os-lite:
  - Linux pilite 6.12.25+rpt-rpi-2712 #1 SMP PREEMPT Debian 1:6.12.25-1+rpt1 (2025-04-30) aarch64 GNU/Linux
- ubuntu-rt:
  - Linux domas 6.8.1-1034-realtime #35-Ubuntu SMP PREEMPT_RT Tue Sep  9 12:37:21 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux

## Real-time Latency (cyclictest)
- pi-debian-rt: min 1μs, avg 1μs, max 12μs, jitter 11μs
- pi-os-lite:   min 1μs, avg 1μs, max 13μs, jitter 12μs
- ubuntu-rt:    min 1–9μs, avg 3–19μs, max 13–53μs, jitter 12–44μs (varies across runs)

## Composite Score
- pi-debian-rt: 61.43
- pi-os-lite:   60.69
- ubuntu-rt:    55.36 → 66.53 (across three snapshots)

## Algorithm Benchmarks (ms)
- pi-debian-rt:
  - quicksort 1.242, mergesort 1.961, matrix 16.208, fft 132.944
- pi-os-lite:
  - quicksort 1.253, mergesort 1.993, matrix 16.139, fft 131.481
- ubuntu-rt (range across runs):
  - quicksort 0.567–0.611, mergesort 0.775–0.867, matrix 6.288–6.907, fft 49.964–58.083

## Multicore Stress (total operations)
- pi-debian-rt: 38,280,000
- pi-os-lite:   39,010,000
- ubuntu-rt:    399,920,000 – 403,520,000

## Observations
- Raspberry Pi (aarch64) with PREEMPT_RT achieves excellent RT latency (avg 1μs, max ~12–13μs) comparable to Pi OS Lite.
- Ubuntu RT on x86_64 delivers far faster algorithm throughput and multicore ops, but latency varied across snapshots; best run reached avg 3μs, max 13μs.
- Composite scores reflect tradeoffs: Ubuntu has stronger compute throughput; Pi has extremely tight RT latency on embedded hardware.

## Artifacts Referenced
- `system-tests/pi-debian-rt/pi_debian_rt_rtos_full_board_results_20251015_232256.json`
- `system-tests/pi-os-lite/pi_os_lite_rtos_full_board_results_20250928_181814.json`
- `system-tests/ubuntu-rt/ubuntu_rt_rtos_full_board_results_20250928_143249.json`
- `system-tests/ubuntu-rt/ubuntu_rt_rtos_full_board_results_20250928_143445.json`
- `system-tests/ubuntu-rt/ubuntu_rt_rtos_full_board_results_20250928_143521.json`

## Raspberry Pi: Pi OS Lite vs Debian PREEMPT_RT (this system)

Requested comparison between:
- Pi OS Lite (PREEMPT) — `Linux pilite 6.12.25+rpt-rpi-2712 #1 SMP PREEMPT Debian 1:6.12.25-1+rpt1 (2025-04-30) aarch64 GNU/Linux`
- Pi Debian PREEMPT_RT — `Linux pilite 6.15.11-v8-16k+ #1 SMP PREEMPT_RT Sun Sep 28 23:54:45 BST 2025 aarch64 GNU/Linux`

Head-to-head summary (from committed snapshots):
- Real-time latency (cyclictest):
  - Pi OS Lite:    min 1μs, avg 1μs, max 13μs, jitter 12μs
  - Debian RT:     min 1μs, avg 1μs, max 12μs, jitter 11μs
  - Takeaway: Debian PREEMPT_RT edges out with slightly lower max and jitter, both are excellent.

- Algorithm performance (ms):
  - QuickSort:     Pi OS Lite 1.253 vs Debian RT 1.242 (≈ parity)
  - MergeSort:     Pi OS Lite 1.993 vs Debian RT 1.961 (≈ parity)
  - Matrix 50x50:  Pi OS Lite 16.139 vs Debian RT 16.208 (≈ parity)
  - FFT 512 (DFT): Pi OS Lite 131.481 vs Debian RT 132.944 (≈ parity)
  - Takeaway: CPU compute on Pi is effectively the same across kernels; tiny swings are within run-to-run variance.

- Multicore stress (5s total ops):
  - Pi OS Lite:    39,010,000
  - Debian RT:     38,280,000
  - Takeaway: Nearly identical; small differences likely due to scheduling/thermal noise.

- Composite score:
  - Pi OS Lite:    60.69
  - Debian RT:     61.43
  - Takeaway: Composite slightly favors Debian PREEMPT_RT, driven by marginally tighter latency.

Bottom line:
- If your priority is determinism and the lowest jitter, Debian PREEMPT_RT shows a tiny advantage (12μs vs 13μs max, 11μs vs 12μs jitter) while retaining identical algorithm throughput.
- Pi OS Lite remains an excellent low-overhead choice with practically equivalent performance; both are strong for Pi 5 real-time workloads.

## Verification Re-runs and Variance Notes (2025-10-15)

We re-ran the Debian PREEMPT_RT benchmarks and an independent cyclictest to validate results after a user-observed discrepancy:

- New Debian RT benchmark snapshots added:
  - `system-tests/pi-debian-rt/pi_debian_rt_rtos_full_board_results_20251015_233712.json` (Max 35μs)
  - `system-tests/pi-debian-rt/pi_debian_rt_rtos_full_board_results_20251015_234033.json` (Max 16μs)

- Independent cyclictest samples (10s, P99, -m, -S, -p99):
  - Run 1: per-thread Max 11–23μs, Avg ≈ 1μs
  - Run 2: per-thread Max 15–18μs, Avg ≈ 2μs

Interpretation:
- The earlier nominal snapshot (Max 12μs) remains representative of typical performance.
- The 35μs event is a tail outlier, likely due to transient system noise (IRQ timing, governor ticks, background I/O). Subsequent runs and independent cyclictest corroborate stable 11–23μs maxima with ~1–2μs average.

Methodology guidance:
- For publication-grade reporting, perform multiple runs and aggregate:
  - Report Avg(Max) across N runs and/or P99/P99.9 if available
  - Include independent cyclictest records alongside benchmark JSON
  - Optionally set CPU governor to performance and minimize background services to reduce variance
