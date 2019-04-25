# problem : https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0
T=int(input()) # test cases
for case in range(T):
    N,S=[int(x) for x in input().split()]# N : array size ,S=sum
    array=[]
    # get array
    for i in range(N):
        array.append(int(input()))
    for j in range(N):
        sum = array[j]
        for k in range(j+1,N):
            while(sum<S):
                sum=sum+array[k]
                k=k+1
            if(sum==S):
                print(j+1,k)
                break
        if (sum==S):
            break
