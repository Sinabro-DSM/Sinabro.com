from tests.views import TestBase


class TestComment(TestBase):
    def setUp(self):
        super(TestComment, self).setUp()
        self.create_fake_account()
        self.get_tokens()
        self.create_fake_category()
        self.create_fake_post()

    def tearDown(self):
        super(TestComment, self).tearDown()

    def testComment(self):
        res = self.json_request(self.client.post, '/post/{0}/comment'.format(self.post_id), token=self.access_token,
                                data={'content': 'this is test'})
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertIn('comment_id', data)

        self.comment_id = data['comment_id']

        res = self.json_request(self.client.patch, '/post/{0}/comment/{1}'.format(self.post_id, self.comment_id),
                                token=self.access_token, data={'content': 'patched content'})

        self.assertEqual(res.status_code, 200)

        res = self.client.delete('/post/{0}/comment/{1}'.format(self.post_id, self.comment_id),
                                 headers={'Authorization': self.access_token})
        self.assertEqual(res.status_code, 200)
