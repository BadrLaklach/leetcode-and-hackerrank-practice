"""
===========================================================
    VALID PARENTHESES — MULTIPLE METHODS
===========================================================

📌 Problem Summary:
Given a string 's' containing just the characters '(', ')', 
'{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket.

Example:
    Input:  s = "()[]{}"
    Output: true

This file includes TWO methods:
    1. Brute Force String Replacement (O(n²))
    2. Stack (O(n) - Optimal)
"""

from typing import List

# ===========================================================
# 1. BRUTE FORCE METHOD
# ===========================================================
class SolutionBruteForce:
    """
    ----------------------------------------------------------
    🔹 METHOD 1 — STRING REPLACEMENT
    ----------------------------------------------------------
    Intuition:
    If a string is valid, there must be at least one pair of 
    adjacent matching brackets (like "()"). We can repeatedly 
    remove these pairs. If the string is valid, it will eventually 
    become empty.

    Time Complexity:  O(n²) - because .replace() is O(n) inside a loop
    Space Complexity: O(n) - string copies created during replacement
    """
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''


# ===========================================================
# 2. STACK METHOD (OPTIMAL)
# ===========================================================
class SolutionStack:
    """
    ----------------------------------------------------------
    🔹 METHOD 2 — STACK (LIFO)
    ----------------------------------------------------------
    Intuition:
    Parentheses follow a "Last-In, First-Out" logic. The last 
    bracket opened must be the first one closed. A stack perfectly 
    models this behavior. We push opening brackets and pop them 
    when we find a matching closing bracket.

    

    Algorithm:
        1. Initialize an empty stack.
        2. Map closing brackets to their opening counterparts.
        3. For each char:
           - If it's a closing bracket, check if stack top matches.
           - If it's an opening bracket, append to stack.
        4. Return True if stack is empty at the end.

    Time Complexity:  O(n) - Single pass through the string
    Space Complexity: O(n) - In the worst case (all opening brackets)
    """
    def isValid(self, s: str) -> bool:
        stack = []
        # Mapping: Closing bracket -> Opening bracket
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closeToOpen:
                # If stack exists and top matches the required opening bracket
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                # It is an opening bracket
                stack.append(c)

        # String is valid only if all brackets were matched and popped
        return True if not stack else False


# ===========================================================
# 📌 METHOD SUMMARY & SYNTAX NOTES
# ===========================================================
"""
METHOD APPLICATION:
- The Stack method is the standard solution for matching problems. 
- The Brute Force method is slow but clever for very small strings 
  or non-time-critical scripts.

IMPORTANT SYNTAX:
1. stack[-1]: Accesses the top element of the stack without removing it.
2. if stack: A concise way to check if a list is not empty before popping.
3. closeToOpen[c]: Dictionary lookup to quickly find the matching pair.
4. not stack: Returns True if the list is empty, which confirms all 
   parentheses were matched.
"""

# ===========================================================
# EXAMPLE USAGE 
# ===========================================================
if __name__ == "__main__":
    test_str = "{[()]}"
    sol = SolutionStack()
    print(f"String: {test_str}")
    print(f"Is Valid: {sol.isValid(test_str)}")