
import urllib.request


# Создать функцию, которая будет скачивать файл из интернета по
# ссылке, повесить на неё декоратор, который будет запускать целевую
# функцию каждый раз в отдельном потоке. Создать список из 10
# ссылок, по которым будет происходить скачивание. Каждый поток
# должен сигнализировать, о том, что, он начал работу и по какой
# ссылке он работает, так же должен сообщать когда скачивание
# закончится.


def run_async(func):
    from threading import Thread
    from functools import wraps

    @wraps(func)
    def async_func(*args, **kwargs):
        func_hl = Thread(target=func, args=args, kwargs=kwargs)

        print(f'{Thread.name} working')
        func_hl.start()
        print(f'{Thread.name} finished')
        return func_hl

    return async_func


if __name__ == '__main__':

    import urllib.request
    import random


    @run_async
    def download(i):

        filename = random.sample(range(1, 100), 1)
        location = f'C:\\Users\\1\\PycharmProjects\\itea_october\\Lesson5\\{filename}.png'
        urllib.request.urlretrieve(i, location)


    def main():
        list = ['https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.292.100.png',
                'https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.297.100.png',
                'https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.266.100.png',
                'https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.265.100.png',
                'https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.154.100.png',
                'https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.292.100.png',
                'https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.155.100.png',
                'https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.258.100.png',
                'https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.123.100.png',
                'https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.295.100.png']

        for i in list:
            download(i)


    main()
