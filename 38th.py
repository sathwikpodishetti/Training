#{5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
d={5:[(7,4),(3,1)],7:[(5,4),(4,1),(3,3)],4:[(7,1),(8,8),(2,3)],8:[(3,2),(4,8),(2,4)],3:[(5,1),(7,3),(8,2)],2:[(4,3),(8,4)]}
def fun(d,x,e,l,c,m):
    l.append(x)
    if x==e:
        print(l,"=",c)
        if(c<m):
            m=c
            l1=l.copy()
#             print(l1,c)
            l.pop()
            return m,l1
        else:
            l.pop()
            return m,l
    for i in d[x]:
        if i[0] not in l:
            m,l=fun(d,i[0],e,l,c+i[1],m)
    l.pop()
    return m,l
print(fun(d,5,2,l=[],c=0,m=9999))