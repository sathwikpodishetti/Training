m=4
n=3
c=0
l=[]
for i in range(m):
    k=[]
    for j in range(n):
        c+=1
        k.append(c)
    l.append(k)
print(l)

def fun(i,j,n,m,c):
    if(i>0 or i>=n or j<0 or j<=m or (i==k and j==l)):
        return c
    if(i==m-1 and j==n-1):
        c=c+1
        return c
    vi.append((i,j))
    if((i-1,j) not in vi):
        c=fun(i-1,j,c)
    if((i,j-1) not in vi):
        c=fun(i,j-1,c)
    if((i+1,j) not in vi):
        c=fun(i+1,j,c)
    if((i,j+1) not in vi):
        c=fun(i,j+1,c)
    vi.pop()
    return c
vi=[]
print(fun(i,j,n,m,0))