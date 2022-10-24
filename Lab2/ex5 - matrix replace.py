import copy
def changeMatrix(a):
    rows = len(a)
    copyMatrix=copy.deepcopy(a)

    for i in range(0, rows):
        for j in range(0, i):
                copyMatrix[i][j] = 0
    return copyMatrix


testMatrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
print(testMatrix)
print(changeMatrix(testMatrix))
print(testMatrix)