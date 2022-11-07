def get_numbers(lista):
    numbers = []
    isNumber = lambda x: type(x) is int or type(x) is float

    for element in lista:
        if isNumber(element):
            numbers.append(element)
    return numbers


if __name__ == '__main__':
    print(get_numbers([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
