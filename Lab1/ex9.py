string="an Applesssss is not a tomato"
string=string.lower()
appearences={
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0,
    "b":0,
    "c":0,
    "d":0,
    "f":0,
    "g":0,
    "h":0,
    "j":0,
    "l":0,
    "m":0,
    "n":0,
    "p":0,
    "k":0,
    "q":0,
    "r":0,
    "s":0,
    "t":0,
    "v":0,
    "x":0,
    "y":0,
    "z":0,
    "w":0

}
vowels="abcdefhijklmnopqrstuvwxyz"
for i in string:
    if vowels.count(i):
        appearences[i]=appearences[i]+1

print(appearences)
maxi=0
maxVow=""
for vow in appearences:
    if appearences[vow]>maxi:
        maxVow=vow
        maxi=appearences[vow]
print(maxVow)
print(maxi)