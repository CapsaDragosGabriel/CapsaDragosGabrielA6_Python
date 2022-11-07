import os


def printFolders(director, fisier):
    os.chdir(director)
    file = open(fisier, mode='w')
    lista=os.listdir(".")

    for element in lista:
        if os.path.isfile(element):
            if element[0]=='A':
                file.write(os.path.abspath(element))
                file.write("\n")
    file.close()

def main():
    director = "E:\AN3\Sem1\A3D"
    fisier = "New Text Document.txt"
    printFolders(director, fisier)


main()
