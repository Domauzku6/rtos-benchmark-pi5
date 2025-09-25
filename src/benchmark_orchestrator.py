#!/usr/bin/env python3
"""
Main Benchmark Orchestrator
===========================

This module coordinates and runs the complete RTOS benchmark suite,
integrating all components and managing the overall test flow.

Features:
---------
- Complete benchmark orchestration
- Test configuration management
- Results aggregation and scoring
- Progress tracking and reporting

Author: RTOS Benchmark Suite Team
"""

import json
import time
from datetime import datetime
from .platform_compat import platform_compat
from .algorithms import RTOSSortingAlgorithms, AlgorithmBenchmark
from .rtos_env import RTOSEnvironment
from .cyclictest import CyclicTestIntegration
from .results_board import ResultsBoard
from .multicore import MulticoreManager


class RTOSBenchmarkOrchestrator:
    """Main benchmark orchestration and coordination"""
    
    def __init__(self):
        """Initialize benchmark orchestrator"""
        self.platform = platform_compat
        self.algorithm_bench = AlgorithmBenchmark()
        self.rtos_env = RTOSEnvironment()
        self.cyclictest = CyclicTestIntegration()
        self.results_board = ResultsBoard()
        self.multicore = MulticoreManager()
        
        # Default test configuration
        self.default_config = {
            'duration': 15,
            'priority': 99,
            'algorithm_tests': True,
            'multicore_tests': True,
            'environment_monitoring': True,
            'save_results': True,
            'show_progress': True
        }
    
    def validate_system_requirements(self):
        """Validate system requirements for benchmarking"""
        validation_results = {
            'system_ready': True,
            'warnings': [],
            'recommendations': [],
            'system_info': {}
        }
        
        # Basic system information
        system_info = self.platform.get_system_info()
        validation_results['system_info'] = system_info
        
        # Check Python version
        python_version = system_info.get('python_version', '')
        if '3.' not in python_version:
            validation_results['warnings'].append("Python 3.x recommended for optimal performance")
        
        # Check for RT capabilities
        if not self.platform.supports_rt_scheduling():
            validation_results['warnings'].append("Real-time scheduling not available - some features limited")
            validation_results['recommendations'].append("Run on Linux with RT kernel for full RT capabilities")
        
        # Check for cyclictest
        if not self.cyclictest.simulation_mode:
            validation_results['recommendations'].append("cyclictest available - will use real measurements")
        else:
            validation_results['warnings'].append("cyclictest not available - will use simulation")
        
        # Check memory
        memory_gb = system_info.get('memory_gb', 0)
        if memory_gb < 1:
            validation_results['warnings'].append("Low memory detected - may affect performance")
        
        # Check multicore capabilities
        cpu_count = self.multicore.cpu_count
        if cpu_count == 1:
            validation_results['warnings'].append("Single-core system - multicore tests will be limited")
        else:
            validation_results['recommendations'].append(f"{cpu_count} cores detected - multicore tests enabled")
        
        return validation_results
    
    def run_comprehensive_benchmark(self, config=None):
        """Run the complete RTOS benchmark suite"""
        if config is None:
            config = self.default_config.copy()
        
        print("🚀 Starting RTOS Benchmark Suite...")
        print("=" * 50)
        
        # Validate system
        validation = self.validate_system_requirements()
        if validation['warnings']:
            print("\n⚠️  System Warnings:")
            for warning in validation['warnings']:
                print(f"   • {warning}")
        
        if validation['recommendations']:
            print("\nℹ️  Recommendations:")
            for rec in validation['recommendations']:
                print(f"   • {rec}")
        
        print("\n🔧 Preparing test environment...")
        
        # Initialize test results structure
        results = {
            'timestamp': datetime.now().isoformat(),
            'test_config': config,
            'system_info': validation['system_info'],
            'validation': validation
        }
        
        # Setup RTOS environment
        env_setup = self.rtos_env.setup_rt_environment(
            lock_memory=config.get('lock_memory', True),
            set_priority=config.get('set_priority', True),
            target_priority=config.get('priority', 99)
        )
        results['environment_setup'] = env_setup
        
        if config.get('show_progress', True):
            print(f"✅ Environment setup completed")
            if env_setup.get('warnings'):
                for warning in env_setup['warnings']:
                    print(f"   ⚠️  {warning}")
        
        # Optimize for multicore if available
        if config.get('multicore_tests', True) and self.multicore.cpu_count > 1:
            multicore_opt = self.multicore.optimize_for_rt_workload()
            results['multicore_optimization'] = multicore_opt
            if config.get('show_progress', True):
                print(f"✅ Multicore optimization applied")
        
        # Run cyclictest benchmark
        print("\n📊 Running real-time latency tests...")
        cyclictest_results = self.cyclictest.run_cyclictest(
            duration=config.get('duration', 15),
            priority=config.get('priority', 99)
        )
        results['cyclictest_results'] = cyclictest_results
        
        if config.get('show_progress', True):
            if cyclictest_results.get('success'):
                max_lat = cyclictest_results.get('max_latency_us', 'N/A')
                avg_lat = cyclictest_results.get('avg_latency_us', 'N/A')
                print(f"✅ Latency test completed - Max: {max_lat}μs, Avg: {avg_lat}μs")
            else:
                print(f"⚠️  Latency test had issues: {cyclictest_results.get('error', 'Unknown error')}")
        
        # Run algorithm benchmarks
        if config.get('algorithm_tests', True):
            print("\n🧮 Running algorithm benchmarks...")
            algorithm_results = {}
            
            algorithms_to_test = ['quick_sort', 'merge_sort', 'matrix_multiplication', 'fft_simulation']
            
            for algorithm in algorithms_to_test:
                if config.get('show_progress', True):
                    print(f"   Running {algorithm}...")
                
                alg_result = self.algorithm_bench.run_algorithm_test(algorithm)
                algorithm_results[algorithm] = alg_result
                
                if config.get('show_progress', True) and alg_result.get('success'):
                    exec_time = alg_result.get('execution_time_ms', 'N/A')
                    print(f"   ✅ {algorithm}: {exec_time} ms")
            
            results['algorithm_results'] = algorithm_results
        
        # Run multicore stress test
        if config.get('multicore_tests', True) and self.multicore.cpu_count > 1:
            print("\n⚡ Running multicore stress test...")
            stress_results = self.multicore.run_multicore_stress_test(duration=5)
            results['multicore_stress'] = stress_results
            
            if config.get('show_progress', True):
                if stress_results.get('success'):
                    cores_tested = stress_results.get('total_cores_tested', 0)
                    total_ops = stress_results.get('total_operations', 0)
                    print(f"✅ Stress test completed - {cores_tested} cores, {total_ops:,} operations")
        
        # Collect environment information
        if config.get('environment_monitoring', True):
            print("\n🌡️  Collecting environment data...")
            env_info = self.rtos_env.get_system_info()
            results['environment_info'] = env_info
            
            if config.get('show_progress', True):
                temp = env_info.get('cpu_temperature_c')
                if temp:
                    print(f"✅ Environment data collected - CPU temp: {temp}°C")
                else:
                    print(f"✅ Environment data collected")
        
        # Calculate composite performance score
        composite_score = self.calculate_composite_score(results)
        results['composite_score'] = composite_score
        
        # Cleanup environment
        cleanup_result = self.rtos_env.cleanup_rt_environment()
        results['cleanup'] = cleanup_result
        
        # Save results to file
        if config.get('save_results', True):
            timestamp_str = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"rtos_full_board_results_{timestamp_str}.json"
            self.results_board.save_results_to_file(results, filename)
        
        print("\n🎯 Benchmark completed!")
        print("=" * 50)
        
        return results
    
    def calculate_composite_score(self, results):
        """Calculate a composite performance score"""
        try:
            score_components = {}
            total_score = 0
            weight_sum = 0
            
            # Real-time latency score (40% weight)
            cyclictest = results.get('cyclictest_results', {})
            if cyclictest.get('success') and cyclictest.get('max_latency_us'):
                max_latency = cyclictest['max_latency_us']
                avg_latency = cyclictest.get('avg_latency_us', max_latency)
                
                # Lower latency = better score (invert and normalize)
                latency_score = 100 / (1 + max_latency / 10 + avg_latency / 20)
                score_components['latency'] = latency_score
                total_score += latency_score * 0.4
                weight_sum += 0.4
            
            # Algorithm performance score (30% weight)
            algorithms = results.get('algorithm_results', {})
            if algorithms:
                alg_scores = []
                for alg_name, alg_result in algorithms.items():
                    if alg_result.get('success') and alg_result.get('execution_time_ms'):
                        # Normalize based on expected performance
                        exec_time = alg_result['execution_time_ms']
                        # Lower execution time = better score
                        alg_score = 100 / (1 + exec_time / 50)
                        alg_scores.append(alg_score)
                
                if alg_scores:
                    avg_alg_score = sum(alg_scores) / len(alg_scores)
                    score_components['algorithms'] = avg_alg_score
                    total_score += avg_alg_score * 0.3
                    weight_sum += 0.3
            
            # System capability score (20% weight)
            system_score = 50  # Base score
            
            # Bonus for RT capabilities
            if results.get('system_info', {}).get('rt_kernel_capable'):
                system_score += 20
            
            # Bonus for multicore
            cpu_count = results.get('system_info', {}).get('cpu_count', 1)
            system_score += min(20, cpu_count * 2)
            
            # Memory bonus
            memory_gb = results.get('system_info', {}).get('memory_gb', 0)
            system_score += min(10, memory_gb)
            
            score_components['system'] = system_score
            total_score += system_score * 0.2
            weight_sum += 0.2
            
            # Environment score (10% weight)
            env_score = 50  # Base score
            
            # Temperature penalty (if available)
            temp = results.get('environment_info', {}).get('cpu_temperature_c')
            if temp:
                if temp > 80:
                    env_score -= 20
                elif temp > 70:
                    env_score -= 10
                elif temp < 50:
                    env_score += 10
            
            score_components['environment'] = env_score
            total_score += env_score * 0.1
            weight_sum += 0.1
            
            # Normalize final score
            if weight_sum > 0:
                final_score = total_score / weight_sum
            else:
                final_score = 50  # Default score
            
            return {
                'composite_score': round(final_score, 2),
                'components': score_components,
                'methodology': 'Weighted average: Latency(40%) + Algorithms(30%) + System(20%) + Environment(10%)'
            }
            
        except Exception as e:
            return {
                'composite_score': 0,
                'error': f'Score calculation failed: {e}',
                'components': {}
            }
    
    def run_quick_benchmark(self):
        """Run a quick benchmark with minimal configuration"""
        quick_config = {
            'duration': 5,
            'priority': 50,
            'algorithm_tests': True,
            'multicore_tests': False,
            'environment_monitoring': True,
            'save_results': False,
            'show_progress': True
        }
        
        return self.run_comprehensive_benchmark(quick_config)
    
    def compare_with_previous_results(self, current_results, previous_results_file):
        """Compare current results with previous benchmark results"""
        previous_results = self.results_board.load_results_from_file(previous_results_file)
        
        if not previous_results:
            return "No previous results found for comparison."
        
        comparison = self.results_board.compare_results(previous_results, current_results)
        return comparison
    
    def generate_comprehensive_report(self, results):
        """Generate a comprehensive benchmark report"""
        if not results:
            return "No results available for report generation."
        
        report_sections = []
        
        # Header
        report_sections.append("📋 RTOS Benchmark Comprehensive Report")
        report_sections.append("=" * 60)
        report_sections.append("")
        
        # Executive Summary
        summary = self.results_board.get_performance_summary(results)
        report_sections.append("🎯 Executive Summary")
        report_sections.append("-" * 30)
        report_sections.append(summary)
        report_sections.append("")
        
        # Detailed Results
        detailed_results = self.results_board.format_test_results(results)
        report_sections.append(detailed_results)
        
        # System Validation
        validation = results.get('validation', {})
        if validation.get('warnings') or validation.get('recommendations'):
            report_sections.append("")
            report_sections.append("🔍 System Analysis")
            report_sections.append("-" * 30)
            
            if validation.get('warnings'):
                report_sections.append("Warnings:")
                for warning in validation['warnings']:
                    report_sections.append(f"  ⚠️  {warning}")
            
            if validation.get('recommendations'):
                report_sections.append("Recommendations:")
                for rec in validation['recommendations']:
                    report_sections.append(f"  💡 {rec}")
        
        return "\n".join(report_sections)