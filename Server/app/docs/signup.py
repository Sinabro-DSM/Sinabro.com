SIGNUP = {
    'tags': ['계정'],
    'description': '서비스 회원가입 API',
    'parameters': [
        {
            'name': 'email',
            'description': '인증할 이메일 입력',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'pwd',
            'description': '회원가입에 필요한 패스워드',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'name',
            'description': '회원가입에 필요한 이름',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'isAdmin',
            'description': '관리자 확인',
            'in': 'json',
            'type': 'str',
            'required': False
        }
    ]
}
CERTIFY_EMAIL = {
    'tags': ['계정'],
    'description': '이메일 인증 API',
    'parameters': [
        {
            'name': 'certify_uri',
            'description': '이메일로 전송된 인증코드 ',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ]
}