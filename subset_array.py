# problem :
T = int(input())
for t in range(T):
    mn = [int(i) for i in input().split(' ')]
    m = mn[0]
    n = mn[1]
    array_big = [int(i) for i in input().split(' ')]
    array_small = [int(i) for i in input().split(' ')]
    array_big.extend(array_small)
    freq = {}
    for item in array_big:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    subset = 'Yes'
    for item in array_small:
        if freq[item] == 1:
            subset = 'No'
            break
    print(subset)
