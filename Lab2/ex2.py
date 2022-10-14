def checkPrime(num):
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num / 2) + 1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return 0
        else:
            return 1
    else:
        return 0


def checkList(listNumbers):
    listPrime = []
    for num in listNumbers:
        if checkPrime(num):
            listPrime.append(num)
    return listPrime


def main():
    listNumbers = [1, 2, 3, 4, 6, 7, 8, 9, 10]
    print(checkList(listNumbers))


main()
