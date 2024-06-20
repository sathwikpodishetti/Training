#single linked list
class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def __init__(self):
        self.head=None
    def display(self):
        c=0
        t=self.head
        while (t!= None):
            c+=1
            print(t.data, end="->")
            t=t.nxt
        print("None")
#         self.count(c)
        return c
    def addback(self,x):
        if self.head==None:
            self.head=node(x)
        else:
            t=self.head
            while(t.nxt!=None):
                t=t.nxt
            t.nxt=node(x)
    def addeven(self):
        t=self.head
        s=0
        while(t!=None):
            if(t.data%2==0):
                s=s+t.data
    def addfront(self,x):
        if self.head==None:
            self.head=node(x)
        else:
            t=node(x)
            t.next=self.head
            self.head=t
    def search(self,x):
        t=self.head
        while(t.nxt!=None):
            if t.data==x:
                print("ele found")
                break
            t=t.nxt
        else:
            print("ele not found")
    def mid_ele(self):
        f=self.head
        s=self.head
        while(f!=None and f.nxt!=None):
            s=s.nxt
            f=f.nxt.nxt
        print("mid_ele:",s.data)
    def count(self):
        c=0
        t=self.head
        while (t!= None):
            c+=1
            t=t.nxt
        if c%2==0:
            print (c,"-even")
        else:
            print (c,"-odd")
    def long_sub(self):
        t=self.head
        c=1
        m=0
        while(t.nxt!=None):
            if(((t.data)+1)==(t.nxt.data)):
                c+=1
                if c>m:
                    m=c
            else:
                c=1
            t=t.nxt
            
        print("max seq:",m)
    def pairs(self):
        t=self.head
        print("all pairs:")
        while(t.nxt!=None):
            v=t.nxt
            while(v!=None):
                print(t.data,v.data)
                v=v.nxt
            t=t.nxt
    def bubble_sort(self):
        t=self.head
        c=0
        while(t.nxt!=None):
            f=0
            v=t.nxt
            while(v!=None):
                c+=1
                if(t.data>=v.data):
                    t.data,v.data=v.data,t.data
                    f=1
                v=v.nxt
                if(f==0):
                    break
            t=t.nxt
        self.display()
        print(c)
#     def poniter():
#         t=self.head
#         a=t.nxt
#         b=a.nxt
#         c=b.nxt
#     def mode(self):
         

l1=sll()
l1.head = node(3)
l1.addback(8)
l1.addback(6)
l1.addback(10)
l1.addback(9)
# l1.addback(18)
# l1.addback(17)
l1.display()
l1.bubble_sort()
# l1.count()
# l1.search(30)
# l1.mid_ele()
# l1.long_sub()
# l1.pairs()
