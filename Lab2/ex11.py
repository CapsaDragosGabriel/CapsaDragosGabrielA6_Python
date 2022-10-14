def weirdSort(tuples):
    tuples.sort(key=getSortChar)

def getSortChar(list):
    return list[1][2]

def main():
    tuples=[
        ("abc","bcd"),
        ("abc","zza")
    ]
    weirdSort(tuples)
    print(tuples)

main()