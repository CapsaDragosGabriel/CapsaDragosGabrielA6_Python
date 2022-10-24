def groupRhymes(words):
    rhymes = []
    for i in words:
        if i == '':
            continue
        else:
            tempList = []
            tempList.append(i)
            rhyme = i[-2:]
            for k in words:
                if k[-2:] == rhyme and not tempList.__contains__(k):
                    tempList.append(k)
            #     words.remove(k)
            for x in tempList:
                words[words.index(x)] = ''
            rhymes.append(tempList)
    return rhymes


def main():
    words = ['carte', 'ana', 'banana', 'arme', 'parte', 'carme', 'cana']
    words = list(filter(lambda x: len(x) > 3, words))
    print(groupRhymes(words))


main()
