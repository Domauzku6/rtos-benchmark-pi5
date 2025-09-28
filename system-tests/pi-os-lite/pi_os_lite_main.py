#!/usr/bin/env python3
"""
RTOS Full Board Benchmark Suite - Main Entry Point
==================================================

A comprehensive real-time operating system benchmark suite that tests
system performance, real-time capabilities, and algorithm efficiency.

This modular version provides organized, maintainable code structure
while preserving all functionality of the original benchmark.

Usage:
------
    python main.py                    # Run full benchmark
    python main.py --quick            # Run quick benchmark
    python main.py --help             # Show help

Features:
---------
- Real-time latency measurement with cyclictest integration
- Algorithm performance benchmarking
- Multicore system testing and optimization
- Cross-platform compatibility (Linux/macOS/Windows)
- Comprehensive results reporting and comparison
- Modular architecture for easy maintenance

Author: RTOS Benchmark Suite Team
License: MIT
"""

import sys
import argparse
import os
from datetime import datetime

# Add src directory to Python path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from src.benchmark_orchestrator import RTOSBenchmarkOrchestrator
    from src.results_board import ResultsBoard
    from src.platform_compat import platform_compat
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Please ensure you're running from the rtos_benchmark directory")
    sys.exit(1)


def print_banner():
    """Print the application banner"""
    banner = """
╔══════════════════════════════════════════════════════════════════╗
║                    RTOS Benchmark Suite v2.0                    ║
║                     Real-Time Performance Testing                ║
╠══════════════════════════════════════════════════════════════════╣
║  Features: Real-time latency • Algorithm testing • Multicore    ║
║           Cross-platform • Comprehensive reporting              ║
╚══════════════════════════════════════════════════════════════════╝
    """.strip()
    print(banner)
    print()


def print_system_overview():
    """Print system overview information"""
    print("🖥️  System Overview")
    print("-" * 30)
    
    system_info = platform_compat.get_system_info()
    
    print(f"Operating System: {system_info.get('os_info', 'Unknown')}")
    print(f"CPU: {system_info.get('cpu_info', 'Unknown')}")
    print(f"Memory: {system_info.get('memory_gb', 'Unknown')} GB")
    print(f"Python: {system_info.get('python_version', 'Unknown')}")
    print(f"Architecture: {system_info.get('architecture', 'Unknown')}")
    
    # RT capabilities
    rt_capable = platform_compat.supports_rt_scheduling()
    cyclictest_available = platform_compat.has_cyclictest()
    
    print(f"RT Scheduling: {'✅ Available' if rt_capable else '❌ Not available'}")
    print(f"cyclictest: {'✅ Available' if cyclictest_available else '❌ Not available (will simulate)'}")
    print()


def run_full_benchmark():
    """Run the complete benchmark suite"""
    print("🚀 Running Full Benchmark Suite")
    print("=" * 50)
    print("This will take approximately 2-3 minutes...")
    print()
    
    orchestrator = RTOSBenchmarkOrchestrator()
    results = orchestrator.run_comprehensive_benchmark()
    
    # Generate and display comprehensive report
    print("\n" + "=" * 60)
    report = orchestrator.generate_comprehensive_report(results)
    print(report)
    
    return results


def run_quick_benchmark():
    """Run a quick benchmark"""
    print("⚡ Running Quick Benchmark")
    print("=" * 50)
    print("This will take approximately 30 seconds...")
    print()
    
    orchestrator = RTOSBenchmarkOrchestrator()
    results = orchestrator.run_quick_benchmark()
    
    # Display basic results
    print("\n" + "=" * 40)
    results_board = ResultsBoard()
    summary = results_board.get_performance_summary(results)
    print("🎯 Quick Benchmark Results")
    print("-" * 40)
    print(summary)
    print()
    
    # Show basic metrics
    cyclictest = results.get('cyclictest_results', {})
    if cyclictest.get('success'):
        max_lat = cyclictest.get('max_latency_us', 'N/A')
        avg_lat = cyclictest.get('avg_latency_us', 'N/A')
        print(f"Real-time Latency: Max {max_lat}μs, Avg {avg_lat}μs")
    
    composite_score = results.get('composite_score', {}).get('composite_score', 'N/A')
    print(f"Performance Score: {composite_score}")
    
    return results


def show_recent_results():
    """Show recent benchmark results"""
    print("📊 Recent Benchmark Results")
    print("=" * 50)
    
    # Look for recent result files
    import glob
    result_files = glob.glob("rtos_full_board_results_*.json")
    result_files.sort(reverse=True)  # Most recent first
    
    if not result_files:
        print("No previous benchmark results found.")
        return
    
    results_board = ResultsBoard()
    
    # Load and display recent results
    recent_results = []
    for filename in result_files[:5]:  # Show up to 5 recent results
        result_data = results_board.load_results_from_file(filename)
        if result_data:
            recent_results.append(result_data)
    
    if recent_results:
        leaderboard = results_board.generate_leaderboard(recent_results)
        print(leaderboard)
    else:
        print("Could not load recent results.")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="RTOS Benchmark Suite - Comprehensive real-time system testing",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                 Run full benchmark suite
  python main.py --quick         Run quick benchmark (30 seconds)
  python main.py --results       Show recent results
  python main.py --system-info   Show detailed system information

For more information, visit: https://github.com/your-repo/rtos-benchmark
        """
    )
    
    parser.add_argument('--quick', '-q', 
                       action='store_true',
                       help='Run quick benchmark (faster, less comprehensive)')
    
    parser.add_argument('--results', '-r',
                       action='store_true', 
                       help='Show recent benchmark results')
    
    parser.add_argument('--system-info', '-s',
                       action='store_true',
                       help='Show detailed system information')
    
    parser.add_argument('--no-banner',
                       action='store_true',
                       help='Skip banner display')
    
    parser.add_argument('--version', '-v',
                       action='version',
                       version='RTOS Benchmark Suite v2.0')
    
    args = parser.parse_args()
    
    # Print banner unless suppressed
    if not args.no_banner:
        print_banner()
    
    try:
        if args.system_info:
            print_system_overview()
            
            # Additional detailed system info
            orchestrator = RTOSBenchmarkOrchestrator()
            validation = orchestrator.validate_system_requirements()
            
            if validation.get('warnings'):
                print("⚠️  System Warnings:")
                for warning in validation['warnings']:
                    print(f"   • {warning}")
                print()
            
            if validation.get('recommendations'):
                print("💡 Recommendations:")
                for rec in validation['recommendations']:
                    print(f"   • {rec}")
                print()
        
        elif args.results:
            show_recent_results()
        
        elif args.quick:
            print_system_overview()
            results = run_quick_benchmark()
            
        else:
            # Default: run full benchmark
            print_system_overview()
            results = run_full_benchmark()
    
    except KeyboardInterrupt:
        print("\n\n⚠️  Benchmark interrupted by user.")
        print("Partial results may be available in JSON files.")
        sys.exit(130)
    
    except Exception as e:
        print(f"\n❌ Benchmark failed with error: {e}")
        print("Please check your system configuration and try again.")
        sys.exit(1)


if __name__ == "__main__":
    main()