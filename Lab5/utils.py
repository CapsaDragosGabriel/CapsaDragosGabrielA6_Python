def process_item(x):
    flag = False
    # prime numbers are greater than 1
    i = 1
    currNum = 0
    while not flag:
        num = x + i
        currNum = num
        if num > 1:
            # check for factors
            flag = True
            for f in range(2, num):
                # print(f)
                if (num % f) == 0:
                    flag = False
                    break
        i += 1
    return currNum


if __name__ == '__main__':
    number = int(input("Enter a number please\n"))
    print(process_item(number))
