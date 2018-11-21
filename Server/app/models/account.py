from mongoengine import *


class TempAccountModel(Document):
    meta = {
        'collection': 'user_temp'
    }

    email = StringField(required=True, primary_key=True)

    pwd = StringField(required=True)

    name = StringField(required=True)

    certify_uri = StringField(required=True)

    isAdmin = BooleanField(default=False)


class AccountModel(Document):
    meta = {
        'collection': 'user_account'
    }
    email = StringField(required=True, primary_key=True)
    pwd = StringField(required=True)

    name = StringField(required=True)

    bio = StringField(required=True, default='')

    isAdmin = BooleanField(default='')


class CertifyCodeModel(Document):
    meta = {
        'collection': 'certify_code_model'
    }
    email = StringField(required=True)
    certify_code = StringField(required=True)
