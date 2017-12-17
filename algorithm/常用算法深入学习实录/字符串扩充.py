def replace(chars, old=' ', new="%20"):
    """替换字符串中的字符"""
    if type(chars) is not list:
        print("chars should be list", type(chars))
        return ""
    expand_size = len(new) - len(old)
    count = 0
    j = len(chars) - 1  # 扫描指针
    # 首先扩充字符数组
    for i in range(len(chars)):
        if chars[i] == old:
            count += 1
            for _ in range(expand_size):
                chars.append('~')
    i = len(chars) - 1  # 守卫指针

    while j >= 0:
        if chars[j] != old:  # 不该替换
            chars[i] = chars[j]  # 纳入范围
            i -= 1
            j -= 1
        else:  # 替换
            for c in reversed(new):  # 替换  纳入范围
                chars[i] = c
                i -= 1
            j -= 1
    return "".join(chars)


if __name__ == '__main__':
    chars = list("a*bc*def*g")
    print("".join(chars), "->", end=" ")
    print(replace(chars,old='*'))
