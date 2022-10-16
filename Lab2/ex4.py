# compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"]

def compose(notes, moves, start):
    song = []
    k = start
    song.append(notes[k])
    for i in moves:
        k += i
        song.append(notes[(k) % len(notes)])
    return song


def main():
    notes = ["do", "re", "mi", "fa", "sol"]
    moves = [1, -3, 4, 2]
    start = 2
    print(compose(notes, moves, start))

main()