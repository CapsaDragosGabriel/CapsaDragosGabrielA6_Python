def pair_numbers(lista):
    even_list = []
    odd_list = []
    isEven = lambda x: x % 2 == 0
    for element in lista:
        if isEven(element):
            even_list.append(element)
        else:
            odd_list.append(element)
    print(even_list)
    print(odd_list)
    return list(zip(even_list, odd_list))


if __name__ == '__main__':
    print(pair_numbers([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))
