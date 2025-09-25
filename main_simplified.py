#!/usr/bin/env python3
"""
COMPREHENSIVE RTOS BENCHMARK WITH FULL RESULTS BOARD
====================================================

This enhanced version provides:
1. Complete RTOS + cyclictest integration
2. Comprehensive results dashboard/board
3. Visual performance analysis
4. Real-time certification board
5. Detailed system analysis display

CROSS-PLATFORM SUPPORT
======================
✅ Linux (Full features)
✅ macOS (Limited RT features)
✅ Windows (Algorithm testing only)

SYSTEM REQUIREMENTS
==================
• Python 3.6+ (recommended: 3.8+)
• No external Python packages required
• Optional: cyclictest (Linux only, for RT latency testing)

INSTALLATION GUIDE
==================

Linux (Ubuntu/Debian):
----------------------
# Install cyclictest (optional but recommended for full RT testing)
sudo apt-get update
sudo apt-get install rt-tests

# Run the benchmark
sudo python3 main.py

Linux (RHEL/CentOS/Fedora):
---------------------------
# Install cyclictest
sudo yum install rt-tests
# or for newer versions:
sudo dnf install rt-tests

# Run the benchmark
sudo python3 main.py

macOS:
------
# No additional packages needed, but RT features are limited
python3 main.py

Windows:
--------
# No additional packages needed, algorithm testing only
python main.py

FEATURES BY PLATFORM
====================
Linux:
• ✅ Real-time scheduling (SCHED_FIFO)
• ✅ Memory locking (mlockall)
• ✅ CPU temperature monitoring
• ✅ System cache control
• ✅ cyclictest latency testing
• ✅ CPU core affinity setting
• ✅ All algorithm performance tests

macOS:
• ❌ Real-time scheduling (not available)
• ❌ Memory locking (not available)
• ⚡ CPU temperature monitoring (limited)
• ❌ System cache control (not needed)
• ❌ cyclictest (not available, uses simulation)
• ❌ CPU core affinity (not available)
• ✅ All algorithm performance tests

Windows:
• ❌ Real-time scheduling (not available)
• ❌ Memory locking (not available)
• ❌ CPU temperature monitoring (complex)
• ❌ System cache control (not needed)
• ❌ cyclictest (not available, uses simulation)
• ❌ CPU core affinity (not implemented)
• ✅ All algorithm performance tests

Run with: 
  Linux:   sudo python3 main.py
  macOS:   python3 main.py
  Windows: python main.py

Cross-platform support: Linux, Windows, macOS
"""

import os
import platform

# Import modules from src directory
try:
    from src.platform_compat import platform_compat
    from src.benchmark_orchestrator import RTOSBenchmarkOrchestrator
except ImportError as e:
    print(f"❌ Error importing modules: {e}")
    print("Make sure all files in the src/ directory are present")
    exit(1)


def main():
    """Main execution function"""
    print("🚀 Starting Comprehensive RTOS Benchmark with Full Results Board")
    print(f"📱 Platform: {platform_compat.system.title()} ({platform.machine()})")
    
    # Platform-specific privilege checks
    if platform_compat.is_unix:
        if hasattr(os, 'geteuid') and os.geteuid() != 0:
            print("⚠️ WARNING: Not running as root - some optimizations may not be available")
            print("   For best results on Linux, run with: sudo python3 main.py")
        else:
            print("✅ Running with root privileges - full optimization available")
    else:
        print(f"ℹ️ Running on {platform_compat.system.title()} - using available optimizations")
    
    # Check available features
    print("\n🔍 Checking system capabilities:")
    print(f"   Real-time scheduling: {'✅ Available' if platform_compat.supports_rt_scheduling() else '❌ Not available'}")
    print(f"   Root privileges: {'✅ Available' if platform_compat.has_root_privileges() else '❌ Not available'}")
    print(f"   Temperature monitoring: {'✅ Available' if platform_compat.get_cpu_temperature() else '❌ Not available'}")
    print(f"   Cyclictest: {'✅ Available' if platform_compat.has_cyclictest() else '❌ Not available (will simulate)'}")
    
    # More detailed cache control info
    if platform_compat.is_linux:
        if platform_compat.has_root_privileges():
            cache_available = platform_compat.drop_system_caches()
            # Test and restore - we're just checking capability
            print(f"   System cache control: {'✅ Available' if cache_available else '⚠️ Limited (check /proc/sys/vm/drop_caches)'}")
        else:
            print(f"   System cache control: ⚠️ Requires root privileges")
    else:
        print(f"   System cache control: ❌ Not available on {platform_compat.system.title()}")
    
    system_info = platform_compat.get_system_info()
    print(f"   Multi-core processing: ✅ Available ({system_info.get('cpu_count', 'Unknown')} cores)")
    
    # Initialize benchmark orchestrator
    benchmark = RTOSBenchmarkOrchestrator()
    
    try:
        # Validate system requirements
        validation = benchmark.validate_system_requirements()
        
        if validation['warnings']:
            print("\n⚠️ System warnings:")
            for warning in validation['warnings']:
                print(f"   • {warning}")
        
        if validation['recommendations']:
            print("\n💡 Recommendations:")
            for rec in validation['recommendations']:
                print(f"   • {rec}")
        
        # Run comprehensive benchmark
        duration = 15 if not platform_compat.has_cyclictest() else 30
        print(f"\n🧪 Starting benchmark suite (duration: {duration}s)...")
        
        config = {
            'duration': duration,
            'priority': 99,
            'algorithm_tests': True,
            'multicore_tests': True,
            'environment_monitoring': True,
            'save_results': True,
            'show_progress': True
        }
        
        results = benchmark.run_comprehensive_benchmark(config)
        
        print("\n🎯 COMPREHENSIVE BENCHMARK COMPLETE!")
        print("Results include:")
        print("• Complete visual results dashboard")
        print("• Algorithm performance analysis")
        print("• Real-time latency analysis")
        print("• System validation and recommendations")
        print("• Performance monitoring and optimization analysis")
        
    except KeyboardInterrupt:
        print("\n🛑 Benchmark interrupted by user")
    except Exception as e:
        print(f"\n❌ Benchmark failed: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()