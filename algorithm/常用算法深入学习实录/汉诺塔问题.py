def move(num, begin, support, target):
    if num == 1:
        print("{} -> {}".format(begin, target))
    else:
        move(num - 1, begin, target, support)
        print("{} -> {}".format(begin, target))
        input("Enter\n")
        move(num - 1, support, begin, target)


if __name__ == '__main__':
    num = int(input("pan nums:"))
    move(num, 'a', 'b', 'c')
