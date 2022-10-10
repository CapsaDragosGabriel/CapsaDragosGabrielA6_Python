l="UpperCamelCase"
l=l.replace(l[0],l[0].lower(),1)

for i in range(1,len(l)):
    if l[i].isupper():
        s="_"+l[i].lower()
        l=l.replace(l[i],s)
print(l)