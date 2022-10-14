def asciiDivizibil(strings, flag, x=1):
    list_chars = []
    if flag == True:
        for i in strings:
            chars = []
            for j in i:
                if ord(j) % x == 0:
                    chars.append(j)
            list_chars.append(chars)
    else:
        for i in strings:
            chars = []
            for j in i:
                if int(ord(j)) % x != 0:
                    chars.append(j)
            list_chars.append(chars)

    return list_chars


def main():
    strings = ["test", "hello", "lab002"]
    flag = False
    x = 2
    print(asciiDivizibil(strings, flag, x))


main()
