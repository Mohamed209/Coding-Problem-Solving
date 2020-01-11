# problem : https://www.geeksforgeeks.org/the-celebrity-problem/
def getId(m, n):
    # code here
    stack = []
    for i in range(n):
        for j in range(n):
            if i == j:
                pass
            else:
                if m[i][j] == 1:
                    if len(stack) > 0 and j != stack[-1]:
                        return -1
                    else:
                        stack.append(j)
                        break
    if len(stack) == n-1:
        return stack[-1]
    else:
        return -1


a = [[0, 0, 1, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 0],
     [0, 0, 1, 0]]
b = [[0, 0, 0, 1, 0],
     [0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0]]
print(getId(b, 5))
