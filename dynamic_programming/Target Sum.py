# https://www.geeksforgeeks.org/problems/target-sum-1626326450/1
"""
                    0
                  /   \
                +1     -1
               /  \    /  \
             +2   -2  +2   -2
            / \   / \ / \  / \
           +3 -3 +3-3+3 -3+3 -3
           │   │  │ ││  ││   │
           6   0  4-44 -22  -6-8
                               ↑
                          Only this = 2 ✅
"""

from functools import cache


class Solution:
    def totalWays(self, arr, target):
        # code here
        @cache
        def dfs(i, target):
            if i == len(arr):
                return 1 if target == 0 else 0
            return dfs(i + 1, target + arr[i]) + dfs(i + 1, target - arr[i])

        return dfs(0, target)


"""Test cases for Target Sum problem"""


def run_tests():
    sol = Solution()
    test_cases = [
        # (arr, target, expected, description)
        # Given examples
        ([1, 1, 1, 1, 1], 3, 5, "Example 1: Five 1s, target 3"),
        ([1, 2, 3], 2, 1, "Example 2: [1,2,3], target 2"),
        # Single element cases
        ([5], 5, 1, "Single element matches target (+5)"),
        ([5], -5, 1, "Single element matches target (-5)"),
        ([5], 0, 0, "Single element cannot make 0"),
        ([5], 10, 0, "Single element, target too large"),
        # Two elements
        ([1, 1], 0, 2, "Two 1s, target 0: +1-1 or -1+1"),
        ([1, 1], 2, 1, "Two 1s, target 2: +1+1"),
        ([1, 1], -2, 1, "Two 1s, target -2: -1-1"),
        ([3, 5], 2, 1, "[3,5], target 2: -3+5"),
        ([3, 5], 8, 1, "[3,5], target 8: +3+5"),
        ([3, 5], -8, 1, "[3,5], target -8: -3-5"),
        ([3, 5], 0, 0, "[3,5], target 0: impossible"),
        # All same elements
        ([2, 2, 2], 6, 1, "Three 2s, target 6: all positive"),
        ([2, 2, 2], -6, 1, "Three 2s, target -6: all negative"),
        ([2, 2, 2], 2, 3, "Three 2s, target 2: one negative"),
        ([2, 2, 2], -2, 3, "Three 2s, target -2: one positive"),
        ([2, 2, 2], 0, 0, "Three 2s, target 0: impossible (odd count)"),
        # Target is 0
        ([1, 2, 3], 0, 2, "Target 0: +1+2-3 or -1-2+3"),
        ([1, 2, 1], 0, 2, "Target 0: -1+2-1 or +1-2+1"),
        # Negative target
        ([1, 2, 3], -2, 1, "Negative target: +1-2-3"),
        ([1, 1, 1, 1, 1], -3, 5, "Negative target: symmetric to positive"),
        # Larger array
        ([1, 2, 3, 4, 5], 3, 3, "Five elements, target 3"),
        ([1, 2, 3, 4, 5], 15, 1, "Five elements, max sum (all positive)"),
        ([1, 2, 3, 4, 5], -15, 1, "Five elements, min sum (all negative)"),
        # Impossible cases
        ([1, 2, 3], 10, 0, "Target exceeds max possible sum"),
        ([1, 2, 3], -10, 0, "Target below min possible sum"),
        # Edge: parity check (sum and target must have same parity)
        ([1, 2], 0, 0, "Sum=3 (odd), target=0 (even): impossible"),
        ([1, 2, 3], 1, 0, "Sum=6 (even), target=1 (odd): impossible"),
    ]

    passed = 0
    failed = 0

    print(f"\n{'='*70}")
    print(f"Running Target Sum Test Cases")
    print(f"{'='*70}\n")

    for i, (arr, target, expected, desc) in enumerate(test_cases, 1):
        result = sol.totalWays(arr, target)
        status = "✅ PASS" if result == expected else "❌ FAIL"

        if result == expected:
            passed += 1
        else:
            failed += 1

        print(f"Test {i:2d}: {status}")
        print(f"         {desc}")
        print(f"         arr={arr}, target={target}")
        print(f"         Expected: {expected}, Got: {result}")
        print()

    print(f"{'='*70}")
    print(f"Results: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print(f"{'='*70}\n")

    return failed == 0


if __name__ == "__main__":
    run_tests()
