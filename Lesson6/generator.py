import random


def random_numbers_generator(num):
    start = 0

    while start < num:
        yield random.randint(0, 100)
        start += 1


# for i in random_numbers_generator(10):
#     print(i)


iterator = iter(random_numbers_generator(10))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


a = [x for x in range(10)]
print(a)