from datetime import datetime

from mongoengine import *
from app.models.account import AccountModel

class PostBase(Document):
    meta = {
        'collection': 'post_model'
    }
    creation_time = DateTimeField(required=True, default=datetime.now())

    owner = ReferenceField(AccountModel, required=True)
    title = StringField(required=True)
    content = StringField(required=True)
    category = StringField(required=True)

    image_name = StringField()


class CommentModel(Document):
    mata = {
        'collection': 'comment_model'
    }
    post = ReferenceField()
    creation_time = DateTimeField(required=True, default=datetime.now())
    owner = ReferenceField(required=True)
    content = StringField(required=True)

