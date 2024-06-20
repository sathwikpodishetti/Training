s="hello:5438,car:214,book:8799,apple:2187"
a=list(map(str,s.split(",")))
for i in a:
    b=[]
    b=list(map(str,i.split(":")))
    if str(len(b[0])) in b[-1]:
        print(b[0][len(b[0])-1],end="")
    else:
        j=(len(b[0])-1)
        while(j!=0):
            if str(j) in b[-1]:
                print(b[0][j-1],end="")
                break
            j=j-1
        else:
            print('x',end="")
