# problem >>> https://www.hackerrank.com/challenges/pairs/problem
def pairs(k, arr):
    d = {}
    count = 0
    for i in range(len(arr)):
        d[arr[i]] = i
    for i in range(len(arr)):
        if arr[i]+k in d:
            count += 1
    return count
