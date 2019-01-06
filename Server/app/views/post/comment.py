from flask import Flask
from flask import Response, request, Blueprint, g
from flask_restful import Api
from flask_jwt_extended import get_jwt_identity, jwt_required
from uuid import uuid4

from app.views import BaseResource, json_required
from app.models.account import *
from app.models.post import *

api = Api(Blueprint(__name__, __name__))


@api.resource('/post/<post_id>/comment')
class Comment(BaseResource):
    @jwt_required
    @json_required({'content': str})
    def post(self,  post_id):

        post = PostModel.objects(id=post_id).first()
        user = AccountModel.objects(email=get_jwt_identity()).first()

        if not post:
            return Response('post not exist', 404)

        content = request.json['content']

        comment = CommentModel(content=content, owner=user, post=post).save()

        return Response('success', 201)