s="(([{}}))"
n=[]
for i in s:
    if i in "({[":
        n.append(i)
    else:
        if n[-1]=="(" and i==")":
            n.pop()
        elif n[-1]=="[" and i=="]":
            n.pop()
        elif n[-1]=="{" and i=="}":
            n.pop()
        else:
            print(s.index(i)+1)
            break
             
if len(n)==0:
    print("-1")