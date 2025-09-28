# Pi OS Lite System Tests

## Test Environment
- **Operating System**: Linux pilite 6.12.25+rpt-rpi-2712 #1 SMP PREEMPT Debian 1:6.12.25-1+rpt1 (2025-04-30) aarch64 GNU/Linux
- **Platform**: Raspberry Pi OS Lite (Debian 12 "Bookworm" based)
- **CPU**: ARM Cortex-A76 (4 cores) - Raspberry Pi 5 Model B Rev 1.0
- **Clock Speed**: 1.5 GHz - 2.4 GHz (dynamic scaling)
- **Memory**: 4.0 GB RAM
- **Storage**: 64GB SD card (59GB available)
- **Python**: 3.11.2
- **Architecture**: ARM64 (aarch64)
- **RT Kernel**: SMP PREEMPT enabled
- **cyclictest**: Available and utilized (rt-tests v2.40)

## Hardware Specifications
- **Device**: Raspberry Pi 5 Model B Rev 1.0
- **SoC**: Broadcom BCM2712 (ARM Cortex-A76 quad-core)
- **CPU Cache**: L1d: 256 KiB, L1i: 256 KiB, L2: 2 MiB, L3: 2 MiB
- **CPU Flags**: fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm lrcpc dcpop asimddp
- **Memory Type**: LPDDR4X
- **Storage Interface**: microSD (UHS-I)
- **Form Factor**: Single Board Computer (SBC)

## Latest Test Results Summary
- **Test Date**: 2025-09-28 18:18:14
- **Real-time Latency**: Max 13μs, Avg 1μs, Min 1μs
- **Jitter**: 12μs (excellent consistency)
- **Multicore Operations**: 39,010,000 total operations across 4 cores

## Key Performance Metrics

### Real-time Performance
- **Average Latency**: 1μs (excellent for embedded systems)
- **Maximum Latency**: 13μs (improved from previous 30μs)
- **Jitter**: 12μs (very consistent timing)
- **RT Priority**: 99 (maximum available)
- **Memory Locking**: ✅ Supported
- **CPU Isolation**: Core 3 isolated for RT tasks
- **RT Scheduling**: ✅ Available

### Algorithm Benchmarks (Latest Run)
- **QuickSort (1000 elements)**: 1.253ms avg (improved performance)
- **MergeSort (1000 elements)**: 1.993ms avg (better than previous 2.78ms)  
- **Matrix Multiplication (50x50)**: 16.139ms avg (improved from 20.8ms)
- **FFT Simulation (512 points)**: 131.481ms avg (O(n²) DFT implementation)

### Multicore Stress Test Performance
- **Total Operations**: 39,010,000 operations (5-second test)
- **Average per Core**: 9,752,500 operations
- **All 4 ARM Cortex-A76 cores**: Successfully utilized
- **CPU Isolation**: Core 3 optimized for real-time tasks

## Performance Comparison vs Ubuntu RT
| Metric | Pi OS Lite (Pi 5) | Ubuntu RT (Ryzen 7) | Pi Advantage |
|--------|-------------------|---------------------|--------------|
| **Avg Latency** | 1μs | 3μs | 🏆 **3x better** |
| **Power Usage** | 5-15W | 65-142W | 🏆 **~10x efficient** |
| **Cost** | ~$80 | ~$400+ | 🏆 **5x cheaper** |
| **Form Factor** | Credit card size | Full desktop | 🏆 **Portable** |

## Environment Notes
- **Headless Configuration**: No desktop environment for minimal overhead
- **Optimized Boot**: Fast startup and low memory footprint  
- **Real-time Optimizations**: Memory locking, RT priority scheduling
- **ARM Architecture**: Native ARM64 instruction set utilization
- **NUMA Topology**: 8 NUMA nodes detected for advanced memory management
- **Security Mitigations**: Speculative execution protections enabled

## File Structure
```
pi-os-lite/
├── README.md                                          # This comprehensive documentation
├── pi_os_lite_main.py                                # Full benchmark script
├── pi_os_lite_main_simplified.py                     # Simplified benchmark script  
├── pi_os_lite_rtos_full_board_results_20250928_181814.json  # Latest test results
└── pi_os_lite_tests/                                 # Additional test resources
```

## Running Tests
```bash
# Navigate to pi-os-lite directory
cd system-tests/pi-os-lite/

# Full benchmark (requires sudo for real-time priority)
sudo python3 pi_os_lite_main.py

# Simplified benchmark (user permissions)
python3 pi_os_lite_main_simplified.py

# View detailed results
cat pi_os_lite_rtos_full_board_results_20250928_181814.json
```

## System Optimization Applied
- **Real-time Scheduling**: Maximum priority (99) for critical tasks
- **Memory Locking**: RT tasks protected from virtual memory swapping
- **CPU Affinity**: Dedicated core isolation for real-time processing
- **Garbage Collection**: Disabled during benchmark execution
- **Core Isolation**: Core 3 reserved for RT tasks
- **PREEMPT Kernel**: SMP PREEMPT scheduling for low-latency response

## Key Findings
1. **Exceptional Latency**: 1μs average latency rivals high-end systems
2. **Consistent Performance**: 12μs jitter shows excellent timing predictability  
3. **Improved Results**: Better performance than previous test runs
4. **Power Efficiency**: Outstanding performance-per-watt for embedded applications
5. **Cost Effectiveness**: Professional RT capabilities at consumer price point

## Ideal Use Cases
- **Industrial IoT**: Real-time sensor data processing
- **Robotics Control**: Low-latency motor control and feedback systems
- **Edge Computing**: Real-time ML inference at the edge
- **Automation**: Time-critical control systems
- **Embedded RT**: Cost-effective real-time system prototyping

---
*Test conducted on Raspberry Pi 5 Model B with Pi OS Lite - demonstrating exceptional real-time performance for embedded applications.*