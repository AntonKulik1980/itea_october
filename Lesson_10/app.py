from flask import Flask, request
from .models import User


app = Flask(__name__)


@app.route('/user',methods=['GET','PUT','POST','DELETE'])
@app.route('/user/<int:user_id>',methods=['GET','PUT','POST','DELETE'])
def user(user_id=None):
    if request.method == 'GET':
        users = User.objects()
        users_json = users.to_json()
        return users_json
    elif request.method == 'PUT':
        pass
    elif request.method == 'POST':
        pass
    elif request.method == 'DELETE':
        pass



app.run(debug=True)