def countChars(a):
    y={}
    for i in a:
        y.update(dict.fromkeys(i,a.count(i)))
    return y

def main():
    a="Ana has apples."
    print(countChars(a))

main()