def get_sum(n):
    asum=0
    while(n!=0):
        asum+=n%10
        n=n//10
    return asum
def is_prime(asum):
    i=2
    result=True
    while i<(asum//2):
        if asum%i==0:
            result=False
            break
        else:
            i+=1
    return result
def main(x):
    a=x
    while(x//10!=0):
        x=get_sum(x)
#         print(x)
    y=is_prime(x)
    if(y==False):
        print("sum of",a,"is",x,"i.e not prime")
        a+=1
        main(a)
    else:
        print("sum of",a,"is",x,"i.e prime")
    return
n=int(input("Enter a num:"))
x=n
main(x)