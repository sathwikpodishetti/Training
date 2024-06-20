s="the 4quick br$%^own foENDx j45umps o\.ver the lazy dog"
# s="qwweer yuiop asdfvgh JKL mnbvlkjcxz"
b="abcdefghijklmnopqrstuvwxyz"
for i in s:
   if i.islower():
        b=b.replace(i,"")
if b=="":
    print(b)
    print("all there")
else:
    print(b)
    print("all not there")