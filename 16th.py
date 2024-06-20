s="bvec"
key=30
alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
new=[]
for i in s:
    x=alpha.index(i)
    key=(key%26)
    new.append(alpha[x-key])
print("".join(new))
