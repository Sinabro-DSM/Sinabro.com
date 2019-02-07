from tests.views import TestBase
import ujson


class TestPost(TestBase):
    def setUp(self):
        super(TestPost, self).setUp()

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

        res = self.request(self.client.get, '/post', query_string={'page': 1, 'category': 12})

        self.assertEqual(res.status_code, 200)

        data = ujson.loads(self.decode_data(res))
        self.assertIsInstance(data, list)
        post = data[0][0]
