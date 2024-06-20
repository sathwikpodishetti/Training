a="placements"
for i in a:
    if i in "aeiou":
        i=i.upper()
    elif i>='A' and i<='Z':
        if i not in "AEIOU":
            i=i.lower()
print(a)
            