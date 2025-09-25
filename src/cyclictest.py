#!/usr/bin/env python3
"""
Cyclictest Integration and Simulation
=====================================

This module handles cyclictest execution, output parsing,
and provides simulation for systems where cyclictest is unavailable.

Features:
---------
- Cyclictest command execution with multiple fallbacks
- Output parsing and latency analysis
- Simulation mode for non-Linux systems
- Statistical analysis of latency data

Author: RTOS Benchmark Suite Team
"""

import random
import statistics
import subprocess
from .platform_compat import platform_compat


class CyclicTestIntegration:
    """Lightweight cyclictest integration with proper output parsing"""
    
    def __init__(self):
        """Initialize cyclictest integration"""
        self.simulation_mode = not platform_compat.has_cyclictest()
    
    @staticmethod
    def parse_cyclictest_output(output):
        """Parse cyclictest output to extract latency statistics"""
        try:
            latency_data = {
                'min_latency_us': None,
                'avg_latency_us': None,
                'max_latency_us': None,
                'jitter_us': None,
                'duration': 0,
                'success': True
            }
            
            # Look for summary line like: "T: 0 (12345) P:99 I:100 C: 10000 Min:    5 Act:   12 Avg:   15 Max:   85"
            lines = output.split('\n')
            
            for line in lines:
                line = line.strip()
                
                # Parse the main data line
                if line.startswith('T:') and 'Min:' in line and 'Max:' in line:
                    try:
                        # Extract numeric values using string parsing
                        parts = line.split()
                        
                        for i, part in enumerate(parts):
                            if part == 'Min:' and i + 1 < len(parts):
                                latency_data['min_latency_us'] = int(parts[i + 1])
                            elif part == 'Avg:' and i + 1 < len(parts):
                                latency_data['avg_latency_us'] = int(parts[i + 1])
                            elif part == 'Max:' and i + 1 < len(parts):
                                latency_data['max_latency_us'] = int(parts[i + 1])
                        
                        # Calculate jitter (max - min)
                        if latency_data['max_latency_us'] and latency_data['min_latency_us']:
                            latency_data['jitter_us'] = latency_data['max_latency_us'] - latency_data['min_latency_us']
                        
                        break
                    except (ValueError, IndexError) as e:
                        continue
            
            # Validate that we got meaningful data
            if latency_data['max_latency_us'] is None:
                raise ValueError("Could not parse latency values from output")
            
            return latency_data
            
        except Exception as e:
            return {
                'min_latency_us': None,
                'avg_latency_us': None,
                'max_latency_us': None,
                'jitter_us': None,
                'duration': 0,
                'success': False,
                'error': f'Failed to parse cyclictest output: {e}',
                'raw_output': output[:500] if output else 'No output'
            }
    
    @staticmethod
    def simulate_cyclictest_fallback():
        """Simulate cyclictest results when not available or no privileges"""
        # Generate realistic latency values based on typical system performance
        base_latency = random.randint(8, 25)  # Base latency in microseconds
        jitter_factor = random.uniform(1.5, 4.0)  # Jitter multiplier
        
        min_latency = max(1, base_latency - random.randint(2, 5))
        avg_latency = base_latency + random.randint(1, 8)
        max_latency = base_latency + int(base_latency * jitter_factor)
        
        return {
            'min_latency_us': min_latency,
            'avg_latency_us': avg_latency,
            'max_latency_us': max_latency,
            'jitter_us': max_latency - min_latency,
            'duration': 15,  # Simulated duration
            'success': True,
            'simulated': True,
            'note': 'Simulated cyclictest results - cyclictest not available'
        }
    
    @staticmethod
    def run_cyclictest(duration=15, priority=99):
        """Run cyclictest command with fallback simulation"""
        
        # Check if cyclictest is available and if we're on a supported platform
        if not platform_compat.is_linux:
            print(f"ℹ️  cyclictest not available on {platform_compat.system.title()} - using simulation...")
            return CyclicTestIntegration.simulate_cyclictest_fallback()
        
        if not platform_compat.has_cyclictest():
            print("ℹ️  cyclictest not installed - using simulation...")
            return CyclicTestIntegration.simulate_cyclictest_fallback()
        
        try:
            # Try different command variations for better compatibility
            cmd_variations = [
                # Standard high-priority command
                ['cyclictest', '-t', '1', '-p', str(priority), '-i', '100', '-q', '-l', str(duration * 1000)],
                # Lower priority without RT scheduling
                ['cyclictest', '-t', '1', '-p', '50', '-i', '100', '-q', '-l', str(duration * 1000)],
                # Minimal command
                ['cyclictest', '-t', '1', '-i', '100', '-q', '-l', str(duration * 500)]
            ]
            
            for cmd in cmd_variations:
                try:
                    result = subprocess.run(cmd, capture_output=True, text=True, timeout=duration + 10)
                    
                    if result.returncode == 0 and result.stdout.strip():
                        parsed_results = CyclicTestIntegration.parse_cyclictest_output(result.stdout)
                        parsed_results['duration'] = duration
                        return parsed_results
                    
                except subprocess.TimeoutExpired:
                    continue
                except subprocess.CalledProcessError:
                    continue
                except Exception:
                    continue
            
            # If all commands failed, fall back to simulation
            print("⚠️  cyclictest execution failed, using simulation...")
            return CyclicTestIntegration.simulate_cyclictest_fallback()
            
        except Exception:
            print("⚠️  cyclictest not available or no RT privileges, using simulation...")
            return CyclicTestIntegration.simulate_cyclictest_fallback()
    
    def analyze_latency_distribution(self, results_list):
        """Analyze latency distribution across multiple test runs"""
        if not results_list:
            return {}
        
        # Extract latency values
        max_latencies = [r.get('max_latency_us', 0) for r in results_list if r.get('success')]
        avg_latencies = [r.get('avg_latency_us', 0) for r in results_list if r.get('success')]
        jitter_values = [r.get('jitter_us', 0) for r in results_list if r.get('success')]
        
        if not max_latencies:
            return {'error': 'No valid latency data available'}
        
        analysis = {
            'max_latency_stats': {
                'mean': statistics.mean(max_latencies),
                'median': statistics.median(max_latencies),
                'stdev': statistics.stdev(max_latencies) if len(max_latencies) > 1 else 0,
                'min': min(max_latencies),
                'max': max(max_latencies)
            },
            'avg_latency_stats': {
                'mean': statistics.mean(avg_latencies),
                'median': statistics.median(avg_latencies),
                'stdev': statistics.stdev(avg_latencies) if len(avg_latencies) > 1 else 0,
                'min': min(avg_latencies),
                'max': max(avg_latencies)
            },
            'jitter_stats': {
                'mean': statistics.mean(jitter_values),
                'median': statistics.median(jitter_values),
                'stdev': statistics.stdev(jitter_values) if len(jitter_values) > 1 else 0,
                'min': min(jitter_values),
                'max': max(jitter_values)
            },
            'test_count': len(results_list),
            'success_rate': len(max_latencies) / len(results_list) * 100
        }
        
        return analysis
    
    def get_rt_performance_rating(self, max_latency_us, avg_latency_us):
        """Get performance rating based on latency values"""
        if max_latency_us is None or avg_latency_us is None:
            return "Unknown", 0
        
        # RT performance thresholds (microseconds)
        if max_latency_us <= 20 and avg_latency_us <= 10:
            return "Excellent", 95
        elif max_latency_us <= 50 and avg_latency_us <= 25:
            return "Good", 80
        elif max_latency_us <= 100 and avg_latency_us <= 50:
            return "Fair", 65
        elif max_latency_us <= 200 and avg_latency_us <= 100:
            return "Poor", 40
        else:
            return "Unacceptable", 20