from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
cars = [
    {'model': 'BMW',
     'price': 12000},
]


# def add_car(**kwargs):
#     SQL = 'SQL '.execude(kwargs.get('price'), kwargs.get('model'))

@app.route('/cars')
def get_cars():
    return render_template('get_cars.html', cars=cars)


@app.route('/add_cars', methods=['GET', 'POST'])
def add_cars():
    if request.method == 'POST':
        cars.append(request.form)
        return redirect(url_for('get_cars'))
    return render_template('add_car.html')


app.run(debug=True)