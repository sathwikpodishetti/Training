n=[4,9,8,2,14,3,5,6]
def swap(a,b,c):
    if b>c:
        b,c=c,b
    if a>b:
        a,b=b,a
    return a,b,c

for i in range(len(n)-2):
    n[i],n[i+1],n[i+2]=swap(n[i],n[i+1],n[i+2])
#     print(n[i],n[i+1],n[i+2],end="  ")
print(n)