from unittest import TestCase
import ujson

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

    def _create_fake_account(self):
        AccountModel(email=self.email, pwd=self.pwd, name=self.name, isAdmin=False).save()

    def _get_tokens(self):
        res = self.client.post('/auth', json={'email': self.email, 'pwd': self.pwd})

        data = ujson.loads(self.decode_data(res))

        self.access_token = 'JWT {}'.format(data['access_token'])
        self.refresh_token = 'JWT {}'.format(data['refresh_token'])

    def decode_data(self, res):
        return res.data.decode()

    def setUp(self):
        self._create_fake_account()
        AccountModel.objects.delete()
        self._get_tokens()

    def tearDown(self):
        AccountModel.objects.delete()
        RefreshTokenModel.objects.delete()
        PostModel.objects.delete()

    def json_request(self, method, target_url, token=None, *args, **kwargs):
        data = kwargs.pop('data')

        return method(
            target_url,
            json=data if data else None,
            headers={'Authorization': token or self.access_token},
            *args, **kwargs)

    def request(self, method, target_url, token=None, *args, **kwargs):
        return method(
            target_url, headers = {'Authorization': token or self.access_token},
            *args, **kwargs
        )