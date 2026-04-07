#!/bin/python3
"""
===========================================================
  COUNT ELEMENTS GREATER THAN PREVIOUS AVERAGE (EASY)
===========================================================

📌 Problem Summary:
Given an array of positive integers, return the number of elements 
that are strictly greater than the average of all previous elements. 
Skip the first element.

Example:
Input: responseTimes = [100, 200, 150, 300]
Output: 2

Explanation:
- Day 0: 100 (no previous days, skip) 
- Day 1: 200 > average(100) = 100 → count = 1 
- Day 2: 150 vs average(100, 200) = 150 → not greater → count = 1 
- Day 3: 300 > average(100, 200, 150) = 150 → count = 2 
Return 2.

We will show an O(n) Time Complexity method to solve this problem.

This method has:
    - Explanation
    - Step-by-step reasoning
    - Full code
    - Time & Space complexity
"""

import math
import os
import random
import re
import sys
from typing import List

# ===========================================================
# 1. RUNNING SUM METHOD (ONE PASS)
# ===========================================================
class SolutionRunningSum:
    """
    ----------------------------------------------------------
    🔹 METHOD 1 — RUNNING SUM (OPTIMAL)
    ----------------------------------------------------------
    Intuition:
    To find if an element is strictly greater than the average 
    of all previous elements, we don't need to recalculate the 
    sum of previous elements from scratch each time. Instead, 
    we maintain a `running_sum` as we iterate through the array.

    How it works:
        • Loop `i` from 0 to n-1.
        • For each element, if it's not the first element (i > 0),
          we calculate the average of previous elements as `(running_sum / i)`.
        • Check if `time > (running_sum / i)`.
        • If true, increment the `count`.
        • Always add the current `time` to the `running_sum`.

    This allows us to process the array in a single pass efficiently.

    Time Complexity:
        O(n) — single pass through the array.
    Space Complexity:
        O(1) — variables for sum and count, no extra structures.
    """

    def countResponseTimeRegressions(self, responseTimes: List[int]) -> int:
        if not responseTimes:
            return 0
        
        count = 0
        running_sum = 0
        
        for i, time in enumerate(responseTimes):
            # Check if strictly greater than the average of previous elements
            if i > 0 and time > (running_sum / i):
                count += 1
            
            # Update the running sum for the next iterations
            running_sum += time
            
        return count

# ===========================================================
# ORIGINAL HACKERRANK SOLUTION FORMAT
# ===========================================================
def countResponseTimeRegressions(responseTimes):
    """
    Original function format as provided by HackerRank.
    """
    if not responseTimes:
        return 0
    
    count = 0
    running_sum = 0
    
    for i, time in enumerate(responseTimes):
        if i > 0 and time > (running_sum / i):
            count += 1
        running_sum += time
        
    return count

# ===========================================================
# EXAMPLE USAGE 
# ===========================================================
if __name__ == '__main__':
    # Default sample testcase, mimics HackerRank environment or local execution
    try:
        responseTimes_count = int(input().strip())
        responseTimes = []

        for _ in range(responseTimes_count):
            responseTimes_item = int(input().strip())
            responseTimes.append(responseTimes_item)

        result = countResponseTimeRegressions(responseTimes)
        print(result)
    except EOFError:
        # Fallback to a hardcoded testcase if running directly without stdin
        print("--- Running Default Demo Testcase ---")
        sample_times = [100, 200, 150, 300]
        print(f"Input: {sample_times}")
        print("Output:", countResponseTimeRegressions(sample_times))
        print("Expected: 2")
