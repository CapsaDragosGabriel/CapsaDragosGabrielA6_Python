def getFromList(lists):
    normalizeLists(lists)
    newlists = []
    for l in range(0,len(lists[0])):
        templist = []
        for k in range(0, len(lists)):
            templist.append(lists[k][l])

        newlists.append(tuple(templist))
    return newlists

def normalizeLists(lists):
    maxLen=0
    for k in range(0,len(lists)):
        if len(lists[k]) > maxLen:
            maxLen=len(lists[k])

    for k in range(0,len(lists)):
        for j in range(0,maxLen):
            if j<len(lists[k]):
                continue
            else:
                lists[k].append(None)

def sol2(lists):
    z=list(zip(*lists))
    print(z)
    return z
def main():
    lists = [
        [1, 2, 3,4],
        [5, 6, 7],
        ["a", "b", "c","d"]
    ]
    normalizeLists(lists)
    sol2(lists)
   # print(lists)
   # print(sol2(lists))


main()
