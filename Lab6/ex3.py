import re


def mega_filtru(text, lista):
    comp = lambda x: re.compile(x)
    toReturn = []
    for regula in lista:
        comp(regula)
        res = re.findall(regula, text)
        # print(res)
        for cuvant in res:
            if cuvant not in toReturn:
                toReturn.append(cuvant)
    return toReturn


if __name__ == '__main__':
    lista = [r'\d+', r'[a-zA-Z]+']
    text = "test words 65464asd 646"
    print(mega_filtru(text, lista))
