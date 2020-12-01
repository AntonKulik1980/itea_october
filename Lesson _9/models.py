import mongoengine as me
import datetime
me.connect('TEST_LESSON12')


class User(me.Document):
    first_name = me.StringField(min_length=2, max_length=64, required=True)
    Last_name = me.StringField(min_length=2, max_length=64)
    interests = me.ListField()
    age = me.IntField(min_value=12, max_value=99)
    created_at = me.DateTimeField()

    def say_hello(self):
        return f'Hello my name is {self.first_name}'


    def __str__(self):
        return f'{self.first_name} {self.age}'

    def save(self,*args,**kwargs):
        self.created_at = datetime.datetime.now()
        super().save(*args,**kwargs)

# if __name__ == 'main':
user = User(first_name='Jhon',interests = ['sport','programing'],age = 18)
user.save()
# users = User.objects(me.Q(age__gte=20) | me.Q(first_name='Jhon'))
# for u in users:
#     print(u.say_hello())

# user = User(first_name ='Nikolay', interests=['cars'],age=25)
#
# user.save()
# print(user.age,user.first_name,user.id)
