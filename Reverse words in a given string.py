#problem: https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string/0
# Solution:
T=int(input())#Test cases
for t in range(0,T):#looping through all test cases
    string=[x for x in input().split(".")]
print(*string[::-1],sep='.')
