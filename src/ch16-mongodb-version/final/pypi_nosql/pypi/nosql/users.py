import datetime
import mongoengine


class User(mongoengine.Document):
    email = mongoengine.StringField()
    name = mongoengine.StringField()
    hashed_password = mongoengine.StringField()
    created_date = mongoengine.DateTimeField(default=datetime.datetime.now)

    meta = {
        'db_alias': 'core',
        'collection': 'users',
        'indexes': [
            'created_date',
            'email',
        ]
    }
