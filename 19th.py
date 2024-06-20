def fun(x,s):
    s+=x%10
    x=x//10
    if x!=0:
        s=s*10
        s=fun(x,s)
    return s
     
n=12321
s=0
y=fun(n,s)
if(y==n):
    print("Yes")
else:
    print("No")