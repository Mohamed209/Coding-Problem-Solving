from typing import List

cache = {}


def canSum(target: int, nums: List[int]):
    # handle base cases
    """
    because we are solving the problem top-down approach , so we will subtract from the target sum
    every elemnt in nums (check decesion tree ../images/Can Sum.png) , so if there is a path in the tree that ends with 0
    this means that the target can be constructed from this path
    note : in ../images/Can Sum.png , we must use caching (memoaization) 
    """
    if target == 0:
        return True
    if target < 0:
        return False
    if target in cache:
        return cache[target]
    for num in nums:
        if canSum(target-num, nums):
            cache[target] = True
            return True
    cache[target] = False
    return False


print(canSum(7, [2, 3]))
print(canSum(7, [3, 5, 4, 7]))
print(canSum(7, [2, 4]))
print(canSum(8, [2, 3, 5]))
print(canSum(300, [7, 14]))

print("#"*10)
# Tabulation


def canSum(target: int, nums: List[int]):
    # populate table with false
    table = [False]*(target+1)
    table[0] = True
    """
    1- every element in nums should have true in table as it can be constructed from the array
    2- at any index i in the table , i+n for n in nums should be true
    """
    for i in range(0, len(table)):
        if table[i] == True:
            for n in nums:
                if i+n < len(table):
                    table[i+n] = True
    return table[-1]


print(canSum(7, [2, 3]))
print(canSum(7, [3, 5, 4, 7]))
print(canSum(7, [2, 4]))
print(canSum(8, [2, 3, 5]))
print(canSum(300, [7, 14]))
