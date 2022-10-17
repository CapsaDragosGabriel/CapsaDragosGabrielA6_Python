def weirdSort(tuples):
    tuples.sort(key=getSortChar)


def getSortChar(list):
    return list[1][2]


def getSortSol2(pereche):
    return pereche[1][2]


def sol2(lists):
    z = list(*zip(*lists))
    print(z)


def main():
    tuples = [
        ("abc", "bcd"),
        ("abc", "zza"),
        ("abc","aaa")
    ]
    weirdSort(tuples)
    print(tuples)


main()
