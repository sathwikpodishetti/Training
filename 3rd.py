a=[3,5,4,3,6,7,1,2,4,3,3,7,6,8,8]
a.sort()
print(a)
new=[]
count=i=0
j=a[i]
while(i<len(a)):
    if j==a[i]:
        count+=1
    else:
        new.append(j)
        new.append(count)
        j=a[i]
        count=1
    i+=1
new.append(j)
new.append(count)
for i in range(0,len(new),2):
    print(new[i],"-",new[i+1])

