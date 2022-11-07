import os


def callback(eroare):
    print("Am primit ValueError: " + str(eroare))


def cautare(target, to_search, functie):
    try:
        if os.path.isdir(target):
            os.chdir(target)
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
                    except Exception as e:
                        functie(e)
                for directory in directories:
                    full_fileName = os.path.join(root, directory)
                    full_fileName = full_fileName[1:]
                    listFound.append(cautare(target + full_fileName, to_search, callback))

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
    except Exception as e:
        functie(e)


def main():
    target = "E:\\AN3\\Sem1\\A3D\\Alarak\\test"
   # target = "E:\\AN3\\Sem1\\A3D\\New Text Document - Copy.tt"

    to_search = "a"
    print(cautare(target, to_search, callback))


main()
