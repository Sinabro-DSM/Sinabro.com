from unittest import TestCase

from app import create_app
from config import Config
from app.models.account import AccountModel, RefreshTokenModel
from app.models.post import PostModel


class TestBase(TestCase):
    def __init__(self, *args, **kwargs):
        self.app = create_app(Config)
        self.email = 'rsy011203@gmail.com'
        self.pwd = 'sadasd'
        self.name = 'sinabrodotcom'
        self.isAdmin = False

        self.client = self.app.test_client()

        super(TestBase, self).__init__(*args, **kwargs)

    def create_fake_account(self):
        AccountModel(email=self.email, pwd=self.pwd, name=self.name, isAdmin=False).save()

    def get_tokens(self):
        res = self.client.post('/auth', json={'email': self.email, 'pwd': self.pwd})

        self.access_token = 'JWT {}'.format(res.json['access_token'])
        self.refresh_token = 'JWT {}'.format(res.json['refresh_token'])

    def decode_data(self, res):
        return res.data.decode()

    def tearDown(self):
        AccountModel.objects.delete()
        RefreshTokenModel.objects.delete()
        PostModel.objects.delete()

    def json_request(self, method, target_url, token, *args, **kwargs):
        data = kwargs.pop('data')

        return method(
            target_url,
            json=data if data else None,
            headers={'Authorization': token},
            *args, **kwargs)