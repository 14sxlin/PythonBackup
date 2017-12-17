class FuzzBool:
    def __init__(self, value=0.0):
        self.__value = value

    @property
    def value(self):
        return self.__value

    def __invert__(self):  # ~ operator
        return FuzzBool(1.0 - self.__value)

    def __and__(self, other):  # & op
        return FuzzBool(min(self.__value, other.value))

    def __iand__(self, other):  # &= op
        self.__value = min(self.__value, other.value)

    def __or__(self, other):  # ^ op
        return FuzzBool(max(self.__value, other.value))

    def __ior__(self, other):
        self.__value = max(self.__value, other.value)

    def __repr__(self):  # str used by eval()
        return "{0}({1})".format(self.__class__.__name__, self.__value)

    def __str__(self):
        return str(self.__value)

    def __bool__(self):     # used by if
        return self.__value > 0.5

    def __int__(self):          # used by int()
        return round(self.value)

    def __float__(self):        # used by float()
        return self.value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __le__(self, other):
        return self.value <= other.value

    def __hash__(self):
        return hash(id(self))

    def __format__(self, format_spec):
        return self.__value.__format__(format_spec)

    @staticmethod
    def conjunction(*fuzzies):
        return FuzzBool(min([x for x in fuzzies]))


