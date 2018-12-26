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
    id = StringField(required=True, primary_key=True)
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


class RefreshTokenModel(Document):
    meta = {
        'collection': 'refresh_token'
    }
    token_owner = ReferenceField(AccountModel, required=True)
    token_uuid = StringField(primary_key=True)
    pwd_snapshot = StringField()
