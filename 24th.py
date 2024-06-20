#doubly linked list
class node:
    def __init__(self,x):
        self.data=x
        self.nxt=None
        self.prev=None
class dll:
    count=0
    def __init__(self):
        self.head=None
        self.tail=None
    def addback(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            self.tail.nxt=t
            t.prev=self.tail
            self.tail=self.tail.nxt
    def addfront(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
            t=self.head
            self.head=node(x)
            self.head.nxt=t
            t.prev=self.head
    def display(self):
        self.count=0
        t=self.head
        while (t!= None):
            self.count+=1
            print(t.data, end="->")
            t=t.nxt
        print("None")
    def rev_display(self):
        self.count=0
        t=self.tail
        while (t!= None):
            self.count+=1
            print(t.data, end="<-")
            t=t.prev
        print("None")
    def search(self,x):
        i=self.head
        j=self.tail
        flag=0
        c=0
        while i!=j and i!=j.nxt:
            c+=1
            if i.data==x or j.data==x:
                flag=1
                break
            i=i.nxt
            j=j.prev
        if i.data==x:
            flag=1
        if flag==1:
            print("found -itteration count",c)
        else:
            print("not found -itteration count",c)
    def len_e_o(self):
#         if self.count%2==0:
#             print(self.count,"-even")
#         else:
#             print(self.count,"-odd")
        i=self.head
        j=self.tail
        while i!=j and i!=j.nxt:
            i=i.nxt
            j=j.prev
        if(i==j):
            print("odd")
        else:
            print("even")   
    def palindrome(self):
        i=self.head
        j=self.tail
        flag=0
        while i!=j and i!=j.nxt:
            if i.data!=j.data:
                flag=1
                break
            i=i.nxt
            j=j.prev
        if flag==1:
            print("not plaindrome")
        else:
            print("plaindrome")
    def change(self):
        i=self.head
        j=self.tail
        while i!=j and i!=j.nxt:
            i=i.nxt
            j=j.prev
        i=i.prev
        j=j.nxt
        i=self.head
        while j.nxt!=None:
            i.data,j.data=j.data,i.data
            i=i.nxt
            j=j.nxt
        i.data,j.data=j.data,i.data
    def dual_swap(self):
        i=self.head
        j=i.nxt
        while(j!=None):
            if i.prev==None:
                r=j.nxt
                r.prev=i
                j.nxt=r.prev
                j.prev=None
                i.prev=j
                self.head=j
                print("a")
                print(j.data,"-",j.nxt.data,i.data,"-",i.nxt.data)
                i=r
                j=r.nxt
            elif j.nxt==None:
                l.nxt=i.nxt
                i.nxt=None
                j.nxt=l.nxt
                j.prev=l
                i.prev=j
                self.tail=i
                print("b")
                print(i.data,"-",j.data,"-")
                j=None
            else:
                l=i.prev
                r=j.nxt
                l.nxt=i.nxt
                r.prev=j.prev
                j.nxt=r.prev
                i.prev=l.nxt
                print("c")
                print(j.data,"-",j.nxt.data,i.data,"-",i.nxt.data)
                i=r
                j=r.nxt
        print("----")
    def string_sym(self):
        t=self.head
        n=[]
        c=0
        while t!=None:
            c+=1
            if t.data in "({[":
                n.append(t.data)
            else:
                if n[-1]=="(" and t.data==")":
                    n.pop()
                elif n[-1]=="[" and t.data=="]":
                    n.pop()
                elif n[-1]=="{" and t.data=="}":
                    n.pop()
                else:
                    print(c)
                    break
            t=t.nxt
        if len(n)==0:
            print("-1")
            
    def eo_sum(self,t,e,o):
        if t==None:
            return abs(e-o)
        if t.data%2==0:
            e+=t.data
        else:
            o+=t.data
        return self.eo_sum(t.nxt,e,o)
    def prime(self,t,c):
        if t==None:
            return c
        def isprime(s,n):
            if(s>(n//2)+1):
                return 1
            if (n%s==0):
                return 0
            return isprime(s+1,n)
        if(isprime(2,t.data)):
            c+=1
        return self.prime(t.nxt,c)
            
d=dll()
d.addfront(56)
d.addback(65)
d.addback(34)
# d.addfront(1)
d.addback(21)
d.addback(23)
d.addback(14)
d.addback(17)
# d.addback(7)

d.display()
print(d.prime(d.head,0))
# d.rev_display()  
# d.search(5)
# # d.len_e_o()
# d.palindrome()
# d.change()
# d.display()
# d.change()
# d.display()
# d.dual_swap()
# d.display()
# d.string_sym()
# print(d.eo_sum(d.head,0,0))
