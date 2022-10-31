import os
import sys

def printExtensions(director):
    os.chdir(director)
    toRemove = []
    lista = os.listdir(".")
    for element in lista:
        i = 0
        try:
            while (element[i] != "."):
                i += 1
        except:
            toRemove.append(element)
            continue
        else:
            lista[lista.index(element)] = element[i:]
    ret = list(set(lista) - set(toRemove))
    return ret

def main():
    #python3 ex4.py E:\AN3\Sem1\A3D\Alarak
    try:
        print(printExtensions(sys.argv[1]))
    except:
        print("Wrong input")
main()