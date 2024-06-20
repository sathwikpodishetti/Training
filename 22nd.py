n=4
k=1

for i in range(n):
    for j in range(n-i):
        if k<=n:
            print("_",end="")
            k+=1
    print(" ",end="")
    a=97
    if i==0:
        print(chr(a),end=" ")
    else:
        for l in range(i+1):
            a+=l
            print(chr(a),end="")
        a-=1
        for l in range(i+1):
            a-=l
            print(chr(a),end="")
    for m in range(n-i):
        if k>=1:
            print("_",end="")
            k-=1
    print("")