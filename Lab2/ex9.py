def getSeats(heights):
    cantsee = []
    for i in range(0, len(heights)):
        for j in range(0, len(heights[0])):
            curr_height = heights[i][j]
            for k in range(0, i):
                if heights[k][j] >= curr_height:
                    cantsee.append((i, j))
                    break
    return cantsee


def main():
    heights = [
        [1, 2, 3, 2, 1, 1],

        [2, 4, 4, 3, 7, 2],

        [5, 5, 2, 5, 6, 4],

        [6, 6, 7, 6, 7, 5]
    ]
    print(getSeats(heights))


main()
