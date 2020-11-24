import mongoengine as me

me.connect('TEST_LESSON11')

class User(me.Document):
    first_name = me.StringField(min_length=2,max_length=64,required=True)
    Last_name = me.StringField(min_length=2,max_length=64)
    interests = me.ListField()
    age = me.IntField(min_value=12,max_value=99)


# if __name__ == 'main':
# user = User(first_name='Jhon',interests = ['sport','programing'],age = 18)
# user.save()
users = User.objects()
for u in users:
 print(u.first_name)
