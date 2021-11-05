# problem : https://leetcode.com/problems/daily-temperatures/
from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    stack: List[int] = []
    result: List[int] = [0]*len(temperatures)
    stack.append(0)
    for i in range(1, len(temperatures)):
        while temperatures[i] > temperatures[stack[-1]]:
            result[stack[-1]] = i-stack[-1]
            stack.pop()
            if len(stack) == 0:
                break
        stack.append(i)
    return result


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
