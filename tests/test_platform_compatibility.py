#!/usr/bin/env python3
"""
Cross-Platform Test Script for RTOS Benchmark
==============================================

This script tests the cross-platform compatibility of the RTOS benchmark
without running the full benchmark suite.
"""

import sys
import os
import platform

def test_platform_compatibility():
    """Test platform compatibility without running full benchmark"""
    
    print("🧪 CROSS-PLATFORM COMPATIBILITY TEST")
    print("=" * 60)
    
    # Test basic Python version
    python_version = sys.version_info
    print(f"📍 Python Version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version < (3, 6):
        print("❌ ERROR: Python 3.6+ required")
        return False
    else:
        print("✅ Python version compatible")
    
    # Test platform detection
    system = platform.system().lower()
    print(f"📍 Operating System: {system.title()}")
    print(f"📍 Architecture: {platform.machine()}")
    print(f"📍 Processor: {platform.processor() or 'Unknown'}")
    
    # Test basic imports
    print("\n🔍 Testing required imports:")
    required_modules = [
        'gc', 'json', 'math', 'multiprocessing', 'os', 'platform',
        'random', 'statistics', 'subprocess', 'threading', 'time'
    ]
    
    for module in required_modules:
        try:
            __import__(module)
            print(f"  ✅ {module}")
        except ImportError as e:
            print(f"  ❌ {module}: {e}")
            return False
    
    # Test platform-specific capabilities
    print(f"\n🔍 Testing platform capabilities:")
    
    # Memory and CPU
    try:
        import multiprocessing
        cpu_count = multiprocessing.cpu_count()
        print(f"  ✅ CPU cores detected: {cpu_count}")
    except:
        print(f"  ⚠️ CPU core detection failed")
    
    # Unix/Linux specific tests
    if system in ['linux', 'darwin']:
        print(f"  📍 Unix-like system detected")
        
        # Test subprocess
        try:
            import subprocess
            result = subprocess.run(['echo', 'test'], capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                print(f"  ✅ Subprocess execution works")
            else:
                print(f"  ⚠️ Subprocess execution issue")
        except:
            print(f"  ❌ Subprocess execution failed")
        
        # Test real-time capabilities (if available)
        try:
            import os
            os.sched_get_priority_max(os.SCHED_FIFO)
            print(f"  ✅ Real-time scheduling available")
        except:
            print(f"  ⚠️ Real-time scheduling not available")
    
    elif system == 'windows':
        print(f"  📍 Windows system detected")
        print(f"  ℹ️ Limited RT features (expected)")
    
    print(f"\n🎯 Platform Compatibility Summary:")
    print(f"  • System: {system.title()}")
    print(f"  • Python: Compatible ({python_version.major}.{python_version.minor})")
    print(f"  • Required modules: Available")
    
    if system == 'linux':
        print(f"  • Expected features: Full RTOS testing with cyclictest")
    elif system == 'darwin':
        print(f"  • Expected features: Algorithm testing (limited RT)")
    elif system == 'windows':
        print(f"  • Expected features: Algorithm testing only")
    
    print(f"\n✅ COMPATIBILITY TEST PASSED!")
    print(f"📝 The RTOS benchmark should run on this system")
    return True

if __name__ == "__main__":
    success = test_platform_compatibility()
    sys.exit(0 if success else 1)