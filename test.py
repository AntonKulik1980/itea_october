# # def sales(sales, items):
# #     sales_utd = sales + items
# #     print(sales_utd)
# #
# #
# # sales(10,10)
#
# def sum_(required_value, *args):
#     print(args)
#     result = 0
#     for i in (required_value, ) + args:
#         result += i
#     return result
#
# data = []
#
# result = sum_(1, 2)
# print(result)
# # То же, что и выше
# print(sum_(100, 200, 300, 400))
#
#
# class shop():
#
#     items: int
#
#     def __init__(self,name,sales):
#         self.name = name
#         self.sales = sales
#
#
#
#     def sale(self,items):
#         self.items = items
#         self.sales = self.items + self.sales
#         print(self.sales)
#
#
#
#     # def sup(required_value, *added):
#     #     result = 0
#     #     for i in (required_value,) + added:
#     #         result += i
#     #     return result
#     #     print(result)
#
#
# print('-'*35)
# shop1 = shop('First', 10)
# print(shop1.sales)
# shop2 = shop('Second', 2)
# print(shop2.sales)
# print(shop2.sale(10))
# print(shop2.sale(15))

class Smartphone():

    type_ = 'Смартфон'

    def download_application(self):
        print('Downloading application from market')


Smartphone.download_application()