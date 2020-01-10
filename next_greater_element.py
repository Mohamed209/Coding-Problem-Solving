# code
T = int(input())
for t in range(T):
    N = int(input())
    array = [int(i)for i in input().split()]
    stack = []
    NG = {}
    stack.append(array[0])
    for j in range(1, N):  # O(n)
        while (len(stack) != 0) and(array[j] > stack[-1]):
            NG[stack[-1]] = array[j]
            stack.pop()
        stack.append(array[j])
    for element in stack:
        NG[element] = -1
    for el in array:
        print(NG[el], end=' ')
