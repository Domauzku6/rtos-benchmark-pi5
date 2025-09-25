"""
RTOS Benchmark Suite - Source Package
====================================

A comprehensive real-time operating system benchmark suite with
modular architecture for maintainable and extensible testing.

Modules:
--------
- platform_compat: Cross-platform compatibility layer
- algorithms: Algorithm benchmarking and performance testing
- rtos_env: RTOS environment setup and management
- cyclictest: cyclictest integration and latency simulation
- results_board: Results formatting, display, and management
- multicore: Multicore management and CPU affinity
- benchmark_orchestrator: Main benchmark coordination and orchestration

Usage:
------
    from src.benchmark_orchestrator import RTOSBenchmarkOrchestrator
    
    orchestrator = RTOSBenchmarkOrchestrator()
    results = orchestrator.run_comprehensive_benchmark()

Author: RTOS Benchmark Suite Team
"""

# Version information
__version__ = "2.0.0"
__author__ = "RTOS Benchmark Suite Team"

# Import main components for easier access
from .benchmark_orchestrator import RTOSBenchmarkOrchestrator
from .results_board import ResultsBoard
from .platform_compat import platform_compat

# Define what gets imported with "from src import *"
__all__ = [
    'RTOSBenchmarkOrchestrator',
    'ResultsBoard', 
    'platform_compat'
]