#missing numbers in array
n=6
l=[0,5,3,6,7,1]
l.sort()
t=l[0]
for i in range(1,n):
    if t+1!=l[i]:
        print(t+1)
    t=l[i]
