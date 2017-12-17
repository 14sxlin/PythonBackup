def judge(string, head, tail):
    if head >= tail:
        return True
    if string[head] == string[tail]:
        return judge(string, head + 1, tail - 1)
    else:
        return False


if __name__ == '__main__':
    string = input("input your string: ")
    if judge(string, 0, len(string)-1):
        print("{} 是回文".format(string))
    else:
        print("{} 不是回文".format(string))
