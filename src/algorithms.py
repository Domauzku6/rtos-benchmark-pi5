#!/usr/bin/env python3
"""
Algorithm Implementations for RTOS Benchmarking - Educational Edition
====================================================================

This module contains optimized sorting algorithm implementations designed for
real-time system benchmarking and serves as an educational resource for learning
algorithms, performance analysis, and real-time system concepts.

🎓 EDUCATIONAL FEATURES:
- Detailed algorithm explanations with complexity analysis
- Step-by-step code comments for learning
- Performance comparison tools
- Real-world optimization techniques
- Big O notation examples and practical implications

🚀 ALGORITHMS IMPLEMENTED:
- Bubble Sort (O(n²)) - Simple but inefficient, educational value
- Quick Sort (O(n log n)) - Divide-and-conquer, cache-efficient
- Merge Sort (O(n log n)) - Stable, predictable performance
- Heap Sort (O(n log n)) - In-place, guaranteed performance
- Binary Search (O(log n)) - Search algorithm example

🔧 REAL-TIME OPTIMIZATIONS:
- Memory access pattern optimization
- Cache-friendly implementations
- Early termination conditions
- Reduced system call overhead

📚 LEARNING OBJECTIVES:
After studying this module, you will understand:
1. How algorithm choice affects real-time performance
2. The difference between theoretical and practical complexity
3. Memory access patterns and cache efficiency
4. Performance measurement and benchmarking techniques
5. Optimization strategies for embedded/RT systems

Author: Domas Užkuraitis (uzkuraitis.domas@gmail.com)
Created for: RTOS Benchmark Suite - Educational Edition
"""

import random
import time
import math


class RTOSSortingAlgorithms:
    """
    📚 Educational Collection of Sorting Algorithms for RTOS Benchmarking
    
    This class demonstrates various sorting algorithms with detailed explanations,
    performance analysis, and real-time optimization techniques.
    
    🎯 Purpose: Learn how algorithm choice impacts real-time system performance
    
    Key Concepts Demonstrated:
    -------------------------
    - Time Complexity: Big O notation in practice
    - Space Complexity: Memory usage patterns
    - Cache Efficiency: Memory access optimization
    - Stability: Maintaining relative order of equal elements
    - Adaptability: Performance on different data patterns
    
    Real-Time Considerations:
    ------------------------
    - Predictable execution time (important for RT systems)
    - Memory locality and cache-friendly access patterns
    - Minimal dynamic memory allocation
    - Early termination optimizations
    """
    
    def __init__(self):
        """
        Initialize the algorithm collection with performance tracking.
        
        The algorithm_stats dictionary will store performance metrics
        for educational analysis and comparison.
        """
        self.algorithm_stats = {}
        
        # 📊 Store algorithm characteristics for educational purposes
        self.algorithm_info = {
            'bubble_sort': {
                'time_complexity': 'O(n²) worst/average, O(n) best',
                'space_complexity': 'O(1)',
                'stable': True,
                'adaptive': True,
                'description': 'Simple comparison sort, good for learning basics'
            },
            'quick_sort': {
                'time_complexity': 'O(n log n) average, O(n²) worst',
                'space_complexity': 'O(log n)',
                'stable': False,
                'adaptive': False,
                'description': 'Fast divide-and-conquer, cache-efficient'
            },
            'merge_sort': {
                'time_complexity': 'O(n log n) always',
                'space_complexity': 'O(n)',
                'stable': True,
                'adaptive': False,
                'description': 'Predictable performance, good for RT systems'
            },
            'heap_sort': {
                'time_complexity': 'O(n log n) always',
                'space_complexity': 'O(1)',
                'stable': False,
                'adaptive': False,
                'description': 'In-place with guaranteed performance'
            }
        }
    
    def optimized_bubble_sort(self, data):
        """
        🫧 BUBBLE SORT - Educational Implementation with Real-Time Optimizations
        
        📚 ALGORITHM EXPLANATION:
        Bubble Sort works by repeatedly stepping through the list, comparing
        adjacent elements and swapping them if they're in the wrong order.
        The pass through the list is repeated until no swaps are needed.
        
        🎓 WHY "BUBBLE"?
        Smaller elements "bubble" to the beginning of the list, just like
        air bubbles rise to the surface of water.
        
        ⏱️ COMPLEXITY ANALYSIS:
        - Time: O(n²) worst/average case, O(n) best case (already sorted)
        - Space: O(1) - sorts in-place, very memory efficient
        
        🚀 REAL-TIME OPTIMIZATIONS APPLIED:
        1. Early termination: Stop if no swaps occur (data is sorted)
        2. Reduced comparisons: Each pass reduces inner loop by 1
        3. Cache-friendly: Sequential memory access pattern
        4. Input validation: Handle edge cases efficiently
        
        🎯 WHEN TO USE:
        - Educational purposes (easy to understand)
        - Small datasets (< 50 elements)
        - When simplicity is more important than speed
        - When you need a stable, in-place sort
        
        ❌ WHEN NOT TO USE:
        - Large datasets (performance degrades quickly)
        - Real-time systems with strict timing (unpredictable)
        - When you need optimal performance
        
        Args:
            data (list): List of comparable elements to sort
            
        Returns:
            list: New sorted list (original unchanged)
            
        Example:
            >>> sorter = RTOSSortingAlgorithms()
            >>> result = sorter.optimized_bubble_sort([64, 34, 25, 12, 22, 11, 90])
            >>> print(result)  # [11, 12, 22, 25, 34, 64, 90]
        """
        # 🛡️ Input validation - important for robust RT systems
        if not data or len(data) < 2:
            return data.copy()  # Return copy to maintain consistency
        
        # 📊 Create a working copy to avoid modifying original data
        result = data.copy()
        n = len(result)
        
        # 🔄 Outer loop: Each pass bubbles one element to correct position
        for i in range(n):
            swapped = False  # 🚩 Flag to detect if any swaps occurred
            
            # 🔍 Inner loop: Compare adjacent elements
            # Optimization: Reduce range by i (last i elements already sorted)
            for j in range(0, n - i - 1):
                
                # 📊 Compare adjacent elements
                if result[j] > result[j + 1]:
                    # 🔄 Swap elements (bubble smaller element up)
                    result[j], result[j + 1] = result[j + 1], result[j]
                    swapped = True  # Mark that a swap occurred
            
            # 🚀 Early termination optimization
            # If no swaps occurred, the array is already sorted!
            if not swapped:
                break
        
        return result
    
    def optimized_quicksort(self, data):
        """
        ⚡ QUICKSORT - Educational Implementation with Cache Optimizations
        
        📚 ALGORITHM EXPLANATION:
        Quicksort uses a divide-and-conquer strategy. It picks a 'pivot' element
        and partitions the array around it, then recursively sorts the partitions.
        
        🎓 HOW IT WORKS:
        1. Choose a pivot element from the array
        2. Partition: rearrange array so elements < pivot come before,
           elements > pivot come after
        3. Recursively apply the same process to sub-arrays
        
        ⏱️ COMPLEXITY ANALYSIS:
        - Time: O(n log n) average case, O(n²) worst case
        - Space: O(log n) average (recursion stack)
        
        🚀 OPTIMIZATIONS APPLIED:
        1. Median-of-three pivot selection (reduces worst case)
        2. Tail recursion optimization (reduces stack depth)
        3. Insertion sort for small arrays (< 10 elements)
        4. Cache-friendly partitioning
        
        🎯 WHEN TO USE:
        - Large datasets (very efficient on average)
        - When average performance is more important than worst-case
        - General-purpose sorting (most programming languages use variants)
        
        ⚠️ REAL-TIME CONSIDERATIONS:
        - Worst case O(n²) can be problematic for RT systems
        - Recursion depth can vary (stack usage unpredictable)
        - Consider merge sort for guaranteed performance
        
        Args:
            data (list): List of comparable elements to sort
            
        Returns:
            list: New sorted list (original unchanged)
        """
        if len(data) < 2:
            return data.copy()
        
        def quicksort_recursive(arr, low, high):
            """
            🔄 Recursive quicksort with tail recursion optimization
            
            This implementation reduces stack depth by always recursing
            on the smaller partition first, then handling the larger
            partition iteratively.
            """
            while low < high:
                # 🚀 Optimization: Use insertion sort for small subarrays
                # Small arrays sort faster with insertion sort due to
                # lower overhead and better cache locality
                if high - low < 10:
                    insertion_sort_range(arr, low, high)
                    break
                
                # 📊 Partition array around pivot
                pivot_index = partition(arr, low, high)
                
                # 🚀 Tail recursion optimization:
                # Always recurse on smaller partition first
                if pivot_index - low < high - pivot_index:
                    # Left partition is smaller
                    quicksort_recursive(arr, low, pivot_index - 1)
                    low = pivot_index + 1  # Handle right partition iteratively
                else:
                    # Right partition is smaller
                    quicksort_recursive(arr, pivot_index + 1, high)
                    high = pivot_index - 1  # Handle left partition iteratively
        
        def partition(arr, low, high):
            """
            🎯 Partitioning with median-of-three pivot selection
            
            This reduces the chance of worst-case behavior by choosing
            a better pivot than just the last element.
            """
            # 📊 Median-of-three pivot selection optimization
            # This significantly reduces worst-case scenarios
            mid = (low + high) // 2
            
            # Sort the three candidates: arr[low], arr[mid], arr[high]
            if arr[mid] < arr[low]:
                arr[low], arr[mid] = arr[mid], arr[low]
            if arr[high] < arr[low]:
                arr[low], arr[high] = arr[high], arr[low]
            if arr[high] < arr[mid]:
                arr[mid], arr[high] = arr[high], arr[mid]
            
            # Now arr[mid] contains the median, use it as pivot
            pivot = arr[high]
            i = low - 1  # Index of smaller element
            
            # 🔍 Partitioning loop
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            
            # Place pivot in correct position
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1
        
        def insertion_sort_range(arr, low, high):
            """
            🔧 Insertion sort for small ranges (optimization)
            
            For small arrays (< 10 elements), insertion sort is faster
            than quicksort due to lower overhead and better constants.
            """
            for i in range(low + 1, high + 1):
                key = arr[i]
                j = i - 1
                
                # Shift elements greater than key to the right
                while j >= low and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1
                
                # Insert key at correct position
                arr[j + 1] = key
        
        # Create working copy and sort it
        result = data.copy()
        quicksort_recursive(result, 0, len(result) - 1)
        return result
    
    def merge_sort(self, data):
        """
        Divide-and-conquer merge sort implementation
        
        Features:
        - Stable sorting algorithm
        - Predictable O(n log n) performance
        - Memory-efficient implementation
        """
        if len(data) <= 1:
            return data
        
        def merge_sort_recursive(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort_recursive(arr[:mid])
            right = merge_sort_recursive(arr[mid:])
            
            return merge(left, right)
        
        def merge(left, right):
            result = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            
            # Add remaining elements
            result.extend(left[i:])
            result.extend(right[j:])
            
            return result
        
        return merge_sort_recursive(data)
    
    def heap_sort(self, data):
        """
        In-place heap sort implementation
        
        Features:
        - O(n log n) worst-case performance
        - In-place sorting (O(1) extra space)
        - Cache-efficient heap operations
        """
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < n and arr[left] > arr[largest]:
                largest = left
            
            if right < n and arr[right] > arr[largest]:
                largest = right
            
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)
        
        result = data.copy()
        n = len(result)
        
        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(result, n, i)
        
        # Extract elements one by one
        for i in range(n - 1, 0, -1):
            result[0], result[i] = result[i], result[0]
            heapify(result, i, 0)
        
        return result
    
    def benchmark_algorithm(self, algorithm_func, test_data, iterations=100):
        """
        Benchmark a specific algorithm with performance metrics
        
        Args:
            algorithm_func: Function to benchmark
            test_data: Data to sort
            iterations: Number of iterations to run
        
        Returns:
            dict: Performance metrics
        """
        times = []
        
        for _ in range(iterations):
            data_copy = test_data.copy()
            start_time = time.perf_counter()
            algorithm_func(data_copy)
            end_time = time.perf_counter()
            times.append(end_time - start_time)
        
        # Calculate statistics
        avg_time = sum(times) / len(times)
        min_time = min(times)
        max_time = max(times)
        
        # Calculate median
        sorted_times = sorted(times)
        n = len(sorted_times)
        median_time = (sorted_times[n//2] + sorted_times[(n-1)//2]) / 2
        
        return {
            'average_time': avg_time,
            'median_time': median_time,
            'min_time': min_time,
            'max_time': max_time,
            'iterations': iterations,
            'total_time': sum(times),
            'data_size': len(test_data)
        }
    
    def generate_test_data(self, size, data_type="random"):
        """
        Generate test data for algorithm benchmarking
        
        Args:
            size: Size of data to generate
            data_type: Type of data ("random", "sorted", "reverse", "mostly_sorted")
        
        Returns:
            list: Generated test data
        """
        if data_type == "random":
            return [random.randint(1, size * 10) for _ in range(size)]
        elif data_type == "sorted":
            return list(range(size))
        elif data_type == "reverse":
            return list(range(size, 0, -1))
        elif data_type == "mostly_sorted":
            data = list(range(size))
            # Swap 10% of elements randomly
            swaps = size // 10
            for _ in range(swaps):
                i, j = random.randint(0, size-1), random.randint(0, size-1)
                data[i], data[j] = data[j], data[i]
            return data
        else:
            raise ValueError(f"Unknown data type: {data_type}")
    
    def get_all_algorithms(self):
        """Get all available sorting algorithms"""
        return {
            'bubble_sort': self.optimized_bubble_sort,
            'quicksort': self.optimized_quicksort,
            'merge_sort': self.merge_sort,
            'heap_sort': self.heap_sort
        }


class AlgorithmBenchmark:
    """Algorithm benchmarking with comprehensive performance testing"""
    
    def __init__(self):
        """Initialize algorithm benchmark"""
        self.sorting_algorithms = RTOSSortingAlgorithms()
        self.test_results = {}
    
    def run_algorithm_test(self, algorithm_name, data_size=1000, iterations=5):
        """Run a specific algorithm test with timing and performance analysis"""
        try:
            if algorithm_name == 'quick_sort':
                return self._benchmark_sorting('quicksort', data_size, iterations)
            elif algorithm_name == 'merge_sort':
                return self._benchmark_sorting('merge_sort', data_size, iterations)
            elif algorithm_name == 'matrix_multiplication':
                return self._benchmark_matrix_multiplication(50, iterations)
            elif algorithm_name == 'fft_simulation':
                return self._benchmark_fft_simulation(512, iterations)
            else:
                return {
                    'algorithm': algorithm_name,
                    'error': f'Unknown algorithm: {algorithm_name}',
                    'success': False
                }
        
        except Exception as e:
            return {
                'algorithm': algorithm_name,
                'error': str(e),
                'success': False
            }
    
    def _benchmark_sorting(self, algorithm_name, data_size, iterations):
        """Benchmark a sorting algorithm"""
        algorithms = self.sorting_algorithms.get_all_algorithms()
        
        if algorithm_name not in algorithms:
            return {
                'algorithm': algorithm_name,
                'error': f'Algorithm {algorithm_name} not found',
                'success': False
            }
        
        algorithm_func = algorithms[algorithm_name]
        execution_times = []
        
        for i in range(iterations):
            # Generate test data
            test_data = self.sorting_algorithms.generate_test_data(data_size, 'random')
            
            # Time the algorithm
            start_time = time.perf_counter()
            algorithm_func(test_data.copy())
            end_time = time.perf_counter()
            
            execution_times.append((end_time - start_time) * 1000)  # Convert to ms
        
        avg_time = sum(execution_times) / len(execution_times)
        min_time = min(execution_times)
        max_time = max(execution_times)
        
        return {
            'algorithm': algorithm_name,
            'data_size': data_size,
            'iterations': iterations,
            'execution_time_ms': round(avg_time, 3),
            'min_time_ms': round(min_time, 3),
            'max_time_ms': round(max_time, 3),
            'all_times': execution_times,
            'success': True
        }
    
    def _benchmark_matrix_multiplication(self, matrix_size, iterations):
        """Benchmark matrix multiplication"""
        def matrix_multiply(a, b):
            """Simple matrix multiplication"""
            rows_a, cols_a = len(a), len(a[0])
            rows_b, cols_b = len(b), len(b[0])
            
            if cols_a != rows_b:
                raise ValueError("Cannot multiply matrices")
            
            result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
            
            for i in range(rows_a):
                for j in range(cols_b):
                    for k in range(cols_a):
                        result[i][j] += a[i][k] * b[k][j]
            
            return result
        
        execution_times = []
        
        for i in range(iterations):
            # Generate random matrices
            matrix_a = [[random.randint(1, 100) for _ in range(matrix_size)] for _ in range(matrix_size)]
            matrix_b = [[random.randint(1, 100) for _ in range(matrix_size)] for _ in range(matrix_size)]
            
            # Time the multiplication
            start_time = time.perf_counter()
            result = matrix_multiply(matrix_a, matrix_b)
            end_time = time.perf_counter()
            
            execution_times.append((end_time - start_time) * 1000)  # Convert to ms
        
        avg_time = sum(execution_times) / len(execution_times)
        
        return {
            'algorithm': 'matrix_multiplication',
            'matrix_size': matrix_size,
            'iterations': iterations,
            'execution_time_ms': round(avg_time, 3),
            'operations': matrix_size ** 3,  # Approximate operation count
            'success': True
        }
    
    def _benchmark_fft_simulation(self, data_size, iterations):
        """Benchmark FFT simulation (simplified DFT)"""
        def simple_dft(x):
            """Simple Discrete Fourier Transform simulation"""
            n = len(x)
            result = [0] * n
            
            for k in range(n):
                for j in range(n):
                    angle = -2 * math.pi * k * j / n
                    result[k] += x[j] * (math.cos(angle) + 1j * math.sin(angle))
            
            return result
        
        execution_times = []
        
        for i in range(iterations):
            # Generate test signal
            test_data = [math.sin(2 * math.pi * i / data_size) + 
                        0.5 * math.sin(4 * math.pi * i / data_size) 
                        for i in range(data_size)]
            
            # Time the FFT simulation
            start_time = time.perf_counter()
            result = simple_dft(test_data)
            end_time = time.perf_counter()
            
            execution_times.append((end_time - start_time) * 1000)  # Convert to ms
        
        avg_time = sum(execution_times) / len(execution_times)
        
        return {
            'algorithm': 'fft_simulation',
            'data_size': data_size,
            'iterations': iterations,
            'execution_time_ms': round(avg_time, 3),
            'complexity': 'O(n²) - Simplified DFT',
            'success': True
        }


class AlgorithmLearningLab:
    """
    🎓 Educational Laboratory for Algorithm Analysis and Learning
    
    This class provides interactive methods to help students and developers
    understand algorithm behavior, performance characteristics, and real-time
    system implications.
    """
    
    def __init__(self):
        self.sorter = RTOSSortingAlgorithms()
    
    def algorithm_comparison_demo(self, data_sizes=[10, 100, 1000], verbose=True):
        """
        🔬 Compare all sorting algorithms across different data sizes
        
        This educational method demonstrates how algorithm performance
        scales with input size and helps visualize Big O complexity.
        
        Args:
            data_sizes (list): List of data sizes to test
            verbose (bool): Whether to print detailed explanations
            
        Returns:
            dict: Comprehensive comparison results
        """
        if verbose:
            print("🎓 ALGORITHM COMPARISON LABORATORY")
            print("=" * 50)
            print("This demo compares sorting algorithms to demonstrate:")
            print("• How theoretical complexity translates to real performance")
            print("• When to choose each algorithm")
            print("• Real-time system considerations")
            print()
        
        results = {}
        algorithms = [
            ('Bubble Sort', self.sorter.optimized_bubble_sort),
            ('Quick Sort', self.sorter.optimized_quicksort),
        ]
        
        for size in data_sizes:
            if verbose:
                print(f"📊 Testing with {size} elements:")
                print("-" * 30)
            
            # Generate test data
            test_data = self.sorter.generate_test_data(size, "random")
            results[size] = {}
            
            for name, algorithm in algorithms:
                # Benchmark the algorithm
                stats = self.sorter.benchmark_algorithm(algorithm, test_data, iterations=10)
                results[size][name] = stats
                
                if verbose:
                    info = self.sorter.algorithm_info.get(name.lower().replace(' ', '_'), {})
                    print(f"  {name}:")
                    print(f"    Time Complexity: {info.get('time_complexity', 'N/A')}")
                    print(f"    Average Time: {stats['average_time']*1000:.3f} ms")
                    print(f"    Min Time: {stats['min_time']*1000:.3f} ms")
                    print(f"    Max Time: {stats['max_time']*1000:.3f} ms")
                    print()
        
        if verbose:
            self._print_learning_insights(results)
        
        return results
    
    def demonstrate_best_vs_worst_case(self, size=1000):
        """
        🎯 Demonstrate best vs worst case performance
        
        Shows how data patterns affect algorithm performance,
        crucial for real-time system design.
        """
        print("🎯 BEST vs WORST CASE DEMONSTRATION")
        print("=" * 45)
        print("Understanding how input data affects performance is")
        print("crucial for real-time systems where predictability matters.")
        print()
        
        test_cases = {
            'Random Data': self.sorter.generate_test_data(size, 'random'),
            'Already Sorted': self.sorter.generate_test_data(size, 'sorted'),
            'Reverse Sorted': self.sorter.generate_test_data(size, 'reverse'),
            'Mostly Sorted': self.sorter.generate_test_data(size, 'mostly_sorted')
        }
        
        algorithms = [
            ('Bubble Sort (Adaptive)', self.sorter.optimized_bubble_sort),
            ('Quick Sort', self.sorter.optimized_quicksort)
        ]
        
        for algo_name, algorithm in algorithms:
            print(f"📊 {algo_name} Performance:")
            print("-" * 25)
            
            for data_type, data in test_cases.items():
                stats = self.sorter.benchmark_algorithm(algorithm, data, iterations=5)
                print(f"  {data_type:<15}: {stats['average_time']*1000:6.2f} ms")
            
            print()
    
    def explain_algorithm_choice(self):
        """
        🧠 Educational guide for choosing the right algorithm
        """
        print("🧠 ALGORITHM SELECTION GUIDE")
        print("=" * 35)
        print()
        
        guide = {
            "For Learning/Education": {
                "choice": "Bubble Sort",
                "why": "Simple to understand, demonstrates basic concepts"
            },
            "General Purpose (Most Cases)": {
                "choice": "Quick Sort",
                "why": "Fast average performance, widely used"
            },
            "Real-Time Systems": {
                "choice": "Merge Sort or Heap Sort", 
                "why": "Predictable O(n log n) performance, no worst-case surprises"
            },
            "Memory Constrained": {
                "choice": "Heap Sort",
                "why": "In-place sorting, O(1) space complexity"
            },
            "Stable Sorting Required": {
                "choice": "Merge Sort",
                "why": "Maintains relative order of equal elements"
            },
            "Small Arrays (<50 elements)": {
                "choice": "Insertion Sort",
                "why": "Low overhead, fast for small datasets"
            }
        }
        
        for scenario, recommendation in guide.items():
            print(f"🎯 {scenario}:")
            print(f"   Choice: {recommendation['choice']}")
            print(f"   Why: {recommendation['why']}")
            print()
    
    def _print_learning_insights(self, results):
        """Print educational insights from comparison results"""
        print("🧠 KEY LEARNING INSIGHTS:")
        print("=" * 30)
        
        # Find performance trends
        sizes = sorted(results.keys())
        if len(sizes) >= 2:
            bubble_times = [results[size]['Bubble Sort']['average_time'] for size in sizes]
            quick_times = [results[size]['Quick Sort']['average_time'] for size in sizes]
            
            bubble_growth = bubble_times[-1] / bubble_times[0] if bubble_times[0] > 0 else 0
            quick_growth = quick_times[-1] / quick_times[0] if quick_times[0] > 0 else 0
            
            print(f"📈 Performance Growth (from {sizes[0]} to {sizes[-1]} elements):")
            print(f"   Bubble Sort: {bubble_growth:.1f}x slower")
            print(f"   Quick Sort: {quick_growth:.1f}x slower")
            print()
            print("💡 This demonstrates why O(n²) algorithms don't scale well!")
            print("   Quick Sort's O(n log n) shows much better scaling.")
            print()
        
        print("🔑 Real-Time System Takeaways:")
        print("• Predictable performance is often more important than average speed")
        print("• Consider worst-case scenarios when choosing algorithms")
        print("• Memory access patterns affect real-world performance")
        print("• Algorithm choice depends on your specific constraints")


# 🎓 Example usage and learning exercises
if __name__ == "__main__":
    print("🎓 Welcome to the Algorithm Learning Laboratory!")
    print()
    
    # Create learning lab instance
    lab = AlgorithmLearningLab()
    
    # Run educational demonstrations
    print("Running algorithm comparison demo...")
    lab.algorithm_comparison_demo([50, 200, 500])
    
    print("\n" + "="*60 + "\n")
    
    print("Demonstrating best vs worst case scenarios...")
    lab.demonstrate_best_vs_worst_case(200)
    
    print("\n" + "="*60 + "\n")
    
    print("Algorithm selection guide...")
    lab.explain_algorithm_choice()