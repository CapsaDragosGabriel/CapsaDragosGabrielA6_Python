def print_arguments2(function):
    # print("Arguments are: ",function.__name__)
    # print(function.__code__.co_varnames[0])
    def new_function(*args, **kwargs):
        print("Arguments are: ", args, kwargs)

    return new_function


def return5():
    return 5


def addArguments(function, *args, **kwargs):
    print("Arguments are: ", args, kwargs)  # spun care-s parametrii
    return function(*args, **kwargs)  # apelez functia cu parametrii respectivi


def print_arguments(function):
    return lambda *args, **kwargs: addArguments(function, *args, **kwargs)  # construiesc functia noua cu parametrii corespunzatori


def multiply_output(function):
    return lambda *args, **kwargs: function(*args, **kwargs) * 2


def augment_function(function, decorators):
    for decorator in decorators:
        function = decorator(function)
        # wrapping de genul multiplyoutput(print_arguments(functie,*args,**kwargs))

    return lambda *args, **argvs: function(*args, **argvs)


if __name__ == '__main__':
    def multiply_by_two(x):
        return x * 2


    def add_numbers(a, b):
        return a + b


    augmented_multiply_by_two = print_arguments(multiply_by_two)
    x = augmented_multiply_by_two(10)  # this will print: Arguments are: (10,), {} and will return 20.
    print(x)
    augmented_add_numbers = print_arguments(add_numbers)
    x = augmented_add_numbers(3, 4)  # this will print: Arguments are: (3, 4), {} and will return 7.
    print(x)


    def multiply_by_three(x):
        return x * 3


    augmented_multiply_by_three = multiply_output(multiply_by_three)

    x = augmented_multiply_by_three(10)  # this will return 2 * (10 * 3)
    print(x)


    def add_numbers(a, b):
        return a + b


    decorated_function = augment_function(add_numbers, [print_arguments, multiply_output])

    x = decorated_function(3, 4)  # this will print: Arguments are: (3, 4), {} and will return (2 * (3 + 4))
    print(x)
