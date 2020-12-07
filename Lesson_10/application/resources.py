from flask_restful import Resource
from flask import request
from .models import User
from .shemas import UserSchema
import json
from marshmallow.exceptions import ValidationError

class UserResource(Resource):

    def get(self,id=None):
        if id:
            return json.loads(User.objects.get(id=id).to_json())
        else:
            users = User.objects()
            return json.loads(users.to_json())

    def post(self):
        try:
            UserSchema().load(request.json)
        except ValidationError as e:
            return {'text': str(e)}
        user = User(**request.json).save()
        return UserSchema().dump(user)


    def put(self):
        pass

    def delete(self):
        pass
