import sys

if __name__ == '__main__':
    num = input().strip()
    for i in range(1, int(num)+1):
        s = input().strip()
        a, b, c = s.split(' ')
        if int(a) + int(b) > int(c):
            print("Case #{}: true".format(i))
        else:
            print("Case #{}: false".format(i))
