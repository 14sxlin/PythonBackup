import collections

if __name__ == '__main__':
    seq1 = ((123, 34, 56), "jig", (("fs", 123), 12312), 435)
    print(seq1[2][0][0])

    Sale = collections.namedtuple("Sale", "name price quantity")
    sales = [Sale("A", 10, 20), Sale("B", 20, 30)]

    total = 0
    for sale in sales:
        total += sale.price * sale.quantity
    print("total = {}".format(total))

    Aircraft = collections.namedtuple("Aircraft", "id model seating")
    Seating = collections.namedtuple("Seating", "min,max")
    aircraft = Aircraft("NO.002", "747", Seating(10, 100))
    print(aircraft.seating.max)
    print("model = {0.model}".format(aircraft))

    print("{id} {model} ".format(**aircraft._asdict()))
