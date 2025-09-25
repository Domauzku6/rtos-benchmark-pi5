#!/usr/bin/env python3
"""
Multicore Management and CPU Affinity
=====================================

This module handles multicore system management, CPU affinity settings,
and parallel processing coordination for RTOS benchmarking.

Features:
---------
- CPU core detection and management
- CPU affinity setting and validation
- Multicore benchmark coordination
- Process isolation and prioritization

Author: RTOS Benchmark Suite Team
"""

import os
import multiprocessing
import threading
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from .platform_compat import platform_compat


class MulticoreManager:
    """Multicore system management and coordination"""
    
    def __init__(self):
        """Initialize multicore manager"""
        self.cpu_count = multiprocessing.cpu_count()
        self.available_cores = list(range(self.cpu_count))
        self.isolated_cores = []
        self.affinity_supported = platform_compat.supports_cpu_affinity()
    
    def get_system_topology(self):
        """Get system CPU topology information"""
        topology = {
            'total_cores': self.cpu_count,
            'available_cores': self.available_cores,
            'isolated_cores': self.isolated_cores,
            'affinity_supported': self.affinity_supported,
            'logical_processors': self.cpu_count
        }
        
        # Try to get more detailed topology on Linux
        if platform_compat.is_linux:
            try:
                # Check for hyperthreading/SMT
                with open('/proc/cpuinfo', 'r') as f:
                    cpuinfo = f.read()
                
                # Count physical cores vs logical processors
                physical_cores = set()
                for line in cpuinfo.split('\n'):
                    if line.startswith('core id'):
                        core_id = line.split(':')[1].strip()
                        physical_cores.add(core_id)
                
                if physical_cores:
                    topology['physical_cores'] = len(physical_cores)
                    topology['hyperthreading'] = len(physical_cores) < self.cpu_count
                
            except Exception:
                pass
        
        return topology
    
    def set_process_affinity(self, cpu_list=None):
        """Set CPU affinity for current process"""
        if not self.affinity_supported:
            return False, "CPU affinity not supported on this platform"
        
        if cpu_list is None:
            cpu_list = [0]  # Default to CPU 0
        
        try:
            if hasattr(os, 'sched_setaffinity'):
                # Linux
                os.sched_setaffinity(0, cpu_list)
                return True, f"Process affinity set to CPUs: {cpu_list}"
            else:
                return False, "sched_setaffinity not available"
        
        except Exception as e:
            return False, f"Failed to set CPU affinity: {e}"
    
    def get_process_affinity(self):
        """Get current process CPU affinity"""
        if not self.affinity_supported:
            return None
        
        try:
            if hasattr(os, 'sched_getaffinity'):
                return list(os.sched_getaffinity(0))
            else:
                return None
        except Exception:
            return None
    
    def isolate_cpu_for_rt(self, cpu_id=None):
        """Attempt to isolate a CPU core for real-time tasks"""
        if cpu_id is None:
            # Choose the highest numbered CPU (often less used)
            cpu_id = self.cpu_count - 1
        
        if cpu_id >= self.cpu_count or cpu_id < 0:
            return False, f"Invalid CPU ID: {cpu_id}"
        
        # Set affinity to the isolated CPU
        success, message = self.set_process_affinity([cpu_id])
        
        if success:
            self.isolated_cores = [cpu_id]
            return True, f"Isolated CPU {cpu_id} for RT tasks"
        else:
            return False, message
    
    def run_parallel_benchmark(self, test_function, test_args_list, max_workers=None):
        """Run benchmark tests in parallel across multiple cores"""
        if max_workers is None:
            max_workers = min(4, self.cpu_count)  # Reasonable default
        
        results = []
        
        try:
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = []
                
                for args in test_args_list:
                    future = executor.submit(test_function, *args)
                    futures.append(future)
                
                # Collect results
                for future in futures:
                    try:
                        result = future.result(timeout=60)  # 60 second timeout
                        results.append(result)
                    except Exception as e:
                        results.append({'error': str(e), 'success': False})
            
            return results
            
        except Exception as e:
            return [{'error': f'Parallel execution failed: {e}', 'success': False}]
    
    def run_multicore_stress_test(self, duration=10):
        """Run a multicore stress test to evaluate system behavior under load"""
        def cpu_stress_worker(core_id, duration):
            """Worker function for CPU stress testing"""
            try:
                # Try to set affinity to specific core
                if self.affinity_supported and hasattr(os, 'sched_setaffinity'):
                    try:
                        os.sched_setaffinity(0, [core_id])
                    except:
                        pass  # Ignore affinity errors in stress test
                
                # CPU-intensive calculation
                import time
                start_time = time.time()
                operations = 0
                
                while time.time() - start_time < duration:
                    # Simple arithmetic operations
                    for i in range(10000):
                        _ = i * i + i / 2
                        operations += 1
                
                end_time = time.time()
                actual_duration = end_time - start_time
                ops_per_second = operations / actual_duration
                
                return {
                    'core_id': core_id,
                    'operations': operations,
                    'duration': actual_duration,
                    'ops_per_second': ops_per_second,
                    'success': True
                }
                
            except Exception as e:
                return {
                    'core_id': core_id,
                    'error': str(e),
                    'success': False
                }
        
        # Run stress test on all available cores
        test_args = [(i, duration) for i in range(self.cpu_count)]
        results = self.run_parallel_benchmark(cpu_stress_worker, test_args)
        
        # Analyze results
        successful_results = [r for r in results if r.get('success')]
        
        if successful_results:
            total_ops = sum(r['operations'] for r in successful_results)
            avg_ops_per_core = total_ops / len(successful_results)
            
            analysis = {
                'total_cores_tested': len(successful_results),
                'total_operations': total_ops,
                'avg_ops_per_core': avg_ops_per_core,
                'individual_results': results,
                'test_duration': duration,
                'success': True
            }
        else:
            analysis = {
                'error': 'All stress tests failed',
                'individual_results': results,
                'success': False
            }
        
        return analysis
    
    def optimize_for_rt_workload(self):
        """Optimize system configuration for real-time workloads"""
        optimizations = []
        warnings = []
        
        # Check if we can isolate a CPU
        if self.cpu_count > 1:
            success, message = self.isolate_cpu_for_rt()
            if success:
                optimizations.append(message)
            else:
                warnings.append(f"CPU isolation failed: {message}")
        else:
            warnings.append("Single-core system - cannot isolate CPU for RT tasks")
        
        # Check for RT scheduling capabilities
        if platform_compat.supports_rt_scheduling():
            try:
                # Try to set RT priority (this might require privileges)
                if hasattr(os, 'sched_get_priority_max'):
                    max_priority = os.sched_get_priority_max(os.SCHED_FIFO)
                    optimizations.append(f"RT scheduling available (max priority: {max_priority})")
                else:
                    optimizations.append("RT scheduling support detected")
            except Exception as e:
                warnings.append(f"RT scheduling check failed: {e}")
        else:
            warnings.append("RT scheduling not supported on this platform")
        
        # Memory locking check
        if platform_compat.supports_memory_locking():
            optimizations.append("Memory locking supported for RT tasks")
        else:
            warnings.append("Memory locking not available")
        
        return {
            'optimizations_applied': optimizations,
            'warnings': warnings,
            'topology': self.get_system_topology()
        }
    
    def get_core_utilization_info(self):
        """Get information about current CPU core utilization"""
        utilization_info = {
            'timestamp': platform_compat.get_timestamp(),
            'total_cores': self.cpu_count,
            'current_affinity': self.get_process_affinity()
        }
        
        # Try to get load average on Unix systems
        if hasattr(os, 'getloadavg'):
            try:
                load_avg = os.getloadavg()
                utilization_info['load_average'] = {
                    '1_minute': load_avg[0],
                    '5_minute': load_avg[1],
                    '15_minute': load_avg[2]
                }
            except Exception:
                pass
        
        # Try to get CPU usage information
        try:
            import psutil
            cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
            utilization_info['per_core_usage'] = {
                f'core_{i}': usage for i, usage in enumerate(cpu_percent)
            }
            utilization_info['average_usage'] = sum(cpu_percent) / len(cpu_percent)
        except ImportError:
            utilization_info['note'] = 'psutil not available for detailed CPU usage'
        except Exception as e:
            utilization_info['error'] = f'CPU usage detection failed: {e}'
        
        return utilization_info