from tests.views import TestBase


class TestAccount(TestBase):
    def setUp(self):
        super(TestAccount, self).setUp()

    def tearDown(self):
        super(TestAccount, self).tearDown()

    def testAccount(self):
        res = self.json_request(self.client.patch, '/change/pwd', data={'current_pw': 'sadasd', 'change_pw': 'qwer'})
        self.assertEqual(res.status_code, 200)

        # Exception test

        res = self.json_request(self.client.patch, '/change/pwd', data={'current_pw': 'qwer', 'change_pw': 'qwer'})
        self.assertEqual(res.status_code, 204)

        res = self.json_request(self.client.patch, '/change/pwd', data={'current_pw': 'dvf', 'change_pw': 'qwer'})
        self.assertEqual(res.status_code, 401)