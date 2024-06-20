from collections import defaultdict
class node:
    def __init__(self,u):
        self.data=u
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None
    def creat(self,root,x):
        if(root==None):
            return node(x)
        elif(root.data>x):
            root.left=self.creat(root.left,x)
        else:
            root.right=self.creat(root.right,x)
        return root
    def leftdisplay(self,root,c,l):
        if root==None:
            return
        if c not in l:
            l.append(c)
            print(root.data,end=" ")
        self.leftdisplay(root.left,c+1,l)
        self.leftdisplay(root.right,c+1,l)
    def rightdisplay(self,root,c,l):
        if root==None:
            return
        if c not in l:
            l.append(c)
            print(root.data,end=" ")
        self.rightdisplay(root.right,c+1,l)
        self.rightdisplay(root.left,c+1,l)
    def topdisplay(self,root,c,l):
        d= defaultdict(list)
        q=[(root,0)]
        while q:
            root,h=q.pop()
            d[h].append(root.data)
            if root.right:
                q.append((root.right,h+1))
            if root.left:
                q.append((root.left,h+1))
#         print(d,q)
        l=[]
        for i in d:
            l.append(d[i][0])
        print(l)
        
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
    def preorder(self,root):
        if root:
            print(root.data,end=" ")
            self.inorder(root.left)
            self.inorder(root.right)
    def postorder(self,root):
        if root:
            self.inorder(root.left)
            self.inorder(root.right)
            print(root.data,end=" ")
    def sumofroots(self,root):
        if root==None:
            return 0
        else:
            return root.data + self.sumofroots(root.left) + self.sumofroots(root.right)
    def sumofeven(self,root):
        if root==None:
            return 0
        if root.data%2==0:
            return root.data+self.sumofeven(root.left)+self.sumofeven(root.right)
        else:
            return self.sumofeven(root.left) + self.sumofeven(root.right)
    def sumofodd(self,root):
        if root==None:
            return 0
        if root.data%2!=0:
            return root.data+self.sumofodd(root.left)+self.sumofodd(root.right)
        else:
            return self.sumofodd(root.left) + self.sumofodd(root.right)
    def es_os(self,root):
        if root==None:
            return 0
        if root.data%2==0:
            return root.data+self.es_os(root.left)+self.es_os(root.right)
        else:
            return self.es_os(root.left)+self.es_os(root.right)-root.data
    def height(self,root):
        if root==None:
            return -1
        return max(self.height(root.left),self.height(root.right))+1
    def bal(self,root):
        return abs(self.height(root.left)-self.height(root.right))<=1
    def leaf(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        else:
            return self.leaf(root.left) + self.leaf(root.right)
    def sumleaf(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return root.data
        else:
            return self.sumleaf(root.left) + self.sumleaf(root.right)
    def depth(self,root,x):
        pass
        if root==None:
            return 0
        if root.data==x:
            return 0
        elif root.data>x:
            return 1+self.depth(root.left,x)
        else:
            return 1+self.depth(root.right,x)
    def search(self,root,x):
        if root==None:
            return "not found"
        if root.data==x:
            return "found"
        if root.data>x:
            return self.search(root.left,x)
        else:
            return self.search(root.right,x)
    
t1=tree()
t1.root=node(10)
t1.creat(t1.root,5)
t1.creat(t1.root,2)
t1.creat(t1.root,7)
t1.creat(t1.root,4)
t1.creat(t1.root,3)
# t1.creat(t1.root,9)
t1.creat(t1.root,15)
t1.creat(t1.root,11)
t1.creat(t1.root,20)
t1.creat(t1.root,12)
t1.creat(t1.root,13)
t1.creat(t1.root,14)
print("left view:",end="")
t1.leftdisplay(t1.root,0,l=[])
print()
print("right view:",end="")
t1.rightdisplay(t1.root,0,l=[])
print()
print("top view:",end="")
t1.topdisplay(t1.root,0,l=[])
# t1.creat(t1.root,22)
# print("inorder:",end="")
# t1.inorder(t1.root)
# print("\npreorder:",end="")
# t1.preorder(t1.root)
# print("\npostorder:",end="")
# t1.postorder(t1.root)
# print("\nsum of roots:",t1.sumofroots(t1.root))
# print("diff of left and right roots:",abs(t1.sumofroots(t1.root.left)-t1.sumofroots(t1.root.right)))
# print("sum of even roots:",t1.sumofeven(t1.root))
# print("sum of odd roots:",t1.sumofodd(t1.root))
# print("diff of even and odd roots:",abs(t1.es_os(t1.root)))
# print(x.data)
# print("height of tree:",t1.height(t1.root))
# if(t1.bal(t1.root)):
#     print("balanced")
# else:
#     print("not balanced")
# print(t1.leaf(t1.root))
# print(t1.sumleaf(t1.root))
# print(t1.depth(t1.root,9))
# print(t1.search(t1.root,5))