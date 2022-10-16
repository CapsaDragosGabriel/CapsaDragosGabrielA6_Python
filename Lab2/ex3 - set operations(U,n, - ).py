def intersect(a, b):
    new_list = []
    for i in a:
        for j in b:
            if i == j:
                new_list.append(i)
    return new_list


def reunite(a, b):
    new_list = []
    for i in a:
        new_list.append(i)
    for i in b:
        if new_list.__contains__(i):
            continue
        else:
            new_list.append(i)
    return new_list


def difference(a, b):
    new_list = []
    for i in a:
        if b.__contains__(i):
            continue
        else:
            new_list.append(i)
    return new_list


def main():
    a = [1, 2, 3, 4, "dog"]
    b = ["cat", "dog", 2, "fish", 3.14]

    print(intersect(a, b))
    print(reunite(a, b))
    print(difference(a, b))
    print(difference(b, a))



main()
