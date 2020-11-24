# 1) Создать базу данных товаров, у товара есть: Категория (связанная
# таблица), название, есть ли товар в продаже или на складе, цена, кол-во
# единиц.Создать html страницу. На первой странице выводить ссылки на все
# категории, при переходе на категорию получать список всех товаров в
# наличии ссылками, при клике на товар выводить его цену, полное описание и
# кол-во единиц в наличии.






from flask import Flask, render_template
import sqlite3


class dbconnection(object):
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, type, value, traceback):
        self.conn.close()


app = Flask(__name__)





@app.route('/categories/')
def get_categories():
    with dbconnection('shop.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT cat_id,Category_name FROM Category')
        categories = dict(cursor.fetchmany(10))
        return render_template('/categories.html', categories=categories)



@app.route('/categories/<string:category>')
def get_category_product(category):
    with dbconnection('shop.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f'select p_id,name from Products where Category_id ={category}')
        products = dict(cursor.fetchmany(10))
        return render_template('/products.html', products=products)

@app.route('/products/<string:product>')
def get_detail_product(product):
    with dbconnection('shop.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f'select instock,q_ty,price from Products where p_id={product} ')
        product = dict(cursor.fetchmany(10))
        return render_template('/product_detail.html', product=product)







app.run(debug=True)
