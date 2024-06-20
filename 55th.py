# ip:
# 7
# 1 school
# 1 world
# 1 word
# 1 scholar
# 2 word
# 2 wood
# 3 sch
l=set()
r=[]
x=int(input("no of iterations:"))
for i in range(x):
    n=int(input("1 insert,2 search,3 prefix search,4 delete:"))
    if n==1:
        s=input()
        l.add(s)
    elif n==2:
        s=input()
        if s in l:
#             print(True)
            r.append(True)
        else:
#             print(False)
            r.append(False)
    elif n==3:
        s=input()
        c=0
        flag=0
        for j in l:
            for k in range(len(s)):
                if j[k]==s[k]:
                    flag=1
                else:
                    flag=0
            if flag==1:
                c+=1
        r.append(c)
#                 print(True)
#                 break
#         else:
#             c=0
#             print(False)
    elif n==4:
        s=input()
        l.remove(s)
    l=set(l)
print("result:")
for ele in r:
    print(ele)
print("<--end-->")
            