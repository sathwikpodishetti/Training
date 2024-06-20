n=[14,16,20,22]
def lprime(x):
    f=1
    for i in range(2,x//2):
        if x%i==0:
            f=0
            break
        else:
            f=1
    return f
s=0
for i in range(len(n)-1):
    m=0
    k=n[i+1]
    while k!=n[i]:
        v=lprime(k)
        if v==1 and m==0:
            m=k
            print(k,end=" ")
            break
        k-=1
    s+=m
print(":",s)