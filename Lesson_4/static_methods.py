from abc import ABC, abstractmethod
class Shop:

    total_sales = 0

    def __init__(self,shop_name, sales):
        self.shop_name = shop_name
        self.sales = sales
        Shop.total_sales += sales

    def make_sales(self,num):
        self.sales += sales
        Shop.total_sales += sales


    @classmethod
    def get_total_sales(cls):
        if Shop.total_sales <1000:
            return ('Sales are low',cls.total_sales)
        return ('Sales are higth',cls.total_sales)





print(Shop.get_total_sales())