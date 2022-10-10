string="aeiouAEIOU"
f=input("Give me a string and i ll tell you no. of vowels\n")
vowCount=0
for i in string:
    vowCount=vowCount+ f.count(i)

print("There are "+str(vowCount)+" vowels.\n")