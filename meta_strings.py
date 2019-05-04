# problem : https://www.geeksforgeeks.org/meta-strings-check-two-strings-can-become-swap-one-string/
# Solution
T=int(input())
for t in range(T):
    flag=0
    sindex=0
    str1,str2=input().split()
    if len(str1)!=len(str2):
        print(flag)
    else :
        for i in range(len(str1)):
            if str1[i] != str2[i] and not flag:
                sindex=i
                for j in range(i+1,len(str2)):
                    if str2[j]!=str1[j]:
                        if str2[j]==str1[sindex] and str1[j]==str2[sindex]:
                            flag=1
        print(flag)