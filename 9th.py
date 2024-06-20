a=123456
b=0
while a!=0:
    b=a%10
    a=a//10
    if b in [2,3,5,7]:
        print(b)
