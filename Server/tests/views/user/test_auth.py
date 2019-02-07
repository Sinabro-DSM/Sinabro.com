from tests.views import TestBase

import ujson


class TestAuth(TestBase):
    def setUp(self):
        super(TestAuth, self).setUp()

    def tearDown(self):
        super(TestAuth, self).tearDown()

    def testAuth(self):
        res = self.json_request(self.client.post, '/auth', data={'email': self.email, 'pwd': self.pwd})
        self.assertEqual(res.status_code, 200)

        data = ujson.loads(self.decode_data(res))
        self.assertIsInstance(data, dict)

        self.assertIn('access_token', data)

        # Exception test
        res = self.json_request(self.client.post, '/auth', data={'email': 'asdf', 'pwd': self.pwd})
        self.assertEqual(res.status_code, 401)

        res = self.json_request(self.client.post, '/auth', data={'email': self.email, 'pwd': 'asdf'})
        self.assertEqual(res.status_code, 401)
