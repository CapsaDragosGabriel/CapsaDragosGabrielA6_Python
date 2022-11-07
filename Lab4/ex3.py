import os


def functie(my_path):
    if os.path.isdir(my_path):
        countExtensions = {}
        os.chdir(my_path)
        for (root, directories, files) in os.walk("."):
            for fileName in files:
                full_fileName = os.path.join(root, fileName)
                if countExtensions.__contains__(os.path.splitext(full_fileName)[1]):
                    countExtensions[os.path.splitext(full_fileName)[1]] += 1
                else:
                    countExtensions[os.path.splitext(full_fileName)[1]] = 1
                # countExtensions[os.path.splitext(full_fileName)[1]] = countExtensions[
                #                                                         os.path.splitext(full_fileName)[1]] + 1
        toReturn=[]
        for key in countExtensions:
            tuplu=(key,countExtensions[key])
            toReturn.append(tuplu)
        toReturn.sort(key=lambda x:x[1],reverse=True)
        return toReturn
    else:
        file = open(my_path, 'r')
        x = [line for line in file]
        string = ""
        for element in x:
            string += element
        file.close()
        return string[-20:]


def main():
    #my_path = "Alarak"
    my_path = "AbsolutCool.txt"
    os.chdir("E:\AN3\Sem1\A3D")
    print(functie(my_path))


main()
