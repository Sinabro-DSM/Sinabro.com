from tests.views import TestBase


class TestPost(TestBase):
    def setUp(self):
        super(TestPost, self).setUp()
        self.create_fake_account()
        self.get_tokens()
        self.create_fake_category()

    def tearDown(self):
        super(TestPost, self).tearDown()

    def testPost(self):
        res = self.client.post('/post', content_type='multipart/form-data', headers={'Authorization': self.access_token},
                               data={
                                   'title': self.title,
                                   'content': self.content,
                                   'category': self.category_id
                                })
        self.post_id = res.json['post_id']

        self.assertEqual(res.status_code, 200)

        res = self.client.get('/post', query_string={'page': 1, 'category': 1})

        self.assertEqual(res.status_code, 200)

        data = res.get_json()
        self.assertIsInstance(data, list)
        self.assertIsInstance(data[0], dict)
        self.assertIn('author', data[0])
        self.assertIn('reaction', data[0])

        #/post/<post_id>
        res = self.client.get('/post/{0}'.format(self.post_id))
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertIsInstance(data, dict)
        self.assertIn('post_id', data)
        self.assertIn('comments', data)
        self.assertIn('images', data)
        self.assertIsInstance(data['images'], list)

        res = self.client.patch('/post/{0}'.format(self.post_id), headers={'Authorization': self.access_token},
                                content_type='multipart/form-data',
                                data={
                                    'title': 'it is changed title',
                                    'content': 'it is changed content',
                                    'category': 1
                                })
        self.assertEqual(res.status_code, 200)

        res = self.client.delete('/post/{0}'.format(self.post_id), headers={'Authorization': self.access_token})
        self.assertEqual(res.status_code, 200)



