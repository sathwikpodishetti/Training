a="MFMFF"
c=0
for i in range(len(a)):
    if a[i]=="M":
        c+=1
    elif a[i]=="F":
        c-=1
if c>0:
    print("M wins with",c,"majority")
elif c<0:
    print("F wins with",abs(c),"majority")
else:
    print("0")