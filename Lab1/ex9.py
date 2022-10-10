string="an Apple is not a tomato"
string=string.lower()
appearences={
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
}
vowels="aeiou"
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