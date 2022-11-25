import re


def custom_reg(regex, text, x):
    reg = re.compile(regex)
    res = re.findall(reg, text)
    toReturn = []
    for word in res:
        if len(word) == x:
            toReturn.append(word)
    return toReturn


if __name__ == '__main__':
    regex = "[a-zA-Z0-9]+"
    text = "haide sa vedem care sunt cuvintele extrase de aici"
    x = 4
    print(custom_reg(regex, text, x))
