def compareDict(a, b):
    ok = True
    for element in a:
        if not b.__contains__(element):
            ok = False
            print(str(element) + ":" + str(a[element]) + " doar in primul dictionar")
        if b.__contains__(element):
            if (b[element] != a[element]):
                print(str(element) + ":" + str(a[element]) + " " + str(b[element]))
                ok = False
    for element in b:
        if not a.__contains__(element):
            ok = False
            print(str(element) + ":" + str(b[element]) + " doar in al doilea dictionar")
    return ok


def main():
    roti = 7
    a = {
        "a": 1,
        "b": 3,
        "d": 2,
        "c": ["aolo", ['a', 'u', 'l'], "v", "e", "r", "e"],
        "masina": roti
    }
    b = {
        "a": 9,
        "d": 2,
        "c": ["aolo", ['a', 'u'], "v", "e", "r", "e"],
        "x": ["valelei", "v", "e", "r", "e"],
        "masina": roti,
    }
    print(compareDict(a, b))


main()
