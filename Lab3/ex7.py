def dictionarMultimi(*multimi):
    lista = list(multimi)
    dictionar = {}
    for i in range(0, len(lista)):
        for j in range(i+1, len(lista)):
            funct = lambda a, b, s: str(a) + s + str(b)
            # nameOfEntry=str(lista[i])+"&"+str(lista[j])
            getOperator = {
                '&': lambda x, y: x & y,
                '|': lambda x, y: x | y,
                '-': lambda x, y: x - y,
            }
            for k in {'&', '|', '-'}:
                nameOfEntry = funct(lista[i], lista[j], k)
                dictionar.update({nameOfEntry: getOperator[k](lista[i], lista[j])})
                if k.__eq__('-'):
                    nameOfEntry=funct(lista[j], lista[i], k)
                    dictionar.update({nameOfEntry: getOperator[k](lista[j], lista[i])})

                # dictionar.update({nameOfEntry: lista[i] & lista[j]})

    return dictionar


def main():
    a = {1, 2, 3}
    b = {1, 2, 4,5}
    c = {5, 6, 2}

    dictionar=dictionarMultimi(a, b, c)
    for key in dictionar:
        print(str(key)+":"+str(dictionar[key]))

main()
