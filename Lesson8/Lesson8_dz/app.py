# 1) Создать базу данных товаров, у товара есть: Категория (связанная
# таблица), название, есть ли товар в продаже или на складе, цена, кол-во
# единиц.Создать html страницу. На первой странице выводить ссылки на все
# категории, при переходе на категорию получать список всех товаров в
# наличии ссылками, при клике на товар выводить его цену, полное описание и
# кол-во единиц в наличии.

from flask import Flask, render_template, request, redirect, url_for
import sqlite3


class dbconnection(object):
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, type, value, traceback):
        self.conn.commit()
        self.conn.close()


app = Flask(__name__)


cat = []


@app.route('/categories/')
def get_categories():
    with dbconnection('shop.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT cat_id,Category_name FROM Category')
        categories = cursor.fetchmany(10)
        return render_template('/categories.html', categories=categories)



@app.route('/categories/<string:category>')
def get_category_product(category):
    with dbconnection('shop.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f'select p_id,name from Products where Category_id ={category}')
        products = cursor.fetchmany(10)
        return render_template('/products.html', products=products)

@app.route('/products/<string:product>')
def get_detail_product(product):
    with dbconnection('shop.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f'select instock,q_ty,price from Products where p_id={product} ')
        product = cursor.fetchmany(10)
        return render_template('/product_detail.html', product=product)

@app.route('/add_cat', methods=['GET', 'POST'])
def add_cat():
    with dbconnection('shop.db') as conn:
        cursor = conn.cursor()
        if request.method == 'POST':
            a = request.form.get('Category_name')
            cursor.execute(f'insert into Category (category_name) values ("{a}")')

            return redirect(url_for('get_categories'))
    return render_template('add_cat.html')

@app.route('/add_prod', methods=['GET', 'POST'])
def add_prod():
    with dbconnection('shop.db') as conn:
        cursor = conn.cursor()
        if request.method == 'POST':
            a = request.form.get('name')
            b = request.form.get('instok')
            c = request.form.get('Q_ty')
            d = request.form.get('Category_id')
            e = request.form.get('Price')
            cursor.execute(f'insert into Products (name,instok,Q_ty,Category_id,Price) values ("{a}","{b}","{c}","{d}",'
                           f'"{e}")')

            return redirect(url_for('get_categories'))
    return render_template('add_prod.html')







app.run(debug=True,port=8000)
