from flask import Flask
from flask import Response, request, Blueprint, g
from flask_restful import Api
from flask_jwt_extended import get_jwt_identity, jwt_required
from uuid import uuid4

from app.views import BaseResource, json_required
from app.models.account import *
from app.models.post import *

api = Api(Blueprint(__name__, __name__))


@api.resource('/image')
class Image(BaseResource):
    @jwt_required
    def post(self):
        images = request.files.getlist("files[]")
        names = []

        for image in images:
            extension = image.filename.split('.')[-1]
            image_name = '{}.{}'.format(str(uuid4()), extension)

            image.save('./static/img/{0}'.format(image.filename))
            names.append(image_name)

        return names, 201


@api.resource('/post')
class Post(BaseResource):
    @jwt_required
    @json_required({'title': str, 'content': str, 'category': int, 'image_names': list})
    def post(self):

        title = request.json['title']
        content = request.json['content']
        category_int = int(request.json['category'])
        image_names = request.json['image_names']

        category = CategoryModel.objects(id=category_int).first()
        print("asf")
        user = AccountModel.objects(id=get_jwt_identity()).first()
        print("asf")
        post = PostModel(owner=user, title=title, content=content, category=category.id, image_name=image_names).save()

        return str(post.id)