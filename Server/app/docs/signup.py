from app.views.user.signup import Signup

Signup = {
    'tags': ['계정'],
    'description': '회원가입 이메일 인증 전 정보입력.',
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