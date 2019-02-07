from flask import request, Response, abort, Blueprint
from flask_restful import Api
from flask_jwt_extended import get_jwt_identity, jwt_required
from flasgger import swag_from

from app.views import BaseResource
from app.models.account import AccountModel
from app.docs.user.account import CHANGE_PWD

api = Api(Blueprint(__name__, __name__))


@api.resource("/change/pwd")
class Account(BaseResource):
    @jwt_required
    @swag_from(CHANGE_PWD)
    def patch(self):

        user = AccountModel.objects(email=get_jwt_identity()).first()

        current_pwd = request.json['current_pw']  # 확인

        if user.pwd != current_pwd or not user:
            return Response('invalid', 401)

        change_pwd = request.json['change_pw']

        if current_pwd == change_pwd:
            return Response('same', 204)

        if user.update(pwd=change_pwd):
            return Response('success', 200)
        else:
            abort(500)
