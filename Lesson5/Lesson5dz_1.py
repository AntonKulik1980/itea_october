# Создать декоратор, который будет запускать функцию в отдельном
# потоке. Декоратор должен принимать следующие аргументы:
# название потока, является ли поток демоном.



from functools import wraps
import time
from threading import Thread



def decorartor(name='first', daemon=False):
    def actual_decorartor(func):
        @wraps(func)
        def wrapper(*args):
            result = Thread(target=func, args=args, name=name, daemon=daemon)
            result.start()

        return wrapper

    return actual_decorartor


@decorartor('second', False)
def io_bound(id_, sec):
    print(f'{id_} Уснула')
    time.sleep(sec)
    print(f'{id_} Проснулась')


result = io_bound('10', 5)
print(result)