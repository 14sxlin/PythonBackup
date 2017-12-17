import sys, math, decimal

if __name__ == '__main__':
    print("a = {0} b = {1}".format(1, 2))
    print("{who} should do {something}"
          .format(who="Jim", something="washing"))
    print("{who} is {0}".format(12314, who="sdfasdf"))

    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    print("first num is {0[1]} second {0[2]}".format(nums))

    key_values = {"a": 123, "b": 456}
    print("a = {0[a]} b = {0[b]}".format(key_values))

    print("a = {0.pi} b = {1.maxunicode}".format(math, sys))

    print("a = {} b = {} c = {}".format(11, 22, 33))

    a = 10
    b = 20
    print("a={a} b= {b}".format(**locals()))

    print("一般形式 :{0}\n"
          "强制使用字符串形式 {0!s}\n"
          "强制使用表象形式  {0!r}\n"
          "强制使用表象形式, 仅限ascii {0!a}".format(decimal.Decimal("12312.31")))

    print(" {0} {0!a}".format("asdfsndf你是"))  # asdfsndf\u4f60\u662f

    text = "the sword of truth"
    print("'{0}'".format(text))
    print("'{0:25}'".format(text))  # minimum width 25
    print("'{0:>25}'".format(text))  # minimum width 25 right align
    print("'{0:^25}'".format(text))  # minimum width 25 center align
    print("'{0:-^25}'".format(text))  # minimum width 25 center align,fill using -
    print("'{0:-^.5}'".format(text))  # maximum width 25 center align,fill using -

    maxwidth = 5
    print("'{0}'".format(text[:maxwidth]))
    print("'{0:.{1}}'".format(text,maxwidth))

    print("'{0:b} {0:o} {0:x} {0:X} {0:c} {0:n}'".format(250))