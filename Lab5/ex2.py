def Sum(*args, **kwargs):
    suma = 0
    for element in args:
        suma += element
    for element in kwargs:
        suma += kwargs[element]
    return suma


if __name__ == '__main__':
    print(Sum(1, 2, 3, 4, 5, a=5))
    functie = lambda *args, **kwargs: sum(args) + sum(kwargs.values())
    print(functie(1, 2, 3, 4, 5, a=5))
