AUTH = {
    'tags': ['계정'],
    'description': '서비스 로그인 API',
    'parameters': [
        {
            'name': 'email',
            'description': '로그인 할 이메일',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'pwd',
            'description': '로그인 할 패스워드',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ]
}

