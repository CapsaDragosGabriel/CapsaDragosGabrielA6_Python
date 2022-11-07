def getVowels(text):
    list_vows = []
    vowels = "aeiouAEIOU"

    for letter in text:
        if vowels.__contains__(letter):
            list_vows.append(letter)
    return list_vows


def filtru(litera):
    vowels = "aeiouAEIOU"
    return litera in vowels


if __name__ == '__main__':
    text = "Programming in Python is fun"
    # prima metoda
    print(getVowels(text))

    # a doua metoda
    vowels = "aeiouAEIOU"
    isVowel = lambda arg: arg in vowels
    vowel_filter = lambda text: [x for x in text if isVowel(x)]
    print(vowel_filter(text))

    # a treia metoda
    print(list(filter(filtru, text)))
