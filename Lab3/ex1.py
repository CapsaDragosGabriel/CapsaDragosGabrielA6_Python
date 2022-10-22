def lists(a, b):
    longList = []
    longList.append(a | b)
    longList.append(a & b)
    longList.append(a - b)
    longList.append(b - a)
    return longList


def main():
    x = {1, 2, 3}
    y = {1, 5, "A"}
    print(lists(x, y))


main()
