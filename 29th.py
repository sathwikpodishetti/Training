n=[2,3,1,4,3,2,3]
l=[]
t=[]
def fun(n,l,t):
    x=n
    if len(n)==0:
        return l
    else:
        n=[]
        for i in x:
            if i not in t:
                t.append(i)
            else:
                n.append(i)
        l.append(t)
        t=[]
        return fun(n,l,t)
print(fun(n,l,t))
        