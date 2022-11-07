import os


def cautare(target, to_search):
    if os.path.isdir(target):
        os.chdir(target)
        root = target
        listFound = []

        for (root, directories, files) in os.walk("."):
            for fileName in files:
                full_fileName = os.path.join(root, fileName)
                full_fileName = full_fileName[1:]
                try:
                    x = [line for line in open(target + full_fileName)]
                    # print(x)
                    ok = False
                    for element in x:
                        if element.__contains__(to_search) and not ok:
                            ok = True
                    if ok:
                        listFound.append(target + full_fileName)
                except :
                    pass
            for directory in directories:
                full_fileName = os.path.join(root, directory)
                full_fileName = full_fileName[1:]
                print(target + full_fileName)
                listFound.append(cautare(target + full_fileName, to_search))

            return listFound

    elif os.path.isfile(target):

        x = [line for line in open(target)]
        print(x)
        ok = False
        for element in x:
            if element.__contains__(to_search) and not ok:
                ok = True

        return ok
    else:
        raise ValueError


def main():
    target = "E:\\AN3\\Sem1\\A3D\\Alarak\\test"
    #target = "E:\\AN3\\Sem1\\A3D\\New Text Document - Copy.txt"

    to_search = "a"
    print(cautare(target, to_search))


main()
