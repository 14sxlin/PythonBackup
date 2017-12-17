if __name__ == '__main__':
    a = 10
    b = 20
    print(a + b)
    print(type(a))
    a = "20"
    print(type(a))

    my_tuple = (1, 3, "oijf", "sdnf")

    for i in my_tuple:
        print(i)

    print("len of my_tuple is ", len(my_tuple))

    my_list = [1, 2, 3, 4, 5, 6, 7]
    print(my_list)
    print(my_list[3])

    ch = 'a'
    a = int("99")
    print(ch.capitalize())
    print(a)

    print(1 <= a <= 100)
    if ch:
        print("true")
    ch = 0
    if ch:
        print("true")
    else:
        print("false")

    # num = input("give me a number ")
    # try:
    #     num = float(num)
    #     print("your num is ", num)
    # except ValueError as e:
    #     print(e)

    print("12/4 = ", 12/4)
