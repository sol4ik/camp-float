class FloatingPoint:
    def __init__(self, number=0, point_position=0):
        self.number = number
        self.point = point_position
        self.length = 0
        self.get_length()

    def get_length(self):
        self.length = len(str(self.number))

    def __str__(self):
        return str(self.number)[:self.length - self.point] + '.' + str(self.number)[self.length - self.point:]
    # array
    # array[index_1:]

    def __add__(self, other):
        to_return = FloatingPoint()
        if self.point != other.point:
            if self.length > other.length:
                other.number *= 10 ** (self.length - other.length)
                other.point += (self.length - other.length)
                other.length = self.length
            elif self.length < other.length:
                self.number *= 10 ** (other.length - self.length)
                self.point += (other.length - self.length)
                self.length = other.length
        to_return.number = self.number + other.number
        to_return.point = self.point
        to_return.get_length()
        return to_return

    def __sub__(self, other):
        # to do at home
        pass

    def __mul__(self, other):
        to_return = FloatingPoint()
        to_return.number = self.number * other.number
        to_return.point = self.point + other.point
        to_return.get_length()
        return to_return

    def __div__(self, other):
        to_return = FloatingPoint()
        tmp_1 = self.number
        tmp_2 = other.number
        tmp_1 *= 10 ** max(self.length - self.point, other.length - other.point)
        tmp_2 *= 10 ** max(self.length - self.point, other.length - other.point)
        to_return.number = tmp_1 / tmp_2
        while to_return.number % 1 != 0:
            to_return.number *= 10
            to_return.point += 1
        to_return.get_length()
        return to_return

    def __divmod__(self, other):
        # optional at home
        pass
