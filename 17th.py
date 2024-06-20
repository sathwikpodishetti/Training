s="sabcthwik"
count=0
temp=0
for i in range(len(s)):
    if i==0:
        count=1
    elif (ord(s[i-1])+1)==ord(s[i]):
        count+=1
    else:
        if count>temp:
            temp=count
        count=1
print(temp if temp>count else count)