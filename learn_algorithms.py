#!/usr/bin/env python3
"""
Algorithm Learning Demo
======================

This demo script shows how to use the educational features
of the algorithms.py module for learning purposes.

Run this to see algorithm comparisons and educational explanations!

Author: Domas Užkuraitis
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from src.algorithms import AlgorithmLearningLab, RTOSSortingAlgorithms
except ImportError:
    print("❌ Could not import algorithms module")
    print("Make sure you're running from the rtos_benchmark directory")
    sys.exit(1)


def main():
    """Main educational demonstration"""
    print("🎓 RTOS ALGORITHMS - EDUCATIONAL DEMONSTRATION")
    print("=" * 55)
    print("This demonstration will teach you about:")
    print("• Algorithm complexity in practice")
    print("• When to choose each sorting algorithm")
    print("• Real-time system considerations")
    print("• Performance analysis techniques")
    print()
    
    input("Press Enter to start the learning experience...")
    print()
    
    # Create learning lab
    lab = AlgorithmLearningLab()
    
    # Demo 1: Algorithm comparison
    print("DEMO 1: Algorithm Performance Comparison")
    print("-" * 40)
    lab.algorithm_comparison_demo([25, 100, 400])
    
    print("\n" + "="*60 + "\n")
    input("Press Enter to continue to the next demo...")
    
    # Demo 2: Best vs worst case
    print("DEMO 2: Best vs Worst Case Analysis")
    print("-" * 35)
    lab.demonstrate_best_vs_worst_case(300)
    
    print("\n" + "="*60 + "\n")
    input("Press Enter to see the algorithm selection guide...")
    
    # Demo 3: Algorithm selection guide
    print("DEMO 3: How to Choose the Right Algorithm")
    print("-" * 40)
    lab.explain_algorithm_choice()
    
    print("\n" + "="*60)
    print("🎉 Educational demonstration complete!")
    print()
    print("💡 What you learned:")
    print("• Big O notation reflects real-world performance trends")
    print("• Algorithm choice depends on your specific requirements")
    print("• Real-time systems need predictable performance")
    print("• Input data patterns significantly affect performance")
    print()
    print("🚀 Try modifying the demo parameters and run again!")
    print("🔬 Experiment with different data sizes and patterns!")


if __name__ == "__main__":
    main()