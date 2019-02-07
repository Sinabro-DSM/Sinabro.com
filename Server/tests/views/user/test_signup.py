from tests.views import TestBase

from app.models.account import TempAccountModel, AccountModel
from uuid import uuid4


class TestSignup(TestBase):
    def setUp(self):
        super(TestSignup, self).setUp()

        self.test_email = 'rsy011203@gmail.com'

    def tearDown(self):
        TempAccountModel.objects.delete()
        AccountModel.objects.delete()

        super(TestSignup, self).tearDown()

    def testSignup(self):
        res = self.json_request(self.client.post, '/signup',
                                data={'email': self.test_email, 'pwd': self.pwd, 'name': self.name, 'isAdmin': self.isAdmin})

        self.assertEqual(res.status_code, 200)

        certify_url = TempAccountModel.objects(email=self.test_email).first().certify_uri

        res = self.json_request(self.client.get, '/certify/{}'.format(certify_url), data=None)
        self.assertEqual(res.status_code, 201)

         #Exception test

        res = self.json_request(self.client.post, '/signup',
                                data={'email': self.test_email, 'pwd': self.pwd, 'name': self.name,
                                      'isAdmin': self.isAdmin})
        self.assertEqual(res.status_code, 409)

        certify_url = uuid4()
        res = self.json_request(self.client.get, '/certify/{}'.format(certify_url), data=None)
        self.assertEqual(res.status_code, 404)