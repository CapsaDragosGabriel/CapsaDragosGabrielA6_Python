string="An apple is USD56"
numbers="0123456789"
firstNum=""
l=len(string)
print(l)
for i in range(0,len(string)-1):
    if string[i].isdigit() and firstNum=="":
        while string[i].isdigit() and i<l:
            firstNum=firstNum+string[i]
            if i+1<l:
                i=i+1
            else:
                break

print(firstNum)