f=123963321

s=str(f)
r=s[::-1]

l= len(s)

ok=1
for i in range(l):
    if s[i]!=s[l-1-i]:
        ok=0

if ok==1:
    print("Este palindrom")
else:
    print("Nu este palindrom")
