# problem : https://practice.geeksforgeeks.org/problems/length-unsorted-subarray/0
# code
T = int(input())
for t in range(T):
    N = int(input())
    array = [int(i)for i in input().split()]
    sorted_array = sorted(array)
    idxs = []
    for j in range(N):
        if array[j] != sorted_array[j]:
            idxs.append(j)
    if len(idxs) > 0:
        print(idxs[0], idxs[-1])
    else:
        print(0, 0)
