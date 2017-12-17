if __name__ == '__main__':
    p = 1
    i = iter([1, 2, 3, 4, 5, 6])
    while True:
        try:
            p *= next(i)
        except StopIteration:
            break
    print("product = {}".format(p))

    for i in range(10):
        print(i)

    info = [1,2,3,4,6]
    # light copy
    cp = info
    cp[0] = 9
    print(cp, info)
    # deep copy
    dcp = info[:]
    dcp[0] = 6
    print(dcp,info)

    # set adn dirt use copy method to get deep copy
    s = set("apple")
    sc = s.copy()
    sc.pop()
    print(sc,s)

    s = {"a":12,"b":13}
    sc = s.copy()
    sc.pop("a")
    print(s,sc)