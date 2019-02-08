from flask import request, Response, Blueprint, jsonify
import uuid
from flask_restful import Api
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_refresh_token_required, get_jwt_identity
from flasgger import swag_from

from app.views import BaseResource
from app.models.account import AccountModel, RefreshTokenModel
from app.docs.user.auth import AUTH


api = Api(Blueprint(__name__, __name__))


def generate_refresh_token(user):
    while True:
        refresh_token = str(uuid.uuid4())
        if not RefreshTokenModel.objects(token_uuid=refresh_token):
            break
    if user.pwd:
        RefreshTokenModel(token_uuid=refresh_token, token_owner=user, pwd_snapshot=user.pwd).save()
    else:
        RefreshTokenModel(token_uuid=refresh_token, token_owner=user).save()
    return refresh_token


@api.resource('/auth')
class Auth(BaseResource):
    @swag_from(AUTH)
    def post(self):

        email = request.json['email']
        pwd = request.json['pwd']

        user = AccountModel.objects(email=email).first()

        if user and user.pwd == pwd:
            return jsonify(
                access_token=create_access_token(user.email),
                refresh_token=create_refresh_token(generate_refresh_token(user))
            )
        else:
            return Response('login failed', 401)


@api.resource('/refresh')
class RefreshToken(BaseResource):
    @jwt_refresh_token_required
    def post(self):
        token = RefreshTokenModel.objects(token_uuid=get_jwt_identity()).first()

        if not token:
            return Response('', 401)
        if token.token_owner.id.pw != token.pwd_snapshot:
            return Response('', 205)

        return {
            'access_token': create_access_token(token.token_owner.id)
        }, 200


