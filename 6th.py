a=[5, 3.8, 7 ,5.6, 4, 2, 3]
es=os=fs=0
for i in a:
    if i%2==0:
        es+=i
    else:
        if i-int(i)!=0:
            fs+=i
        else:
            os+=i
print(es,os,fs)