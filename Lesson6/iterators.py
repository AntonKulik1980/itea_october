# a = [1, 2, 3, 4, 5]
#
# for i in a:
#     print(a)
#
# iterable = iter(a)
# print(next(iterable))
# print(next(iterable))
# print(next(iterable))
# print(next(iterable))
# print(next(iterable))

class MyRangeIterable:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __next__(self):
        if self.start <= self.end:
            value = self.start
            self.start += 1
            return value
        raise StopIteration


class My_range:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return MyRangeIterable(self.start, self.end)


print(list(My_range(10,20)))



class Randomiter:

    def __init__(self,numbers):
        self.counter = 0
        self.number = numbers


    def __iter__(self):
        return self


    























