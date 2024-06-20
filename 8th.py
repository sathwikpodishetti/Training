a=52
i=2
count=0
while i<(a//2 if a > 6 else a):
    count+=1
    if a%i==0:
        a+=1
        i=2
    else:
        i+=1
    if i==(a//2 if a > 6 else a):
        print(a)
        break
print("total iterations",count)
