import decimal

if __name__ == '__main__':
    com1 = 1 + 5j
    com2 = 2 - 4j
    print(com1 + com2)
    print(com1, "real = ", com1.real, "imag = ", com1.imag)

    num1 = decimal.Decimal("12313.25")
    num2 = decimal.Decimal(123123)
    # num3 = decimal.Decimal(123123.32) # should not use this
    print(num1, type(num1))
    print(num2, type(num2))
    # print(num3, type(num3))
