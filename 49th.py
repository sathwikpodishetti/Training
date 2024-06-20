#7262 sec ---> 2hr: 1min: 2sec
n=int(input())
x=n//3600
x1=n%3600
y=x1//60
y1=x1%60
print(x,'h:',y,'m:',y1,'s:')