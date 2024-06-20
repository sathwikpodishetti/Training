# n=int(input())
n=6
# g=[list(map(int,input().split())) for _ in range(n)]
g=[[0,1,1,1,0,1],[0,1,0,1,0,0],[1,0,1,1,0,0],[0,0,0,1,1,1],[1,1,0,0,0,1],[1,1,1,0,1,0]]
i,j=3,5
def fun(i,j):
    if(not (0<=i<n and 0<=j<n)) or g[i][j]==0 :
        return
    else:
        g[i][j]=0
        fun(i-1,j)
        fun(i,j-1)
        fun(i+1,j)
        fun(i,j+1)
fun(i,j)
for i in g:
    print(i)
print(sum([sum(g[row]) for row in range(len(g))]))
        