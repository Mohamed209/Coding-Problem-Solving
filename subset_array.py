# problem : https://practice.geeksforgeeks.org/problems/array-subset-of-another-array/0
def binarySearch(arr, low, high, x):
    if(high >= low):
        mid = (low + high)//2
        if((mid == 0 or x > arr[mid-1]) and (arr[mid] == x)):
            return mid
        elif(x > arr[mid]):
            return binarySearch(arr, (mid + 1), high, x)
        else:
            return binarySearch(arr, low, (mid - 1), x)
    return -1


T = int(input())
for t in range(T):
    mn = [int(i) for i in input().split(' ')]
    m = mn[0]
    n = mn[1]
    array_big = [int(i) for i in input().split(' ')]
    array_small = [int(i) for i in input().split(' ')]
    # sort both arrays O(nlog(n))
    array_big = sorted(array_big)
    array_small = sorted(array_small)
    # O(log(n)) binary search
    subset = 'Yes'
    for i in range(n):
        if binarySearch(array_big, 0, m-1, array_small[i]) == -1:
            subset = 'No'
    print(subset)
