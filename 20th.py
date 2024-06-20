n=[5,2,9,1,10,8,4,7]
j=len(n)-1
i=0
j=len(n)-1
for k in range(len(n)-1):
    if n[i+1]<n[i]:
        i+=1
    if n[j-1]>n[j]:
        j-=1
    if j+i<=0:
        break
    
print(n[i]-n[j])        
        
    
        