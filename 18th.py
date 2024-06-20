n=int(input(":"))
print(":")
l=[list(input()) for i in range(n)]
s=str(input(":"))
res="YES"
for i in range(len(s)):
    if s[i] not in l[i%n]:
        res="NO"
        break
    else:
        x=str(l[i%n])
        x=x.split()
        print(x)
        x.remove(s[i])
        l.insert(i%n,x)
print(res)
