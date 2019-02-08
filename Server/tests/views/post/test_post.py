from tests.views import TestBase


class TestPost(TestBase):
    def setUp(self):
        super(TestPost, self).setUp()
        self.create_fake_account()
        self.get_tokens()

    def tearDown(self):
        super(TestPost, self).tearDown()

    def testPost(self):
        res = self.client.post('/post', content_type='multipart/form-data', headers={'Authorization': self.access_token},
                               data={
                                   'title': 'this is title',
                                   'content': 'this is content',
                                   'category': 1
                                })
        self.assertEqual(res.status_code, 200)

        res = self.client.get('/post', query_string={'page': 1, 'category': 12})

        self.assertEqual(res.status_code, 200)

        data = res.get_json()
        print(data)
        self.assertIsInstance(data, list)
