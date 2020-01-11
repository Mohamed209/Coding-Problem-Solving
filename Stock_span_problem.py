# Problem Link : https://www.geeksforgeeks.org/the-stock-span-problem/
# straight forward solution O(n^2)
D = [10, 4, 5, 90, 120, 80]
S = [1]
counter = 1
for i in range(1, len(D)):
    for j in range(0, i):
        if D[i-1-j] <= D[i]:
            counter += 1
        else:
            break
    S.append(counter)
    counter = 1
print(S)
# solution using stack O(n)
a = [10, 4, 5, 90, 120, 80]
stack = [0]
span = [1]
for i in range(1, len(a)):
    while len(stack) != 0 and a[i] > a[stack[-1]]:
        stack.pop()
    if len(stack) == 0:
        span.append(i+1)
    else:
        span.append(i-stack[-1])
    stack.append(i)
print(span)
