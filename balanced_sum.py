# problem >> https://www.hackerrank.com/challenges/sherlock-and-array/problem
def balancedSums(arr, l, r):
    # recursive approach O(log(n))
    if r >= l:
        mid = l + (r - l) // 2
        if sum(arr[:mid]) == sum(arr[mid+1:]):
            return 'YES'
        elif sum(arr[:mid]) > sum(arr[mid+1:]):
            return balancedSums(arr, l, mid-1)
        else:
            return balancedSums(arr, mid + 1, r)
    else:
        # Element is not present in the array
        return 'NO'