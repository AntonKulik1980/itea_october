import mongoengine as me

me.connect('REST_API_LESSON_11')


class UserProfile(me.Document):
    login = me.StringField(required=True, unique=True, min_length=4, max_length=128)
    password = me.StringField(required=True, min_length=8)
    about_me = me.StringField()
    likes = me.IntField(default=0)

    def __str__(self):
        return str(self.id)


class User(me.Document):
    first_name = me.StringField(min_length=2, max_length=64, required=True)
    last_name = me.StringField(min_length=2, max_length=64)
    age = me.IntField(min_value=12, max_value=99,)
    interests = me.ListField()
    created_at = me.DateTimeField()
    user_profile = me.ReferenceField(UserProfile)


if __name__ == '__main__':
    # User.drop_collection()
    # UserProfile.drop_collection()
    up = UserProfile(login='ertert', password='dfgdfg56546', about_me='5656').save()
    User(first_name='Nikolai', interests=['cars'], age=23, user_profile=up).save()
    User(first_name='James', interests=['programming'], age=20, user_profile=up).save()


# User.drop_collection()
# User.objects().delete()