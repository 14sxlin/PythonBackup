if __name__ == '__main__':

    print("Type num or anything else , ^D or ^Z to quit")

    total = 0
    count = 0

    while True:
        input_str = input()
        try:
            if input_str:
                try:
                    num = int(input_str)
                except ValueError as e:
                    print(e)
                    continue
                total += num
                count += 1
        except EOFError:
            break

    if count:
        print("total: ", total, "count :", count, "mean : ", total/count)
