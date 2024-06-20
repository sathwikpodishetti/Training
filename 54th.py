# ip:
# 7
# 1 school
# 1 world
# 1 word
# 1 scholar
# 2 word
# 2 wood
# 3 sch
class node:
    def __init__(self,u):
        self.d={}
        self.flag=0

class tries:
    def __init__(self):
        self.root=node()
    def insert(self,s):
        t=self.root
        for i in s:
            if i not in t.d:
                t.d[i]=node()
            else:
                t=t.d[i]
    def search(self,s):
        t=self.root
t1=tries()
n=int(input())
for i in range(n):
    a,s=input().split()
    if a=="1":
        t1.insert(s)
    elif a=="2":
        t1.search(s)
    elif a=="3":
        print(t1.search_prefix(s))

print("--end--")
