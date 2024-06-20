c=[1,3,4,5]
c.sort()
t=c.copy()
n=22
def fun(n):
    count=0
    while(n>0):
        if len(t)==0:
            break
        if n<(max(t)):
            t.pop()
        else:
            if ((n-max(t))!=0) and ((n-max(t))<(min(t))) and (len(t)!=1):
                t.pop()
            else:
                if n in t:
                    n=n-n
                    count+=1
                else:
                    n=n-max(t)
                    count+=1
        if n<min(t) and n not in t and n!=0:
            count=-1
            break
    return count

a=fun(n)
t=c.copy()
t=t[1:]
# print(t,n)

b=fun(n)
# print(a,b)
print(min(a,b) if a>0 and b>0 else a)