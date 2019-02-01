from tests.views import TestBase

from app.models.account import TempAccountModel
import ujson


class TestSignup(TestBase):
    def setUp(self):
        super(TestSignup, self).setUp()

    def tearDown(self):
        TempAccountModel.objects.delete()

        super(TestSignup, self).tearDown()

    def testSignup(self):
        res = self.json_request(self.client.post, '/auth', data={'email': self.email, 'pwd': self.pwd})

        self.assertEqual(res.status_code, 200)

        data = ujson.load(self.decode_data(res))
        self.assertIsInstance(data, dict)


        #Exception test

        res = self.json_request(self.client.post, '/auth', data={'email': 'asdf', 'pwd': self.pwd})
        self.assertEqual(res.status_code, 201)

        res = self.json_request(self.client.post, '/auth', data={'email': self.email, 'pwd': 'asdf'})
        self.assertEqual(res.status_code, 401)