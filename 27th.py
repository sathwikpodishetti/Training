#co prime or not
a=4
b=6
for i in range(2,(min(a,b)//2)+1):
    if a%i==0 and b%i==0:
        print("not co-prime")
        break
else:
    print("co-prime")
