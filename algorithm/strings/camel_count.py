#!/bin/python3

import sys


def is_capital(c):
    return ord('A') <= ord(c) <= ord('Z')


if __name__ == '__main__':
    s = input().strip()
    count = 1
    for ch in s:
        if is_capital(ch):
            count += 1
    print(count)
