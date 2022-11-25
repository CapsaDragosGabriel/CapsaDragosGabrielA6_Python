import re


def get_words(text):
    reg = re.compile("\w+")
    res = re.findall(reg, text)
    print(res)


if __name__ == '__main__':
    text = "haide sa vedem care sunt cuvintele extrase de aici"
    get_words(text)
