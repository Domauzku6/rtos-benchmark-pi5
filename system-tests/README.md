# System Tests Index

This directory contains system-specific benchmark runs and documentation. Each subfolder represents a platform or OS profile.

## Folders

- `pi-os-lite/` — Raspberry Pi OS Lite on Raspberry Pi devices. Includes run scripts and latest result snapshots.
- `ubuntu-rt/` — Ubuntu with RT (PREEMPT_RT) kernel on x86/AMD64 or ARM platforms.
- `pi-debian-rt/` — Raspberry Pi 5 running Debian 12 (Bookworm) with PREEMPT_RT kernel (this system).

## Naming Convention

Result snapshot JSON files follow:

```
<profile>_rtos_full_board_results_YYYYMMDD_HHMMSS.json
```

Examples:
- `pi_os_lite_rtos_full_board_results_20250928_181814.json`
- `ubuntu_rt_rtos_full_board_results_20250928_143249.json`
- `pi_debian_rt_rtos_full_board_results_20251015_232256.json`

## Notes

- Large result files are intentionally committed for reproducibility and historical comparison.
- See each folder's README for environment details, including the exact `uname -a` output.

## Summary

- See consolidated cross-OS results in `RESULTS_SUMMARY.md`.
