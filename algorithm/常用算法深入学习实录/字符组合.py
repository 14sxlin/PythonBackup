string = "abcdefg"
takeOrNot = [0 for _ in range(len(string))]


def take1(chars, n):
    """从M个不同的字符中取N个字符的所有组合"""
    if n > len(chars):
        return
    if n == len(chars):
        print(chars)

    def go(i):
        """决定第i个字母拿不拿"""
        print(takeOrNot)
        if i == len(chars):
            if takeOrNot.count(1) == n:
                for index, v in enumerate(takeOrNot):
                    if v:
                        print(chars[index], end="")
                print()
                print(takeOrNot)
        else:
            # 针对值的for
            takeOrNot[i] = 1
            go(i + 1)  # 拿
            # 这里赋值为0 不能少,少的话,会受takeOrNot的脏数据影响
            # 其他过程也用了这个takeOrNot的 List,不加的话,全是1
            # 而且放在这后面会更好,放在开头会有很多 全0的 没有必要的遍历
            takeOrNot[i] = 0
            go(i + 1)  # 不拿

    go(0)


def take2(chars, n):
    """从M个不同的字符中取N个字符的所有组合"""
    def go(source, result, n):
        if n == 1:          # 取了 n - 1 个, 和剩下的所有字符分别组合
            for c in source:
                print("{}{}".format(result,c))
        else:
            for i,c in enumerate(source):
                result += c                 # 第i个位置的字符，依次选择所有的字符
                go(source[i+1:],result,n-1) # 在剩下的字符里面选择 n-1个
                result = result[:-1]        # 恢复result，去掉前面添加的字符
    go(chars,"", n)


if __name__ == '__main__':
    take1(string, 5)
    # take2(string, 5)

