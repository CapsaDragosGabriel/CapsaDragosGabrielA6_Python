def checkPalindrome(f):
    s = str(f)

    l = len(s)

    ok = 1
    for i in range(l):
        if s[i] != s[l - 1 - i]:
            ok = 0

    if ok == 1:
        return 1
    return 0


def biggestPalindrome(list):
    big = 0
    count = 0
    for i in list:
        if checkPalindrome(i):
            count += 1
            if i > big:
                big = i

    return [count, big]


def main():
    list=[
        123,
        121,
        1331,
        121
    ]
    print(biggestPalindrome(list))

main()