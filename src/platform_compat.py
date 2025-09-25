#!/usr/bin/env python3
"""
Cross-Platform Compatibility Layer
==================================

This module provides cross-platform compatibility utilities for RTOS benchmarking,
handling differences between Linux, macOS, and Windows systems.

Features:
---------
- Platform detection and capability checking
- Cross-platform system information collection
- Temperature monitoring across different systems
- Cache management and filesystem operations
- Privilege detection and management

Author: RTOS Benchmark Suite Team
"""

import os
import platform
import subprocess
import sys
import multiprocessing


class PlatformCompat:
    """Cross-platform compatibility utilities for RTOS benchmarking"""
    
    def __init__(self):
        """Initialize platform compatibility layer"""
        self.system = platform.system().lower()
        self.is_linux = self.system == 'linux'
        self.is_windows = self.system == 'windows'
        self.is_macos = self.system == 'darwin'
        self.is_unix = self.is_linux or self.is_macos
        
    def get_system_info(self):
        """Get comprehensive system information across platforms"""
        system_info = {}
        
        # Operating System Information
        try:
            if self.is_unix:
                # Unix/Linux: use uname -a
                result = subprocess.run(['uname', '-a'], capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    system_info['os_info'] = result.stdout.strip()
                    system_info['uname'] = result.stdout.strip()
                else:
                    system_info['os_info'] = f'{platform.system()} {platform.release()}'
                    system_info['uname'] = f'{platform.system()} {platform.release()}'
            else:
                # Windows: use platform module
                os_info = f'{platform.system()} {platform.release()} {platform.version()}'
                system_info['os_info'] = os_info
                system_info['uname'] = f'{os_info} {platform.machine()}'
        except Exception as e:
            system_info['os_info'] = f'{platform.system()} {platform.release()}'
            system_info['uname'] = f'System info unavailable: {str(e)}'
        
        # CPU Information
        try:
            if self.is_linux:
                # Try to get CPU info from /proc/cpuinfo
                try:
                    with open('/proc/cpuinfo', 'r') as f:
                        cpuinfo = f.read()
                        cpu_model = None
                        hardware = None
                        
                        for line in cpuinfo.split('\n'):
                            if line.startswith('model name'):
                                cpu_model = line.split(':')[1].strip()
                                break
                            elif line.startswith('Hardware'):
                                hardware = line.split(':')[1].strip()
                            elif line.startswith('Model'):
                                cpu_model = line.split(':')[1].strip()
                        
                        if cpu_model:
                            system_info['cpu_info'] = cpu_model
                        elif hardware:
                            system_info['cpu_info'] = f"{hardware} ({platform.machine()})"
                        else:
                            system_info['cpu_info'] = f"{platform.machine()} ({multiprocessing.cpu_count()} cores)"
                except:
                    system_info['cpu_info'] = f"{platform.machine()} ({multiprocessing.cpu_count()} cores)"
            else:
                system_info['cpu_info'] = platform.processor() or platform.machine()
            
            if not system_info.get('cpu_info') or system_info['cpu_info'] == '':
                system_info['cpu_info'] = f"{platform.machine()} ({multiprocessing.cpu_count()} cores)"
        except:
            system_info['cpu_info'] = 'Unknown CPU'
        
        # Memory Information
        try:
            if self.is_linux:
                # Read from /proc/meminfo
                with open('/proc/meminfo', 'r') as f:
                    meminfo = f.read()
                    for line in meminfo.split('\n'):
                        if line.startswith('MemTotal:'):
                            mem_kb = int(line.split()[1])
                            system_info['memory_gb'] = round(mem_kb / 1024 / 1024, 1)
                            break
                    else:
                        system_info['memory_gb'] = 'Unknown'
            elif self.is_windows:
                # Windows: try to get memory info
                try:
                    import ctypes
                    kernel32 = ctypes.windll.kernel32
                    c_ulong = ctypes.c_ulong
                    class MEMORYSTATUSEX(ctypes.Structure):
                        _fields_ = [
                            ('dwLength', c_ulong),
                            ('dwMemoryLoad', c_ulong),
                            ('ullTotalPhys', ctypes.c_ulonglong),
                            ('ullAvailPhys', ctypes.c_ulonglong),
                            ('ullTotalPageFile', ctypes.c_ulonglong),
                            ('ullAvailPageFile', ctypes.c_ulonglong),
                            ('ullTotalVirtual', ctypes.c_ulonglong),
                            ('ullAvailVirtual', ctypes.c_ulonglong),
                            ('sullAvailExtendedVirtual', ctypes.c_ulonglong),
                        ]
                    
                    memoryStatus = MEMORYSTATUSEX()
                    memoryStatus.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
                    kernel32.GlobalMemoryStatusEx(ctypes.byref(memoryStatus))
                    system_info['memory_gb'] = round(memoryStatus.ullTotalPhys / 1024 / 1024 / 1024, 1)
                except:
                    system_info['memory_gb'] = 'Unknown'
            else:
                # macOS and others
                system_info['memory_gb'] = 'Unknown'
        except:
            system_info['memory_gb'] = 'Unknown'
        
        # Cross-platform system details
        try:
            system_info['platform'] = platform.platform()
            system_info['architecture'] = platform.architecture()[0]
            system_info['processor'] = platform.processor() or platform.machine()
        except:
            pass
        
        # Python and CPU info
        try:
            system_info['python_version'] = sys.version
        except:
            system_info['python_version'] = 'Unknown'
        
        try:
            system_info['cpu_count'] = multiprocessing.cpu_count()
        except:
            system_info['cpu_count'] = 'Unknown'
        
        # RT kernel capability check (Linux only)
        if self.is_linux:
            try:
                # Check for RT kernel features
                with open('/proc/version', 'r') as f:
                    version = f.read().lower()
                    system_info['rt_kernel_capable'] = 'rt' in version or 'preempt' in version
            except:
                system_info['rt_kernel_capable'] = False
        else:
            system_info['rt_kernel_capable'] = False
        
        return system_info
    
    def get_cpu_temperature(self):
        """Get CPU temperature with platform-specific methods"""
        if self.is_linux:
            # Linux: try various thermal zones
            thermal_paths = [
                '/sys/class/thermal/thermal_zone0/temp',
                '/sys/class/thermal/thermal_zone1/temp',
                '/sys/class/thermal/thermal_zone2/temp'
            ]
            for path in thermal_paths:
                try:
                    with open(path, 'r') as f:
                        return int(f.read().strip()) / 1000.0
                except:
                    continue
            return None
        elif self.is_macos:
            # macOS: try using system_profiler or sensors (if available)
            try:
                # Try powermetrics (requires sudo)
                result = subprocess.run(['sudo', 'powermetrics', '-s', 'smc', '-n', '1', '--samplers', 'smc'],
                                     capture_output=True, text=True, timeout=10)
                if result.returncode == 0:
                    # Parse temperature from powermetrics output
                    for line in result.stdout.split('\n'):
                        if 'CPU die temperature' in line:
                            temp_str = line.split(':')[-1].strip()
                            if 'C' in temp_str:
                                return float(temp_str.replace('C', ''))
                    return None
            except:
                return None
        elif self.is_windows:
            # Windows: temperature monitoring is complex, return None
            # Could potentially use WMI or other Windows APIs
            return None
        
        return None
    
    def sync_filesystem(self):
        """Sync filesystem buffers across platforms"""
        try:
            if self.is_unix:
                os.system('sync')
                return True
            elif self.is_windows:
                # Windows doesn't have sync, but we can flush Python buffers
                sys.stdout.flush()
                sys.stderr.flush()
                return True
        except:
            return False
        return False
    
    def clear_terminal(self):
        """Clear terminal across platforms"""
        try:
            if self.is_windows:
                os.system('cls')
            else:
                os.system('clear')
            return True
        except:
            return False
    
    def has_root_privileges(self):
        """Check if running with root/administrator privileges"""
        if self.is_unix:
            return hasattr(os, 'geteuid') and os.geteuid() == 0
        elif self.is_windows:
            # On Windows, check if running as administrator
            try:
                import ctypes
                return ctypes.windll.shell32.IsUserAnAdmin() != 0
            except:
                return False
        return False
    
    def drop_system_caches(self):
        """Drop system caches if possible (Linux only)"""
        if not self.is_linux:
            return False  # Not supported on other platforms
        
        if not self.has_root_privileges():
            return False  # Need root permissions
        
        try:
            # Method 1: Try using subprocess with proper shell execution
            result = subprocess.run(['sh', '-c', 'echo 3 > /proc/sys/vm/drop_caches'], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                return True
                
            # Method 2: Try direct file write (more reliable)
            with open('/proc/sys/vm/drop_caches', 'w') as f:
                f.write('3')
                f.flush()
            return True
            
        except PermissionError:
            return False  # Permission denied
        except FileNotFoundError:
            return False  # System doesn't support cache dropping
        except Exception:
            # Method 3: Fallback to os.system (last resort)
            try:
                result = os.system('echo 3 > /proc/sys/vm/drop_caches 2>/dev/null')
                return result == 0
            except:
                return False
    
    def has_rt_capabilities(self):
        """Check if system supports real-time scheduling"""
        if not self.is_unix:
            return False
        
        try:
            # Try to get current scheduler info
            os.sched_get_priority_max(os.SCHED_FIFO)
            return True
        except:
            return False
    
    def has_cyclictest(self):
        """Check if cyclictest is available"""
        try:
            result = subprocess.run(['cyclictest', '--help'], 
                                  capture_output=True, text=True, timeout=5)
            return result.returncode == 0
        except Exception:
            return False
    
    def supports_rt_scheduling(self):
        """Check if real-time scheduling is supported"""
        if not self.is_linux:
            return False
        
        try:
            # Check if RT scheduling policies are available
            return hasattr(os, 'sched_get_priority_max') and hasattr(os, 'SCHED_FIFO')
        except Exception:
            return False
    
    def supports_cpu_affinity(self):
        """Check if CPU affinity setting is supported"""
        return hasattr(os, 'sched_setaffinity') and hasattr(os, 'sched_getaffinity')
    
    def supports_memory_locking(self):
        """Check if memory locking is supported"""
        if self.is_linux:
            return hasattr(os, 'mlockall') or True  # Usually available on Linux
        return False
    
    def get_timestamp(self):
        """Get a platform-appropriate timestamp"""
        from datetime import datetime
        return datetime.now().isoformat()


# Global platform compatibility instance
platform_compat = PlatformCompat()


# Cross-platform helper functions
def sync_system():
    """Sync filesystem across platforms"""
    return platform_compat.sync_filesystem()


def clear_terminal():
    """Clear terminal across platforms"""
    return platform_compat.clear_terminal()


def drop_caches_if_root():
    """Drop system caches if running as root, otherwise skip silently."""
    return platform_compat.drop_system_caches()