from flask import Flask
from flask import Response, request, Blueprint, jsonify
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
        user = AccountModel.objects(email=get_jwt_identity()).first()

        post = PostModel(owner=user, title=title, content=content, category=category.id, image_name=image_names).save()
        return str(post.id)

    def get(self):
        page = int(request.args['page'])
        category = request.args['category']

        return jsonify([{
            'post_id': str(postContent.id),
            'creation_time': str(postContent.creation_time),
            'content': postContent.content[:20],
            'title': postContent.title,
            'category': postContent.category.id,
            'author': postContent.owner.name
        } for postContent in PostModel.objects(category=category).skip((page-1)*20).limit(20)])


@api.resource('/post/<post_id>')
class PostContent(BaseResource):
    def get(self, post_id):
        """
        게시물 상세 정보
        :return:
        """
        post = PostModel.objects(id=post_id).first()
        if not post:
            return Response('', 204)

        comments = CommentModel.objects(post=post)

        return jsonify({
            'creation_time': str(post.creation_time),
            'post_id': str(post.id),
            'title': post.title,
            'content': post.content,
            'owner_name': post.owner.name,
            'owner_id': str(post.owner.id),
            'category': post.category.id,
            'comments': [{
                'author': comment.owner.name,
                'creation_time': str(comment.creation_time),
                'content': comment.content,
                'comment_id': str(comment.id)
            } for comment in comments]
        })

    @jwt_required
    def delete(self, post_id: str) -> Response:
        """
        게시물 삭제
        """
        post = PostModel.objects(id=post_id).first()
        if not post:
            return Response('', 410)

        author = AccountModel.objects(email=get_jwt_identity()).first()

        # 삭제요청자

        if author == post.owner:
            post.delete()
            return Response("success", 200)

        return Response('fail', 401)

    def patch(self):
        """
        게시물 수정
        """

