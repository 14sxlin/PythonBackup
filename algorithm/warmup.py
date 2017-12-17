#!/bin/python3

import sys

def timeConversion(s):
    hour,minute,second = s.split(':')
    hour = int(hour)
    afternoon = second[-2:] == "PM"
    if afternoon:
        if hour < 12:
            hour += 12
    elif hour >= 12:
            hour -= 12
    return "{0:02}:{1}:{2}".format(hour,minute,second[:-2])

if __name__ == '__main__':
    s = input().strip()
    result = timeConversion(s)
    print(result)
