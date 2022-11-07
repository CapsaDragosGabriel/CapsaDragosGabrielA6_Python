def f9(pairs):
    list_dictionaries = []
    for pair in pairs:
        tempDict = {}
        tempDict["sum"] = pair[0] + pair[1]
        tempDict["prod"] = pair[0] * pair[1]
        tempDict["pow"] = pair[0] ** pair[1]
        list_dictionaries.append(tempDict)
    return list_dictionaries


if __name__ == '__main__':
    print(f9(pairs=[(5, 2), (19, 1), (30, 6), (2, 2)]))
