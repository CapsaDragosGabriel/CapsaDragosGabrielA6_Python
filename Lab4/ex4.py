import os
import sys


def print_extensions(director):
    os.chdir(director)
    toRemove = []
    lista = os.listdir(".")
    for element in lista:
        i = 0
        try:
            while element[i] != ".":
                i += 1
        except:
            toRemove.append(element)
            continue
        else:
            lista[lista.index(element)] = element[i:]
    ret = list(set(lista) - set(toRemove))
    ret.sort()
    return ret


def main():
    # python3 ex4.py E:\AN3\Sem1\A3D\
    try:
        print(print_extensions(sys.argv[1]))
    except:
        print("Wrong input")


main()
