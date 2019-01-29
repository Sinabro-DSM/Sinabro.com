from flask import Response, request, Blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Api

from app.models.post import PostModel, CommentModel
from app.models.account import AccountModel
from app.views import BaseResource

api = Api(Blueprint(__name__, __name__))


@api.resource('/post/<post_id>/reaction')
class PostReaction(BaseResource):
    @jwt_required
    def post(self, post_id):
        user = AccountModel.objects(email=get_jwt_identity()).first()
        if not user:
            return Response('', 401)

        post = PostModel.objects(id=post_id).first()
        if not post:
            return Response('', 204)

        if user.id not in post.reaction:
            post.reaction.append(user.id)
            post.save()
        return Response('', 201)

    @jwt_required
    def delete(self, post_id):
        user = AccountModel.objects(id=get_jwt_identity()).first()
        if not user:
            return Response('', 401)

        post = PostModel.objects(id=post_id).first()
        if not post:
            return Response('', 204)
        if user.id in post.reaction:
            post.reaction.remove(user.id)
            post.save()
        return Response('', 200)


@api.resource('/post/<post_id>/comment/<comment_id>/reaction')
class CommentReaction(BaseResource):
    @jwt_required
    def post(self, post_id, comment_id):
        user = AccountModel.objects(email=get_jwt_identity()).first()
        if not user:
            return Response('', 401)

        comment = CommentModel.objects(id=comment_id).first()
        if not comment:
            return Response('', 204)
        if user.id not in comment.reaction:
            comment.reaction.append(user.id)
            comment.save()
        return Response('', 201)

    @jwt_required
    def delete(self, comment_id):
        user = AccountModel.objects(id=get_jwt_identity()).first()
        if not user:
            return Response('', 401)
        comment = CommentModel.objects(id=comment_id).frist()
        if not comment:
            return Response('', 204)
        if user.id in comment.reaction:
            comment.reaction.remove(user.id)
            comment.save()
        return Response('', 200)