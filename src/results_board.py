#!/usr/bin/env python3
"""
Results Board Generation and Display
====================================

This module handles the generation and formatting of benchmark results
into comprehensive boards and reports.

Features:
---------
- ASCII leaderboard generation
- JSON results export/import
- Performance rating and analysis
- Cross-platform system information display

Author: RTOS Benchmark Suite Team
"""

import json
import os
from datetime import datetime
from .platform_compat import platform_compat


class ResultsBoard:
    """Results board generator and manager"""
    
    def __init__(self):
        """Initialize results board"""
        self.results_history = []
    
    def load_results_from_file(self, filename):
        """Load results from JSON file"""
        try:
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    return json.load(f)
        except Exception as e:
            print(f"⚠️  Error loading results from {filename}: {e}")
        return None
    
    def save_results_to_file(self, results, filename):
        """Save results to JSON file"""
        try:
            with open(filename, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"✅ Results saved to {filename}")
            return True
        except Exception as e:
            print(f"❌ Error saving results to {filename}: {e}")
            return False
    
    def generate_leaderboard(self, results_list, show_top=10):
        """Generate ASCII leaderboard from results list"""
        if not results_list:
            return "No results available for leaderboard."
        
        # Sort by composite score (lower is better for RT systems)
        sorted_results = sorted(results_list, 
                              key=lambda x: x.get('composite_score', float('inf')))
        
        leaderboard = []
        leaderboard.append("🏆 RTOS Performance Leaderboard 🏆")
        leaderboard.append("=" * 50)
        leaderboard.append("")
        
        for i, result in enumerate(sorted_results[:show_top], 1):
            system_info = result.get('system_info', {})
            os_info = system_info.get('os_info', 'Unknown OS')
            cpu_info = system_info.get('cpu_info', 'Unknown CPU')
            
            # Truncate long CPU names for display
            if len(cpu_info) > 40:
                cpu_info = cpu_info[:37] + "..."
            
            cyclictest = result.get('cyclictest_results', {})
            max_lat = cyclictest.get('max_latency_us', 'N/A')
            avg_lat = cyclictest.get('avg_latency_us', 'N/A')
            
            score = result.get('composite_score', 'N/A')
            timestamp = result.get('timestamp', 'Unknown')
            
            # Format timestamp
            try:
                dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                time_str = dt.strftime('%Y-%m-%d %H:%M')
            except:
                time_str = timestamp[:16] if len(timestamp) > 16 else timestamp
            
            leaderboard.append(f"#{i:2d} | Score: {score:6.2f} | Max: {max_lat:3}μs | Avg: {avg_lat:3}μs")
            leaderboard.append(f"     | {os_info}")
            leaderboard.append(f"     | {cpu_info}")
            leaderboard.append(f"     | {time_str}")
            leaderboard.append("-" * 50)
        
        return "\n".join(leaderboard)
    
    def format_system_info(self, system_info):
        """Format system information for display"""
        if not system_info:
            return "No system information available."
        
        info_lines = []
        info_lines.append("🖥️  System Information")
        info_lines.append("=" * 30)
        
        # OS Information
        os_info = system_info.get('os_info', 'Unknown')
        info_lines.append(f"Operating System: {os_info}")
        
        # CPU Information
        cpu_info = system_info.get('cpu_info', 'Unknown')
        info_lines.append(f"CPU: {cpu_info}")
        
        # Memory Information
        memory_gb = system_info.get('memory_gb', 'Unknown')
        if memory_gb != 'Unknown':
            info_lines.append(f"Memory: {memory_gb:.1f} GB")
        
        # Python Information
        python_version = system_info.get('python_version', 'Unknown')
        info_lines.append(f"Python: {python_version}")
        
        # Platform Information
        platform_info = system_info.get('platform', 'Unknown')
        info_lines.append(f"Platform: {platform_info}")
        
        # Kernel Information (if available)
        kernel_info = system_info.get('kernel_info')
        if kernel_info:
            info_lines.append(f"Kernel: {kernel_info}")
        
        # Architecture
        arch = system_info.get('architecture', 'Unknown')
        info_lines.append(f"Architecture: {arch}")
        
        return "\n".join(info_lines)
    
    def format_test_results(self, results):
        """Format complete test results for display"""
        if not results:
            return "No test results available."
        
        output_lines = []
        
        # Header
        output_lines.append("🎯 RTOS Benchmark Results")
        output_lines.append("=" * 50)
        output_lines.append("")
        
        # Timestamp
        timestamp = results.get('timestamp', 'Unknown')
        output_lines.append(f"Test Date: {timestamp}")
        output_lines.append("")
        
        # System Information
        system_info = results.get('system_info', {})
        output_lines.append(self.format_system_info(system_info))
        output_lines.append("")
        
        # Test Configuration
        config = results.get('test_config', {})
        if config:
            output_lines.append("⚙️  Test Configuration")
            output_lines.append("=" * 30)
            output_lines.append(f"Duration: {config.get('duration', 'Unknown')} seconds")
            output_lines.append(f"Priority: {config.get('priority', 'Unknown')}")
            output_lines.append(f"Algorithm Tests: {config.get('algorithm_tests', 'Unknown')}")
            output_lines.append("")
        
        # Cyclictest Results
        cyclictest = results.get('cyclictest_results', {})
        if cyclictest:
            output_lines.append("📊 Real-Time Latency Results")
            output_lines.append("=" * 30)
            
            if cyclictest.get('simulated'):
                output_lines.append("ℹ️  Note: Simulated results (cyclictest not available)")
            
            max_lat = cyclictest.get('max_latency_us', 'N/A')
            avg_lat = cyclictest.get('avg_latency_us', 'N/A')
            min_lat = cyclictest.get('min_latency_us', 'N/A')
            jitter = cyclictest.get('jitter_us', 'N/A')
            
            output_lines.append(f"Max Latency: {max_lat} μs")
            output_lines.append(f"Avg Latency: {avg_lat} μs")
            output_lines.append(f"Min Latency: {min_lat} μs")
            output_lines.append(f"Jitter: {jitter} μs")
            output_lines.append("")
        
        # Algorithm Results
        algorithms = results.get('algorithm_results', {})
        if algorithms:
            output_lines.append("🧮 Algorithm Performance")
            output_lines.append("=" * 30)
            
            for alg_name, alg_results in algorithms.items():
                if isinstance(alg_results, dict):
                    exec_time = alg_results.get('execution_time_ms', 'N/A')
                    iterations = alg_results.get('iterations', 'N/A')
                    output_lines.append(f"{alg_name}: {exec_time} ms ({iterations} iterations)")
            output_lines.append("")
        
        # Performance Scores
        composite_score = results.get('composite_score')
        if composite_score:
            output_lines.append("🏆 Performance Score")
            output_lines.append("=" * 30)
            output_lines.append(f"Composite Score: {composite_score:.2f}")
            output_lines.append("(Lower scores indicate better real-time performance)")
            output_lines.append("")
        
        # Environment Information
        env_info = results.get('environment_info', {})
        if env_info:
            output_lines.append("🔧 Environment")
            output_lines.append("=" * 30)
            
            temp = env_info.get('cpu_temperature_c')
            if temp:
                output_lines.append(f"CPU Temperature: {temp}°C")
            
            load_avg = env_info.get('load_average')
            if load_avg:
                output_lines.append(f"Load Average: {load_avg}")
            
            rt_capable = env_info.get('rt_kernel_capable', False)
            output_lines.append(f"RT Kernel: {'Yes' if rt_capable else 'No'}")
            output_lines.append("")
        
        return "\n".join(output_lines)
    
    def compare_results(self, result1, result2):
        """Compare two test results"""
        comparison = []
        comparison.append("🔍 Results Comparison")
        comparison.append("=" * 30)
        comparison.append("")
        
        # Compare latency
        c1_lat = result1.get('cyclictest_results', {}).get('max_latency_us', 0)
        c2_lat = result2.get('cyclictest_results', {}).get('max_latency_us', 0)
        
        if c1_lat and c2_lat:
            diff = c2_lat - c1_lat
            comparison.append(f"Max Latency: {c1_lat}μs vs {c2_lat}μs (Δ{diff:+}μs)")
        
        # Compare scores
        score1 = result1.get('composite_score', 0)
        score2 = result2.get('composite_score', 0)
        
        if score1 and score2:
            diff = score2 - score1
            comparison.append(f"Composite Score: {score1:.2f} vs {score2:.2f} (Δ{diff:+.2f})")
        
        # System comparison
        sys1 = result1.get('system_info', {}).get('os_info', 'Unknown')
        sys2 = result2.get('system_info', {}).get('os_info', 'Unknown')
        
        comparison.append("")
        comparison.append(f"System 1: {sys1}")
        comparison.append(f"System 2: {sys2}")
        
        return "\n".join(comparison)
    
    def get_performance_summary(self, results):
        """Get a quick performance summary"""
        if not results:
            return "No results to summarize."
        
        cyclictest = results.get('cyclictest_results', {})
        max_lat = cyclictest.get('max_latency_us')
        avg_lat = cyclictest.get('avg_latency_us')
        
        # Determine performance level
        if max_lat and avg_lat:
            if max_lat <= 20 and avg_lat <= 10:
                performance = "🟢 Excellent RT Performance"
            elif max_lat <= 50 and avg_lat <= 25:
                performance = "🟡 Good RT Performance"
            elif max_lat <= 100 and avg_lat <= 50:
                performance = "🟠 Fair RT Performance"
            else:
                performance = "🔴 Poor RT Performance"
        else:
            performance = "❓ Unknown Performance"
        
        system = results.get('system_info', {}).get('os_info', 'Unknown System')
        score = results.get('composite_score', 'N/A')
        
        return f"{performance} | Score: {score} | {system}"