import os


def printFolders(director, fisier):
    os.chdir(director)
    file = open(fisier, mode='w')
    lista=os.listdir(".")

    for element in lista:
        if os.path.isdir(element):
            if element[0]=='A':
                file.write(element)
                file.write("\n")


def main():
    director = "E:\AN3\Sem1\A3D"
    fisier = "New Text Document.txt"
    printFolders(director, fisier)


main()
