#problem : https://cpracticeprograms.blogspot.com.eg/2018/05/the-diagonal-parallel-to-main.html
#solution
n= int(input())
b=[[abs(x-y) for x in range(n)]for y in range(n)]
for i in range(n):
    for j in range(n):
        print(b[i][j],end=" ")
    print('\n')
