from flask import Flask,render_template,request,redirect

app = Flask(__name__)
cars = [
    {'model':'BMW',
     'price':12000
     }

]

@app.route('/cars')
def get_cars():
    print(request)
    return render_template('get_cars.html',cars=cars)


@app.route('/add_cars',methods=['GET','POST'])
def add_cars():
    if request.method == 'POST':
        cars.append(request.form)
        return redirect('/cars')
    return render_template('add_cars.html')

app.run(debug=True)