# count or biggest island
l=[[0,1,0,0,1],[1,0,0,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,1]]
c=0
i=0
j=0
def fun(i,j):
    if l[i][j]==1:
        l[i][j]=0
    else:
        return
    if i>0:
        fun(i-1,j)
    if i<4:
        fun(i+1,j)
    if j>0:
        fun(i,j-1)
    if j<4:
        fun(i,j+1)
    return 
c=0
for i in range(5):
    for j in range(5):
        if l[i][j]==1:
            c+=1
            fun(i,j)
print(c)