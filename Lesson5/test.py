# def run_async(func):
#
#     from threading import Thread
#     from functools import wraps
#
#     @wraps(func)
#     def async_func(*args, **kwargs):
#
#
#         func_hl = Thread(target=func, args=args, kwargs=kwargs)
#
#
#         print(f'{Thread.name} working')
#         func_hl.start()
#         print(f'{Thread.name} finished')
#         return func_hl
#     return async_func
#
#
# if __name__ == '__main__':
#     from time import sleep
#     import urllib.request
#     import random
#
#
#
#     @run_async
#     def download(i):
#
#         filename = random.sample(range(1, 100), 1)
#         location = f'C:\\Users\\1\\PycharmProjects\\itea_october\\Lesson5\\{filename}.png'
#         urllib.request.urlretrieve(i, location)
#
#
#     def main():
#         list = ['https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.292.100.png',
#                 'https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.297.100.png',
#                 'https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.266.100.png',
#                 'https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.265.100.png',
#                 'https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.154.100.png',
#                 'https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.292.100.png',
#                 'https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.155.100.png',
#                 'https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.258.100.png',
#                 'https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.123.100.png',
#                 'https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.295.100.png']
#
#         for i in list:
#             print(i)
#             download(i)
#
#
#     main()


class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


with File('demo.txt', 'w') as opened_file:
    opened_file.write('Hello, world!')
