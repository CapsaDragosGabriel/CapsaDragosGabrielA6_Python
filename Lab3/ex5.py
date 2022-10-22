def validate_dict(rules, tuples):
    ok = True
    for grup in rules:
        if tuples.__contains__(grup[0]):
            ok = checkExpression(tuples[grup[0]], grup[1], grup[2], grup[3])
            if ok == -1:
                ok=False
                return ok
            ok=True
    for tuplu in tuples:
        ok=False
        for grup in rules:
            if grup[0]==tuplu:
                ok=True
        if ok == False:
            return ok
    return ok


def checkExpression(a, prefix, middle, suffix):
    if prefix == "":
        ok = True
    else:
        ok = a.startswith(prefix)
    if suffix == "":
        ok = ok and True
    else:
        ok = ok and a.endswith(suffix)
    if middle == "":
        ok = ok and True
    else:
        if prefix != "":
            start = len(prefix)
        else:
            start = 0
        if suffix != "":
            end = len(a) - len(prefix)
            ok = ok and a.find(middle, start, end)
        else:
            ok = ok and a.find(middle, start)

    return ok


def main():
    s = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
    d = {"key1": "come inside, it's too cold out","key3": "this is not valid" }
    #print(checkExpression("come inside, it's too cold out", "", "inside", ""))
    # print(d.__contains__("key1"))
    print(validate_dict(s, d))


main()
