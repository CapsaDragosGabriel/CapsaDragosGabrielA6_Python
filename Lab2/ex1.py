def fibo(n):
    nums = []
    # print("Fibonacci sequence:")
    n1, n2 = 0, 1
    count = 0
    while count < n:
        nums.append(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
    return nums


def main():
    howMany = int(input("How many fibonacci numbers do you want to see:\n"))
    print(fibo(howMany))


main()
