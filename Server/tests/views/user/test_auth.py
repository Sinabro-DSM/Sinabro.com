from tests.views import TestBase


class TestAuth(TestBase):
    def setUp(self):
        super(TestAuth, self).setUp()
        self.create_fake_account()

    def tearDown(self):
        super(TestAuth, self).tearDown()

    def testAuth(self):
        res = self.json_request(self.client.post, '/auth', data={'email': self.email, 'pwd': self.pwd}, token=None)
        self.assertEqual(res.status_code, 200)

        data = res.json
        self.assertIsInstance(data, dict)

        self.assertIn('access_token', data)

        # Exception test
        res = self.json_request(self.client.post, '/auth', data={'email': 'asdf', 'pwd': self.pwd}, token=None)
        self.assertEqual(res.status_code, 401)

        res = self.json_request(self.client.post, '/auth', data={'email': self.email, 'pwd': 'asdf'}, token=None)
        self.assertEqual(res.status_code, 401)
