from flask import request, Response, abort, Blueprint
from flask_restful import Api
from flask_jwt_extended import JWTManager, create_refresh_token, get_jwt_identity
from flasgger import swag_from

from app.views import BaseResource
from app.models.account import AccountModel, RefreshTokenModel

api = Api(Blueprint(__name__, __name__))


@api.resource("/change/pwd")
class account(BaseResource):
    # @swag_from(ACCOUNT) 이거는 swagger 랑 연동해주는 데코레이터에요 근데 이게 안되네요? ㅎㅎ
    def patch(self):

        user = AccountModel.objects(get_jwt_identity()).first()

        current_pw = request.json['current_pw'] # 확인

        if user.pwd != current_pw or not user:
            abort(400)

        change_pw = request.json['change_pw']

        if current_pw == change_pw:
            return "기존 비밀번호와 같습니다. 다시 설정해 주십시오.", 409

        user.update(pwd=change_pw)
        return "비밀번호가 성공적으로 바뀌었습니다. 다시 로그인 해주세요?", 200





