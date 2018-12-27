CHANGE_PWD = {
    'tags': ['계정'],
    'description': '비밀번호 변경 API',
    'parameters': [
        {
            'name': 'current_pw',
            'description': '현재 비밀번호',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'change_pw',
            'description': '바꿀 비밀번호',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '비밀번호 변경 완료'
        },
        '204': {
            'description': '현재 비밀번호과 바꿀 비밀번호 일치'
        },
        '401': {
            'description': '현재 비밀번호 인증 실패'
        }
    }
}