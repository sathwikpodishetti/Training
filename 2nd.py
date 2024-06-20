a="aaabbaaaadddssss"
new=""
count=i=0
j=a[i]
while(i<len(a)):
    if j==a[i]:
        count+=1
    else:
        new+=j
        new+=str(count)
        j=a[i]
        count=1
    i+=1
new+=j
new+=str(count)
print(new)
