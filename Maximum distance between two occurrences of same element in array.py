def maxDistance(arr, n):
    # Code here
    # using hashing O(n)
    freq = {}
    for i in range(len(arr)):
        if arr[i] not in freq:
            freq[arr[i]] = [i]
        else:
            freq[arr[i]].append(i)
    max_dif = 0
    for key in freq:
        dif = freq[key][-1]-freq[key][0]
        if dif > max_dif:
            max_dif = dif
    return max_dif
