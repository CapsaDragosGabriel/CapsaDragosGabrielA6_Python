def my_function(*args, **kwargs):
    list_dictionaries = []
    for element in args:
        if type(element) is dict:
            count_keys = len(element)
            for key in element:
                if type(key) is str:
                    if len(key) >= 3 and count_keys >= 2:
                        list_dictionaries.append(element)
                        break

    for x in kwargs:
        element = kwargs[x]
        if type(element) is dict:
            count_keys = len(element)
            for key in element:
                if type(key) is str:
                    if len(key) >= 3 and count_keys >= 2:
                        list_dictionaries.append(element)
                        break
    return list_dictionaries


if __name__ == '__main__':
    lista = my_function(
        {1: 2, 3: 4, 5: 6},

        {'a': 5, 'b': 7, 'c': 'e'},

        {2: 3},

        [1, 2, 3],

        {'abc': 4, 'def': 5},

        3764,

        dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},

        test={1: 1, 'test': True}
    )
    print(lista)
