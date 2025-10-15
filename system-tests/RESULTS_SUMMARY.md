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
