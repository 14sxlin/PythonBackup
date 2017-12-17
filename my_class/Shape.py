import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Point({0.x!r},{0.y!r})".format(self)

    def __str__(self):
        return "{0.x!r},{0.y!r}".format(self)


class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self._radius = radius

    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)

    @property
    def area(self):
        return self.radius ** 2 * math.pi

    @property
    def radius(self):
        """
        :return: The Circle 's area
        """
        return self._radius

    @radius.setter
    def radius(self, radius):
        assert radius >= 0, "radius should >= 0"
        self._radius = radius

    def circumference(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        if isinstance(other, Circle):
            raise NotImplemented
        return super().__eq__(other) and self.radius == other.radius

    def __repr__(self):
        return "Circle({0.radius},{0.x!r},{0.y!r})".format(self)

    def __str__(self):
        return repr(self)
