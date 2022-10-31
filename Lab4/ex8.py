import os


def printFolders(director, fisier):
    os.chdir(director)
    lista=os.listdir(".")
    toReturn=[]
    for element in lista:
        if not os.path.isdir(element):
            toReturn.append(os.path.abspath(element))
    return toReturn


def main():
    director = "E:\AN3\Sem1\A3D\Alarak\\test"
    fisier = "New Text Document.txt"
    print(printFolders(director, fisier))


main()
