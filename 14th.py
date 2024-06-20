a=[1,2,3,4,5,6,7,8]
i=0
count=0
while(1):
    count+=1
    if a[-2]==a[i]:
        print(i+2)
        break
    elif a[-1]==a[i]:
        print(i)
        break
    else:
        i+=2
print(count)
        