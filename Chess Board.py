# problem link : https://cpracticeprograms.blogspot.com.eg/2018/05/chess-board.html
# Solution
n,m = map(int,input().split())
b=[['. ' for x in range(m)]for y in range(n)]
for i in range(n):
    for j in range(m):
        if(i%2==0 and j%2!=0):
            b[i][j]='* '
        elif(i%2!=0 and j%2==0):
            b[i][j]='* '
for i in range(n):
    for j in range(m):
        print(b[i][j],end="")
    print('\n')
