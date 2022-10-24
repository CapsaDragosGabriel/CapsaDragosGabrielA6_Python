def getElements(multime):
    all = set(multime)
    uniques = set()
    toremove = set()
    for element in multime:
        if uniques.__contains__(element):
            toremove.add(element)
        if not uniques.__contains__(element):
            uniques.add(element)
    uniques = uniques.difference(toremove)
    countUnique = len(uniques)
    all = all.difference(uniques)
    countDupl = len(all)
    return tuple([countUnique, countDupl])


def getElements2(multime):
    all = set(multime)
    uniques = set({})
    toremove = set({})
    for element in multime:
        if uniques.__contains__(element):
            toremove.add(element)
        if not uniques.__contains__(element):
            uniques.add(element)
    uniques = uniques.difference(toremove)
    countUnique = len(uniques)
    all = all.difference(uniques)
    countDupl = len(all)
    return tuple([countUnique, countDupl])

def main():
    a = ['a', 'a', 'b', 3, 'c', "cartof", "cartof", "cartofel"]
    print(getElements(a))


main()
