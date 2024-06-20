a=list(map(str,input(":")))
u=l=n=s=result=0
for i in a:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
    elif i.isnumeric():
        n+=1
    else:
        s+=1
print(u,l,n,s)
if u==0:
    result+=1
if l==0:
    result+=1
if n==0:
    result+=1
if s==0:
    result+=1
if result<(8-len(a)):
    result+=(8-len(a))-result
if result==0:
    print(-1)
else:
    print(result)