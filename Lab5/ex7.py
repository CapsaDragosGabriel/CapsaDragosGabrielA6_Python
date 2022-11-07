def get_fibo(nterms):
    fibo_list = []
    n1, n2 = 0, 1
    count = 0
    if nterms == 1:
        fibo_list.append(n1)
    else:
        while count < nterms:
            fibo_list.append(n1)
            nth = n1 + n2

            n1 = n2
            n2 = nth
            count += 1
    return fibo_list


def process(**kwargs):
    fibo_list = get_fibo(1000)
    #print(type(fibo_list))
    limit = ""
    offset = ""
    for x in kwargs:
        if x == "filters":
            for filtru in kwargs[x]:
                # print(filtru)
                fibo_list = list(filter(filtru, fibo_list))
        if x == "limit":
            limit = kwargs[x]
        if x == "offset":
            offset = kwargs[x]
    to_return = []
    for x in range(offset, limit + offset):
        try:
            to_return.append(fibo_list[x])
        except:
            pass
    return to_return


if __name__ == '__main__':
    def sum_digits(x):
        return sum(map(int, str(x)))


    lista_finala = process(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
                           limit=2,
                           offset=2
                           )
    print(lista_finala)
