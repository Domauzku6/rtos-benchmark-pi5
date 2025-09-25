# RTOS Benchmark Suite - Educational & Modular Edition

A comprehensive real-time operating system benchmark suite that evaluates system performance, real-time capabilities, and algorithm efficiency across multiple platforms.

**🚀 Now with optimized modular architecture for better performance and maintainability!**
**🎓 Plus comprehensive educational features for learning algorithms and real-time concepts!**

## ✨ What's New in the Educational Edition

- **🎓 Interactive Learning Lab**: Hands-on algorithm education with detailed explanations
- **🏎️ Improved Performance**: Faster startup time and reduced memory footprint
- **🔧 Better Maintainability**: Clean modular structure with single-responsibility modules
- **📦 Organized Codebase**: Original 2400+ line file split into focused components
- **🧪 Enhanced Testability**: Individual modules can be tested independently
- **📚 Educational Documentation**: Step-by-step algorithm explanations with complexity analysis
- **🔬 Algorithm Comparison Tools**: Interactive demos showing Big O complexity in practice

#### Linux (Full Features)
```bash
# Install cyclictest for real RT measurements (optional)
sudo apt-get install rt-tests

# Run with full privileges for optimal results
sudo python3 main_simplified.py
```

#### macOS (Limited RT Features)
```bash
# No additional setup required
python3 main_simplified.py
```

#### Windows (Algorithm Testing)
```bash
# No additional setup required
python main_simplified.py
```

## 🏗️ Modular Architecture

The original monolithic 2400+ line file has been expertly split into focused modules:

### Core Modules (`src/`)

- **`platform_compat.py`** (350 lines) - Cross-platform compatibility utilities
- **`rtos_env.py`** (375 lines) - RTOS environment setup and management  
- **`algorithms.py`** (800+ lines) - 🎓 **Educational sorting algorithms with detailed explanations**
- **`cyclictest.py`** (217 lines) - cyclictest integration with simulation fallback
- **`multicore.py`** (291 lines) - CPU core management and affinity setting
- **`results_board.py`** (291 lines) - Results formatting and display
- **`benchmark_orchestrator.py`** (383 lines) - Main benchmark coordination

### Benefits of Modular Design

- **⚡ Faster Loading**: Only necessary modules loaded on demand
- **🧪 Better Testing**: Individual components can be unit tested
- **🔧 Easier Maintenance**: Bug fixes and features isolated to relevant modules
- **📈 Reduced Memory**: More efficient memory usage patterns
- **🔄 Code Reuse**: Modules can be imported independentlytter performance and maintainability!**

## ✨ What's New in the Modular Edition

- **🏎️ Improved Performance**: Faster startup time and reduced memory footprint
- **🔧 Better Maintainability**: Clean modular structure with single-responsibility modules
- **📦 Organized Codebase**: Original 2400+ line file split into focused components
- **🧪 Enhanced Testability**: Individual modules can be tested independently
- **📚 Better Documentation**: Each module is self-documenting with clear purpose

## 📁 Project Structure

```
rtos_benchmark/
├── main.py                          # 🎯 Primary CLI entry point
├── main_simplified.py               # 🎯 Streamlined entry point  
├── rtos_full_board_benchmark.py    # 🎯 Backward compatibility wrapper
├── learn_algorithms.py              # 🎓 Interactive algorithm learning demo
├── README.md                        # 📖 This documentation
├── src/                            # 📦 Modular components
│   ├── platform_compat.py         # Cross-platform utilities
│   ├── rtos_env.py                # RTOS environment management
│   ├── algorithms.py              # 🎓 Educational algorithm implementations  
│   ├── cyclictest.py              # Cyclictest integration
│   ├── multicore.py               # Multi-core management
│   ├── results_board.py           # Results display & reporting
│   └── benchmark_orchestrator.py  # Main coordination
├── tests/                          # 🧪 Test suite
├── old_py/                         # 📦 Original files archive
└── redundant/                      # 📦 Non-essential files archive
```

## Features

### � Educational Features (NEW!)
- **Interactive Algorithm Lab**: Hands-on learning environment with algorithm comparison demos
- **Step-by-Step Explanations**: Detailed code comments explaining optimization techniques
- **Complexity Analysis**: Big O notation examples with real-world performance correlation
- **Algorithm Selection Guide**: Learn when to choose each algorithm for different scenarios
- **Best vs Worst Case Demos**: Understand how input data affects algorithm performance
- **Real-Time Learning**: Educational focus on RT system algorithm considerations

### ���🎯 Core Benchmarking
- **Real-time Latency Testing**: Integration with cyclictest for precise latency measurements
- **Algorithm Performance**: Comprehensive testing of sorting algorithms, matrix operations, and FFT
- **Multicore Optimization**: CPU affinity management and parallel processing evaluation
- **Cross-platform Support**: Linux, macOS, and Windows compatibility with platform-specific optimizations

### 📊 Advanced Analysis
- **Performance Scoring**: Composite scoring system for objective performance comparison
- **Results Management**: JSON export/import with comprehensive reporting
- **Historical Comparison**: Compare current results with previous benchmark runs
- **System Validation**: Automatic capability detection and optimization recommendations

### 🔧 Technical Capabilities
- **RT Environment Setup**: Memory locking, RT scheduling, and privilege management
- **CPU Isolation**: Dedicated core allocation for real-time tasks
- **Temperature Monitoring**: System thermal state tracking during tests
- **Graceful Fallbacks**: Simulation mode when hardware features are unavailable

## Quick Start

### 🎯 Understanding Quicksort Performance & System Types

Before running benchmarks, it's important to understand what different timing results mean for your system type:

#### **Quicksort Complexity Explained**

**Algorithm Characteristics:**
- **Best Case**: O(n log n) - Balanced partitions, ~1.39 × n log n comparisons
- **Average Case**: O(n log n) - Random data, consistent performance 
- **Worst Case**: O(n²) - Already sorted/reverse sorted, n²/2 comparisons

#### **What Timing Results Mean by System Type**

**🖥️ Desktop/Workstation (Typical Results)**
```
Array Size: 100,000 elements
Expected Performance:
├─ Quicksort: 8-15ms      (Good - Standard desktop performance)
├─ Bubble Sort: 2.5-5s    (Educational comparison)  
└─ Matrix Ops: 50-200ms   (CPU-dependent)

System Indicators:
├─ Memory Locking: 🔴 FAILED (normal - no admin rights)
├─ RT Priority: 🔴 INACTIVE (normal - user permissions)
├─ CPU Affinity: 🟢 ISOLATED (works on most systems)
└─ Garbage Collection: 🟢 DISABLED (Python control)
```

**🏭 Production RT System (Professional Results)**
```
Array Size: 100,000 elements  
Expected Performance:
├─ Quicksort: 3-8ms       (Excellent - RT optimizations active)
├─ Bubble Sort: 1.8-3.2s  (Consistent due to RT priority)
└─ Matrix Ops: 25-80ms    (Optimal cache behavior)

System Indicators:
├─ Memory Locking: 🟢 LOCKED (prevents swap delays)
├─ RT Priority: 🟢 ACTIVE (SCHED_FIFO priority 99)
├─ CPU Affinity: 🟢 ISOLATED (dedicated core)
└─ Garbage Collection: 🟢 DISABLED (no interruptions)
```

**💻 Laptop/Mobile (Resource-Constrained)**
```
Array Size: 100,000 elements
Expected Performance:  
├─ Quicksort: 12-25ms     (Slower - thermal throttling possible)
├─ Bubble Sort: 4-8s      (Variable due to power management)
└─ Matrix Ops: 80-300ms   (Limited cache, thermal limits)

System Indicators:
├─ Memory Locking: 🔴 FAILED (normal - power management)
├─ RT Priority: 🔴 INACTIVE (normal - battery optimization)  
├─ CPU Affinity: 🟡 PARTIAL (may work, power dependent)
└─ Garbage Collection: 🟢 DISABLED (software control)
```

#### **Performance Interpretation Guide**

**Quicksort Timing Analysis:**
- **< 5ms**: Excellent RT system or high-end CPU
- **5-15ms**: Normal desktop/server performance  
- **15-30ms**: Laptop/mobile or thermal throttling
- **> 30ms**: System under load or configuration issues

**System Health Indicators:**
- **Consistent timing** (±10%): Good system stability
- **High variance** (±50%): Interference from other processes
- **Progressive slowdown**: Thermal throttling or memory pressure
- **Sudden spikes**: GC pauses or system interruptions

**When Results Don't Match Expectations:**
```bash
# If quicksort > 50ms on desktop system:
python3 tests/test_rtos_config.py  # Check system optimization
python3 tests/test_platform_compatibility.py  # Verify basic setup

# High variance in results:
# → Other processes running (close unnecessary apps)
# → Thermal throttling (check CPU temperature)  
# → Insufficient permissions (try admin/sudo)
```

#### **Choosing the Right Benchmark Mode**

**For Learning (Any System):**
```bash
python3 learn_algorithms.py  # Educational demos work everywhere
```

**For Development (Desktop):**
```bash
python3 main_simplified.py  # General performance testing
```

**For Production Validation (RT System):**
```bash
sudo python3 main.py  # Full benchmark with RT optimizations
```

### Installation

```bash
# Clone or download the project
cd rtos_benchmark

# Ensure Python 3.6+ is installed
python3 --version

# No additional dependencies required - uses only standard library
```

### Multiple Entry Points

Choose the best entry point for your needs:

#### 🎯 **Recommended: Streamlined Entry Point**
```bash
# Fast, direct execution (recommended for most users)
python3 main_simplified.py
```

#### 🎯 **Full CLI Interface**
```bash
# Complete benchmark suite with CLI options
python3 main.py

# Run quick benchmark (30 seconds)
python3 main.py --quick

# Show system information
python3 main.py --system-info

# Show help
python3 main.py --help
```

#### 🎯 **Backward Compatibility**
```bash
# For existing scripts/workflows
python3 rtos_full_board_benchmark.py
```

#### 🎓 **Educational Usage (NEW!)**
```bash
# Interactive algorithm learning laboratory
python3 learn_algorithms.py

# Compare algorithm performance and learn Big O complexity
python3 -c "from src.algorithms import AlgorithmLearningLab; lab = AlgorithmLearningLab(); lab.algorithm_comparison_demo()"

# Explore best vs worst case scenarios
python3 -c "from src.algorithms import AlgorithmLearningLab; lab = AlgorithmLearningLab(); lab.demonstrate_best_vs_worst_case()"

# Get algorithm selection guidance
python3 -c "from src.algorithms import AlgorithmLearningLab; lab = AlgorithmLearningLab(); lab.explain_algorithm_choice()"
```

# View recent results
python3 main.py --results

# Show help
python3 main.py --help
```

## Project Structure

```
rtos_benchmark/
├── main.py                     # Main entry point and CLI
├── src/                        # Source code modules
│   ├── __init__.py
│   ├── platform_compat.py      # Cross-platform compatibility layer
│   ├── algorithms.py           # Algorithm benchmarking
│   ├── rtos_env.py             # RTOS environment management
│   ├── cyclictest.py           # cyclictest integration and simulation
│   ├── results_board.py        # Results formatting and display
│   ├── multicore.py            # Multicore management and CPU affinity
│   └── benchmark_orchestrator.py # Main benchmark coordination
├── tests/                      # Test modules (for future expansion)
│   └── __init__.py
├── docs/                       # Documentation (for future expansion)
│   └── __init__.py
└── README.md                   # This file
```

## Detailed Features

### Real-time Latency Testing
- **cyclictest Integration**: Direct integration with the industry-standard cyclictest tool
- **Simulation Mode**: Realistic latency simulation when cyclictest is unavailable
- **Multiple Priority Levels**: Tests with different RT priority settings
- **Statistical Analysis**: Min/Max/Average latency with jitter calculation

### Algorithm Benchmarking
- **Sorting Algorithms**: Quick sort and merge sort performance comparison
- **Mathematical Operations**: Matrix multiplication and FFT simulation
- **Execution Time Tracking**: Precise timing with multiple iterations
- **Memory Efficiency**: Monitoring of algorithm memory usage patterns

### Multicore Support
- **CPU Topology Detection**: Automatic detection of cores and hyperthreading
- **CPU Affinity Management**: Process isolation to specific cores
- **Parallel Stress Testing**: Coordinated multicore performance evaluation
- **Load Balancing Analysis**: System behavior under distributed workloads

### Cross-platform Compatibility
- **Linux**: Full RT support with cyclictest, memory locking, and RT scheduling
- **macOS**: Adapted performance testing with BSD-compatible features
- **Windows**: Performance testing with Windows-specific optimizations
- **Automatic Fallbacks**: Graceful degradation when features are unavailable

## System Requirements

### Minimum Requirements
- Python 3.6 or higher
- 1 GB available memory
- Multi-core CPU (recommended)

### Optimal Requirements
- Linux with RT kernel (for full real-time testing)
- cyclictest installed (`sudo apt install rt-tests` on Ubuntu/Debian)
- Root/sudo privileges (for RT scheduling and memory locking)
- 4+ CPU cores (for multicore testing)

### Supported Platforms
- **Linux** (Ubuntu, Debian, CentOS, RHEL, etc.) - Full feature support
- **macOS** (10.12+) - Core features with platform adaptations
- **Windows** (10/11) - Core features with Windows-specific optimizations

## Understanding Results

### Performance Metrics

#### Real-time Latency
- **Max Latency**: Highest response time measured (lower is better)
- **Average Latency**: Mean response time across all measurements
- **Jitter**: Variation in response times (Max - Min)

#### Performance Ratings
- **Excellent**: Max latency ≤ 20μs, Average ≤ 10μs
- **Good**: Max latency ≤ 50μs, Average ≤ 25μs
- **Fair**: Max latency ≤ 100μs, Average ≤ 50μs
- **Poor**: Higher latencies indicating non-RT performance

#### Composite Score
The benchmark calculates a weighted composite score:
- **Latency (40%)**: Real-time response performance
- **Algorithms (30%)**: Computational efficiency
- **System (20%)**: Hardware capabilities and optimization
- **Environment (10%)**: Thermal and system state factors

### Results Files
- Results are automatically saved as `rtos_full_board_results_YYYYMMDD_HHMMSS.json`
- JSON format for easy parsing and analysis
- Includes complete system information and test metadata

## Advanced Usage

### Custom Configuration
The benchmark can be customized by modifying the configuration in `benchmark_orchestrator.py`:

```python
custom_config = {
    'duration': 30,              # Test duration in seconds
    'priority': 90,              # RT priority level (1-99)
    'algorithm_tests': True,     # Enable algorithm benchmarks
    'multicore_tests': True,     # Enable multicore testing
    'environment_monitoring': True,  # Monitor system state
    'save_results': True,        # Save results to JSON
    'show_progress': True        # Display progress updates
}
```

### Integration with Other Tools
The benchmark is designed to integrate with:
- **CI/CD Pipelines**: Automated performance regression testing
- **Monitoring Systems**: Regular system performance evaluation
- **Development Workflows**: Performance impact assessment

## Troubleshooting

### Common Issues

#### Permission Denied Errors
```bash
# Run with appropriate privileges for RT features
sudo python3 main.py
```

#### cyclictest Not Found
The benchmark automatically falls back to simulation mode. For real measurements:
```bash
# Ubuntu/Debian
sudo apt install rt-tests

# CentOS/RHEL
sudo yum install rt-tests
```

#### Memory Locking Failures
Check system limits:
```bash
ulimit -l  # Should show 'unlimited' or high value
```

### Platform-specific Notes

#### Linux
- Install `rt-tests` package for cyclictest
- Consider using RT kernel for optimal results
- May require root privileges for some features

#### macOS
- Some RT features limited due to platform restrictions
- Uses high-resolution timing alternatives
- Performance results may vary from Linux

#### Windows
- Limited RT capabilities compared to Linux
- Uses Windows performance counters
- Requires Python 3.6+ with appropriate permissions

## Contributing

This benchmark suite is designed to be modular and extensible. The new architecture makes contributions easier than ever!

### 🎯 Easy Contribution Areas

1. **Algorithm Enhancements**: Add new benchmarks in `src/algorithms.py`
2. **Platform Support**: Enhance `src/platform_compat.py` for new platforms
3. **Visualization**: Extend `src/results_board.py` with charts and graphs
4. **Testing**: Add unit tests in `tests/` directory
5. **Documentation**: Improve module-specific documentation

### 🧪 Development Workflow & Testing

The RTOS Benchmark Suite includes comprehensive testing to ensure reliability across platforms and configurations.

#### 🔍 Test Suite Overview

Our testing framework validates:
- **Cross-platform compatibility** (Linux, macOS, Windows)
- **RTOS configuration validation** (real-time priorities, memory locking)
- **Algorithm correctness** and performance baselines
- **Module integration** and dependency management

#### 🚀 Running Tests

##### Complete Test Suite
```bash
# Run all tests with pytest (recommended)
python3 -m pytest tests/ -v

# Alternative: Run all tests manually
python3 tests/test_platform_compatibility.py
python3 tests/test_rtos_config.py
```

##### Individual Test Categories

**1. Platform Compatibility Test**
```bash
python3 tests/test_platform_compatibility.py
```
*What it tests:*
- Python version compatibility (3.6+ required)
- Operating system detection (Linux/macOS/Windows)
- Required module imports (multiprocessing, threading, etc.)
- CPU architecture and processor information
- Basic module functionality without full benchmark execution

**2. RTOS Configuration Test**
```bash
python3 tests/test_rtos_config.py
```
*What it tests:*
- Memory locking capabilities (`mlockall`)
- Real-time scheduling priorities (`SCHED_FIFO`)
- CPU affinity control for core isolation
- Garbage collection management
- System-level real-time optimizations

##### Module-Specific Testing
```bash
# Test individual modules (development)
python3 -c "import src.platform_compat; print('✅ Platform module works')"
python3 -c "import src.algorithms; print('✅ Algorithms module works')"
python3 -c "import src.rtos_env; print('✅ RTOS environment works')"
```

#### 📊 Understanding Test Output & How Tests Work

**Platform Compatibility Results:**
```
🧪 CROSS-PLATFORM COMPATIBILITY TEST
📍 Python Version: 3.11.0
📍 Operating System: Windows
📍 Architecture: AMD64
📍 Processor: Intel64 Family 6 Model 142 Stepping 10

🔍 Testing required imports:
  ✅ gc
  ✅ multiprocessing
  ✅ threading
  [... all modules tested]

📊 Test Summary: 15/15 tests passed ✅
```

**RTOS Configuration Results:**
```
🔬 RTOS Configuration Test
Memory Locking (mlockall): 🟢 LOCKED
Real-Time Priority (99): 🟢 ACTIVE (SCHED_FIFO)
CPU Affinity: 🟢 CORE 3 ISOLATED
Garbage Collection: 🟢 DISABLED
```

#### 🔬 Deep Dive: How Each Test Works

##### **Platform Compatibility Test Explained**

**What it does:** Validates your system can run RTOS benchmarks without executing the full suite.

**Internal Process:**
1. **Python Version Check**: 
   ```python
   python_version = sys.version_info
   if python_version < (3, 6): return False
   ```
   - *Why*: Async/await syntax and f-strings require Python 3.6+
   - *Impact*: Older Python versions will fail multiprocessing tests

2. **Operating System Detection**:
   ```python
   system = platform.system().lower()  # 'linux', 'darwin', 'windows'
   ```
   - *Why*: Different OS require different system calls for RT features
   - *Impact*: Determines which RTOS optimizations are available

3. **Module Import Testing**:
   ```python
   for module in ['multiprocessing', 'threading', 'subprocess']:
       __import__(module)  # Fails if module missing
   ```
   - *Why*: Benchmarks use these modules for parallel execution
   - *Impact*: Missing modules = benchmark crashes

4. **CPU Architecture Detection**:
   ```python
   arch = platform.machine()  # 'x86_64', 'aarch64', 'AMD64'
   ```
   - *Why*: Some optimizations are architecture-specific
   - *Impact*: Affects memory alignment and SIMD instructions

##### **RTOS Configuration Test Explained**

**What it does:** Tests real-time system capabilities that affect benchmark accuracy.

**Internal Process:**

1. **Memory Locking (`mlockall`)**:
   ```python
   libc = ctypes.CDLL(ctypes.util.find_library('c'))
   result = libc.mlockall(MCL_CURRENT | MCL_FUTURE)
   ```
   - *What it does*: Locks all process memory in RAM
   - *Why important*: Prevents memory swapping during benchmarks
   - *Impact if failed*: Unpredictable latency spikes from disk I/O
   - *🟢 LOCKED*: Memory won't be swapped to disk
   - *🔴 FAILED*: Benchmark results may have swap-induced jitter

2. **Real-Time Priority (`SCHED_FIFO`)**:
   ```python
   param = os.sched_param(99)  # Highest RT priority
   os.sched_setscheduler(0, SCHED_FIFO, param)
   ```
   - *What it does*: Sets process to real-time FIFO scheduling
   - *Why important*: Preempts all non-RT processes
   - *Impact if failed*: Other processes can interrupt benchmarks
   - *🟢 ACTIVE*: Process runs with RT priority 99
   - *🟡 HIGH PRIORITY*: Falls back to `nice -20` (still good)
   - *🔴 INACTIVE*: Normal scheduling (results less consistent)

3. **CPU Affinity (Core Isolation)**:
   ```python
   os.sched_setaffinity(0, {3})  # Pin to CPU core 3
   ```
   - *What it does*: Binds process to specific CPU core
   - *Why important*: Eliminates cache misses from core migration
   - *Impact if failed*: CPU migration causes performance variance
   - *🟢 ISOLATED*: Process locked to one core
   - *🔴 FAILED*: Process can migrate between cores

4. **Garbage Collection Control**:
   ```python
   gc.disable()  # Stop automatic garbage collection
   ```
   - *What it does*: Prevents automatic memory cleanup
   - *Why important*: GC pauses create latency spikes
   - *Impact if failed*: Unpredictable pauses during benchmarks
   - *🟢 DISABLED*: No GC interruptions
   - *🔴 FAILED*: GC may interrupt time-critical sections

#### 🎯 Test Status Indicators

- **🟢 ACTIVE/LOCKED**: Full real-time capability available
- **🟡 PARTIAL**: Limited capability (e.g., high priority instead of RT)
- **🔴 FAILED/INACTIVE**: Feature unavailable (may impact benchmark accuracy)

#### 📈 What Test Results Mean for Benchmark Quality

**🟢 All Green (Ideal Conditions):**
```
Memory Locking: 🟢 LOCKED
RT Priority: 🟢 ACTIVE (SCHED_FIFO)  
CPU Affinity: 🟢 CORE 3 ISOLATED
GC Control: 🟢 DISABLED
```
- **Benchmark Quality**: ⭐⭐⭐⭐⭐ Excellent
- **Latency Consistency**: < 1μs jitter
- **Result Reliability**: Publication-ready data
- **Use Cases**: Research, RT system validation, performance baselines

**🟡 Mixed Results (Good Conditions):**
```
Memory Locking: 🔴 FAILED
RT Priority: 🟡 HIGH PRIORITY (nice -20)
CPU Affinity: 🟢 CORE 3 ISOLATED  
GC Control: 🟢 DISABLED
```
- **Benchmark Quality**: ⭐⭐⭐⭐ Very Good
- **Latency Consistency**: 1-10μs jitter
- **Result Reliability**: Suitable for development testing
- **Use Cases**: Algorithm comparison, development workflow

**🔴 Many Red (Limited Conditions):**
```
Memory Locking: 🔴 FAILED
RT Priority: 🔴 INACTIVE
CPU Affinity: 🔴 FAILED
GC Control: 🟢 DISABLED
```
- **Benchmark Quality**: ⭐⭐ Fair
- **Latency Consistency**: 10-100μs+ jitter
- **Result Reliability**: Trend analysis only
- **Use Cases**: Educational demos, rough algorithm comparison

#### ⚠️ Common Test Scenarios & Interpretations

**Scenario 1: Development Laptop (Typical)**
```bash
$ python3 tests/test_rtos_config.py
Memory Locking: 🔴 FAILED (no permissions)
RT Priority: 🔴 INACTIVE (no permissions) 
CPU Affinity: 🟢 CORE 3 ISOLATED
GC Control: 🟢 DISABLED
```
*Interpretation*: Good for learning and algorithm comparison, but not precision timing.

**Scenario 2: Linux RT Kernel (Production)**
```bash
$ sudo python3 tests/test_rtos_config.py
Memory Locking: 🟢 LOCKED
RT Priority: 🟢 ACTIVE (SCHED_FIFO)
CPU Affinity: 🟢 CORE 3 ISOLATED
GC Control: 🟢 DISABLED
```
*Interpretation*: Ideal conditions - research-grade benchmark results.

**Scenario 3: Windows with Admin (Enterprise)**
```bash
$ python3 tests/test_rtos_config.py  # Run as Administrator
Memory Locking: 🔴 FAILED (Windows limitation)
RT Priority: 🟡 HIGH PRIORITY (Windows equivalent)
CPU Affinity: 🟢 CORE 3 ISOLATED
GC Control: 🟢 DISABLED
```
*Interpretation*: Good Windows performance, limited by OS real-time capabilities.

#### 🔧 Test-Driven Development

When contributing to the project:

```bash
# 1. Write your test first
echo "def test_new_feature(): assert new_function() == expected" > tests/test_new_feature.py

# 2. Run tests to see failure
python3 -m pytest tests/test_new_feature.py

# 3. Implement feature in appropriate src/ module
# 4. Run tests again to verify success
python3 -m pytest tests/ -v

# 5. Test educational examples
python3 learn_algorithms.py
```

#### 🧠 Technical Deep Dive: Why These Tests Matter

**Memory Locking Impact on Results:**
```python
# Without mlockall: Memory pages can be swapped
benchmark_time = 1.23ms  # ... later becomes 15.67ms (swap hit!)

# With mlockall: All memory stays in RAM  
benchmark_time = 1.23ms  # ... consistently 1.24ms, 1.22ms
```

**Real-Time Priority Impact:**
```python
# Normal priority: OS can interrupt for email, background tasks
quicksort_time = [1.2ms, 8.5ms, 1.3ms, 12.1ms]  # Inconsistent!

# RT priority: Process runs uninterrupted
quicksort_time = [1.2ms, 1.3ms, 1.2ms, 1.3ms]   # Consistent!
```

**CPU Affinity Impact:**
```python
# No affinity: Process migrates between cores
cache_miss_rate = 15%  # Cache is cold on new core

# Pinned to core: Process stays on same core  
cache_miss_rate = 2%   # Cache stays warm
```

**Garbage Collection Impact:**
```python
# GC enabled: Unpredictable pauses
algorithm_timing = [1ms, 1ms, 15ms, 1ms]  # 15ms = GC pause!

# GC disabled: Predictable execution
algorithm_timing = [1ms, 1ms, 1ms, 1ms]   # Consistent performance
```

#### 🎯 Choosing the Right Test Environment

**For Learning & Education:**
- Minimum requirements: ✅ Platform compatibility test passes
- Test command: `python3 tests/test_platform_compatibility.py`
- Acceptable results: Basic imports work, any OS

**For Algorithm Development:**
- Recommended: 🟢 GC disabled + 🟢 CPU affinity  
- Test command: `python3 tests/test_rtos_config.py`
- Acceptable results: 2+ green indicators for consistent timing

**For Research & Publication:**
- Required: 🟢 All indicators green
- Test command: `sudo python3 tests/test_rtos_config.py` (Linux RT kernel)
- Acceptable results: Full real-time configuration

**For Production Validation:**
- Critical: 🟢 Memory locked + 🟢 RT priority
- Test environment: Dedicated RT system, isolated cores
- Acceptable results: Sub-microsecond timing precision

#### 🐛 Troubleshooting Test Issues

**Permission Errors (Linux/macOS):**
```bash
# For real-time priorities, run with elevated privileges
sudo python3 tests/test_rtos_config.py
```

**Windows-Specific Issues:**
```bash
# Run PowerShell as Administrator for full RTOS testing
# Some features may show 🟡 PARTIAL instead of 🟢 ACTIVE
```

**Import Errors:**
```bash
# Ensure you're in the project root directory
cd rtos_benchmark/
python3 -m pytest tests/
```

#### 📈 Continuous Integration

The test suite is designed for:
- **Pre-commit validation**: Run tests before code changes
- **CI/CD pipelines**: Automated testing on multiple platforms  
- **Performance regression**: Baseline validation for algorithm changes
- **Educational verification**: Ensure learning examples remain accurate

## 📦 Migration from Original Version

If you were using the original monolithic file:

### Import Changes
```python
# OLD (2400+ line file)
from rtos_full_board_benchmark import RTOSEnvironment

# NEW (modular)
from src.rtos_env import RTOSEnvironment
```

### Entry Point Changes
- **Old**: `python3 rtos_full_board_benchmark.py`
- **New (recommended)**: `python3 main_simplified.py`
- **Backward compatible**: Still works with old entry point

## 🗂️ File Organization

- **`old_py/`** - Contains original 2400+ line file for reference
- **`redundant/`** - Non-essential files archived but preserved
- **`src/`** - Clean, modular implementation
- **`tests/`** - Test suite for validation

## License

MIT License - see LICENSE file for details.

## Authors

**Created by:** Domas Užkuraitis  
**GitHub:** [@Domauzku6](https://github.com/Domauzku6)  
**Email:** uzkuraitis.domas@gmail.com


## Changelog

### v3.1 (Current - Educational Edition)
- 🎓 **NEW: Educational Features**: Interactive algorithm learning laboratory
- 🎓 **NEW: Learning Demo**: `learn_algorithms.py` for hands-on education
- 🎓 **Enhanced Documentation**: Step-by-step algorithm explanations with complexity analysis
- 🎓 **Algorithm Comparison Tools**: Interactive demos showing Big O complexity in practice
- 🎓 **Best vs Worst Case Analysis**: Understand how input patterns affect performance
- 🎓 **Algorithm Selection Guide**: Learn when to choose each algorithm
- ✅ **Educational Code Comments**: Detailed explanations for learning optimization techniques

### v3.0 (Previous - Modular Edition)
- ✅ **Major**: Split 2400+ line file into 8 focused modules
- ✅ **Performance**: Faster startup and reduced memory footprint
- ✅ **Maintainability**: Clean architecture with single-responsibility modules
- ✅ **Organization**: Archived old files, removed redundancy
- ✅ **Documentation**: Enhanced README and per-module documentation
- ✅ **Entry Points**: Multiple entry points for different use cases
- ✅ **Backward Compatibility**: Original entry point still works

### v2.0 (Legacy)
- Modular architecture with separated concerns
- Enhanced cross-platform compatibility
- Improved error handling and fallback mechanisms

### v1.0 (Original)
- Initial monolithic implementation
- Basic cyclictest integration
- Core algorithm benchmarking functionality

---

**🎓 Ready to learn? Try `python3 learn_algorithms.py` for the educational experience!**
**🚀 Ready to benchmark? Try `python3 main_simplified.py` for performance testing!**