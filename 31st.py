s="abfgresagtyuiofds"
a=0
m=0
while(a<len(s)):
#     print("o",end="")
    c=0
    t=""
    for i in range(a,len(s)):
#         print("i",end="")	
        if s[i] not in t:
            t+=s[i]
            c+=1
        else:
            a=s[:i].index(s[i])
#             print(a)
            a+=1
            break
    if m<=c:
        m=c
    if i==len(s)-1:
        break
print("\n",m)