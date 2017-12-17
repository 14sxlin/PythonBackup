import my_class.Shape as Shape

if __name__ == '__main__':
    p = Shape.Point(10, 20)
    print(p)
    print(str(p))
    print(repr(p))
    print(p.distance_from_origin())

    p1 = Shape.Point(10, 20)
    print(p1 == p)
    print(p1 != p)

    print(isinstance(p, Shape.Point))

    print(p.__module__ + "." + repr(p))

    import my_class

    q = eval(p.__module__ + "." + repr(p))
    print(q)
    print(repr(q))

    circle = Shape.Circle(5, 2, 7)
    print(circle)
    print(circle.area)
    print(circle.radius)

    # circle.radius = -2
    print("r = {}".format(circle.radius))

