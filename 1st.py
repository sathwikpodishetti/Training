a = [2,5,7,8,9]
b = [1,3,6,7,10,13]
c=[]
i=j=0
while(i<len(a) and j<len(b)):
    if i<j:
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1
if j<len(b):
    c=c+b[j:len(b)]
if i<len(a):
    c=c+a[i:len(a)]
print(c)
