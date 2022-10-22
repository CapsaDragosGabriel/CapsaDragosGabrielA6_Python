def loop(mapping):
    steps = []
    steps.append(mapping['start'])
    currStep = steps[0]
    nextStep=mapping[currStep]
    while not steps.__contains__(nextStep):
        steps.append(nextStep)
        currStep = nextStep
        nextStep = mapping[currStep]
    return steps


def main():
    dict = {"start": 'a',
            'b': 'a',
            'a': '6',
            '6': 'z',
            'x': '2',
            'z': '2',
            '2': '2',
            'y': 'start'}
    print(loop(dict))


main()
