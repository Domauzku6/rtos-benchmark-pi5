"""
RTOS Benchmark Suite
====================

A comprehensive cross-platform RTOS benchmarking toolkit.

Modules:
--------
- platform_compat: Cross-platform compatibility layer
- algorithms: Sorting algorithm implementations
- rtos_env: RTOS environment management
- cyclictest: Cyclictest integration and simulation
- multicore: Multi-core testing utilities
- display: Results display and visualization
- benchmark: Main benchmark orchestration

Usage:
------
    from rtos_benchmark import RTOSBenchmark
    
    benchmark = RTOSBenchmark()
    results = benchmark.run()

Author: RTOS Benchmark Suite Team
License: MIT
Version: 2.0.0
"""

__version__ = "2.0.0"
__author__ = "RTOS Benchmark Suite Team"
__license__ = "MIT"

# Main imports for easy access
from .src.benchmark import ComprehensiveRTOSBenchmarkWithBoard
from .src.platform_compat import PlatformCompat

# Convenience alias
RTOSBenchmark = ComprehensiveRTOSBenchmarkWithBoard

__all__ = [
    'RTOSBenchmark',
    'ComprehensiveRTOSBenchmarkWithBoard',
    'PlatformCompat',
    '__version__',
    '__author__',
    '__license__'
]