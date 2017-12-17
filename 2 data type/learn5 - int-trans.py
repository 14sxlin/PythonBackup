import sys

if __name__ == '__main__':
    x = 10
    print("hex(10) = ", type(hex(x)))
    print("bin(10) = ", bin(x))
    print("oct(10) = ", oct(x))
    print(int("1110001", base=2))

    x = 2 << 3
    print("s<<3 = s * (2 ** 3) = ", x)
    x = 8 >> 3
    print("s>>3 = s // (2 ** 3) = ", x)

    x = int()
    y = float()

    print(x, y)

    def equal_float(a, b):
        return abs(a - b) <= sys.float_info.epsilon  # don't know why cannot use

    x = 1.111
    y = 1.111111
    print(equal_float(x, y))

    x_hex = x.hex()
    print("hex(", x,")=", x_hex)

    num = float.fromhex(x_hex)
    print("float.fromhex(", x_hex, ") =", num)

