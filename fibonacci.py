# problem : https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
# solution using dynmaic programming technique memoization
def fib(n,memo):
    if memo[n] is not None:
        return memo[n]
    if n==1 or n==2 :
        return 1
    else :
        res=fib(n-1,memo)+fib(n-2,memo)
        memo[n]=res
        return res%1000000007 # to nandel very large numbers

N=int(input())
memo=[None]*(N+1)
print(fib(N,memo))