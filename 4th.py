a="SathWik@123"
lv=uv=lc=uc=d=s=0
for i in range(len(a)):
    if a[i]>='a' and a[i]<='z':
        if a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u':
            lv+=1
        else:
            lc+=1
    elif a[i]>='A' and a[i]<='Z':
        if a[i]=='A' or a[i]=='E' or a[i]=='I' or a[i]=='O' or a[i]=='U':
            uv+=1
        else:
            uc+=1
    elif a[i]>='0' and a[i]<='9':
        d+=1
    else:
        s+=1
print("lv-",lv,"\nuv-",uv,"\nlc-",lc,"\nuc-",uc,"\nd-",d,"\ns-",s)