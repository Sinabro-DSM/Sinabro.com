from flask_restful import Api
from flask import Blueprint, Response, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.views import BaseResource
from app.models.account import AccountModel
from app.models.post import CategoryModel

api = Api(Blueprint(__name__, __name__))


@api.resource('/category')
class Category(BaseResource):
    @jwt_required
    def post(self):
        '''
        카테고리 추가
        '''
        user = AccountModel.objects(email=get_jwt_identity()).first()
        if not user:
            return Response('', 401)

        category_name = request.json['category_name']
        category_id = request.json['category_id']

        CategoryModel(name=category_name, id=category_id).save()
        return Response('', 201)

    @jwt_required
    def delete(self):
        user = AccountModel.objects(email=get_jwt_identity()).first()
        if not user:
            return Response('', 401)
        category_name = request.json['category_name']

        category = CategoryModel.objects(name=category_name).first()

        category.delete()
        return Response('', 200)