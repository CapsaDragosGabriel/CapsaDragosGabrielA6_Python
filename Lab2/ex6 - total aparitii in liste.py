def occurences(lists, x):
    occur = []
    newList = lists[0]
    for i in range(1, len(lists)):
        for j in lists[i]:
            newList.append(j)
    print(newList)

    for i in newList:
        if newList.count(i) == x and not occur.__contains__(i):
            occur.append(i)

    return occur


def main():
    lists = [
        [1, 2, 3],
        [2, 3, 4],
        [4, 5, 6,"test"],
        [4, 1, "test"]
    ]
    print(occurences(lists, 2))


main()
