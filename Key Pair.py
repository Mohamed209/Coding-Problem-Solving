# Problem :https://practice.geeksforgeeks.org/problems/key-pair/0
# Solution:
T=int(input())#Test cases
for t in range(0,T):#looping through all test cases
    N_X = [int(x) for x in input().split()]
    flag=0
    A=[int(y) for y in input().split()]#read elements separated by space
    for a in range(N_X[0]):
        if N_X[1]-A[a] in A:#if number complement found in A[] print yes
            print("Yes")
            flag=1
            break
    if(flag==0):
print("No")
