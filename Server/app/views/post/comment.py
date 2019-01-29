from flask import Response, request, Blueprint
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
        if not user:
            return Response('', 401)

        if not post:
            return Response('post not exist', 204)

        content = request.json['content']

        comment = CommentModel(content=content, owner=user, post=post).save()

        return Response(str(comment.id), 201)


@api.resource(('/post/<post_id>/comment/<comment_id>'))
class CommentDetail(BaseResource):
    @jwt_required
    def delete(self, post_id, comment_id):
        """
        댓글 삭제
        """
        comment = CommentModel.objects(id=comment_id).first()
        user = AccountModel.objects(email=get_jwt_identity()).first()
        if not user:
            return Response('', 401)

        if not comment:
            return Response('', 204)

        if user != comment.owner:
            return Response('', 403)

        comment.delete()

        return Response('', 200)

    @jwt_required
    def patch(self, post_id, comment_id):
        user = AccountModel.objects(email=get_jwt_identity()).first()
        comment = CommentModel.objects(id=comment_id).first()

        if not user:
            return Response('', 401)

        if not comment:
            return Response('', 204)

        if user != comment.owner:
            return Response('', 403)
        content = request.json['content']

        comment.update(content=content)

        return Response('', 200)
