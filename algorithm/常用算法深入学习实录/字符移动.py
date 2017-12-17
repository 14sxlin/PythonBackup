s = "ab**cd*ef**ghij*k*lmn**"


def move_star(chars,target='*'):
    """
    将 * 往前移动, 字母往后移动, 保持顺序
    :param chars:
    :param target:
    :return:
    """
    i = len(chars)-1   # 指向* 防卫指针: 指向的位置后面都是合法的
    j = i               # 指向字母 扫描指针: 每次都移动,如果是符合字符,纳入防卫指针
    while j >= 0:
        if chars[i] != '*':     # 找到第一个 *
            i -= 1
        else:
            # 如果 j 指向一个字母, 则交换
            if chars[j] != '*':
                chars[i] = chars[j]
                chars[j] = '*'
                i -= 1
        j -= 1                      # 指向字母的指针往前移动
    return "".join(chars)


if __name__ == '__main__':
    print(move_star(list(s)))