from datetime import datetime

from mongoengine import *
from app.models.account import AccountModel


class CategoryModel(Document):
    meta = {
        'collection': 'category_model'
    }
    name = StringField(required=True)
    id = IntField(primary_key=True)


class PostModel(Document):
    meta = {
        'collection': 'post_model'
    }
    creation_time = DateTimeField(required=True, default=datetime.now())

    owner = ReferenceField(AccountModel)
    title = StringField(required=True)
    content = StringField(required=True)
    category = ReferenceField(CategoryModel)
    reaction = ListField(StringField())
    image_name = ListField(StringField())


class CommentModel(Document):
    meta = {
        'collection': 'comment_model'
    }
    post = ReferenceField(PostModel)
    creation_time = DateTimeField(required=True, default=datetime.now())
    owner = ReferenceField(AccountModel, required=True)
    content = StringField(required=True)
    reaction = ListField(StringField())

