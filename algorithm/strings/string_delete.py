#!/bin/python3
# 字符串消消乐
# https://www.hackerrank.com/challenges/reduced-string/problem

import sys

def delete_duplicate(s):
    result = s
    char_set = set([c+c for c in s])
    initLen = -1
    while initLen!=0 and len(result) != initLen:
        initLen = len(result)
        for cc in char_set:
            result = result.replace(cc, "")
    if len(result) != 0:
        return result
    else:
        return "Empty String"

if __name__ == '__main__':
    s = input().strip()
    result = delete_duplicate(s)
    print(result)
