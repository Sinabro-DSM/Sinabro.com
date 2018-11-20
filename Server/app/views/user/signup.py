from flask import Blueprint, Response, request, abort, current_app
from flask_restful import Api
from flasgger import swag_from
from email.mime.multipart import MIMEMultipart
import uuid
import smtplib
from email.mime.text import MIMEText

from app.models.account import AccountModel, TempAccountModel
from app.views import json_required, BaseResource

api = Api(Blueprint(__name__, __name__))


@api.resource('/signup')
class Signup(BaseResource):
    @swag_from()
    @json_required({'email': str, 'pwd': str, 'name': str, 'isAdmin': bool})
    def post(self):
        email = request.json['email']
        pwd = request.json['pwd']
        name = request.json['name']
        isAdmin = request.json['isAdmin']

        if AccountModel.objects(email=email):
            return {'msg': 'email duplicated'}, 409
        else:

            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login('sinabrocommunity@gmail.com', 'sinabroisbest')

            certify_uri = str(uuid.uuid4()).replace("-", "")

            temp = TempAccountModel(email=email, pwd=pwd, name=name, certify_uri=certify_uri, isAdmin=isAdmin)
            temp.save()

            html = '<a href=http://localhost:5050/certify/{}>인증하기</a>'.format(certify_uri)
            msg = MIMEText(html, 'html')
            body = MIMEMultipart()
            body['From'] = 'rsy011203@gmail.com'
            body['To'] = email

            body.attach(msg)
            smtp.sendmail('rsy011203@gmail.com', email, msg=body.as_string())
            smtp.quit()
            print("성공")

            return Response('', 200)


@api.resource('/certify/<certify_uri>')
class EmailCertify(BaseResource):
    def get(self, certify_uri):
        user = TempAccountModel.objects(certify_uri=certify_uri).first()

        if not user:
            return Response('', 404)
        email, pwd, name, isAdmin = user.email, user.pwd, user.name, user.isAdmin
        user.delete()
        AccountModel(email=email, pwd=pwd, name=name, isAdmin=isAdmin).save()

        return Response('success', 200)
