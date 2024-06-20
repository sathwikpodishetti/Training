#most repeated element
n=[1,1,1,2,2,2,2]
c=0
for i in range(len(n)):
    if c==0:
        ch=n[i]
        c+=1
    else:
        if n[i]==ch:
            c+=1
        else:
            c-=1
    if c==0 and i==len(n)-1:
        ch="draw"
            
print(ch)