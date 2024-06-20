# leetcode 79
n=4
g=[["t","u","e","d"],
   ["f","b","o","w"],
   ["r","o","o","r"],
   ["d","r","k","i"]]
s="book"
def fun(i,j,k):
    if g[i][j]!=k
        
        fun(i-1,j)
        fun(i,j-1)
        fun(i+1,j)
        fun(i,j+1)
for i range(n):
    for j in range(n):
        if g[i][j]==s[0]:
            fun(i,j,s[0])
fun(i,j)