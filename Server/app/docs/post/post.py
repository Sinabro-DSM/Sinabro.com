POST = {
    'tags': ['게시물'],
    'description': '블로그 게시물 등록 API',
    'parameters': [
        {
            'name': 'content',
            'description': '게시물의 종류',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'title',
            'description': '게시물의 제목',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'images',
            'description': '게시물의 이미지',
            'in': 'json',
            'type': 'str',
            'required': False
        },
        {
            'name': 'category_int',
            'description': '게시물의 분류기준',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'get',
            'description': '원하는 게시물 정보보기',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '게시물등록완료'
        },
        '400': {
            'description': '올바른 접근이 아닙니다. 로그인을 먼저 해주세요'
        }
    }
}

POSTCONTENT = {
    'tags': ['게시물'],
    'descriptions': '등록된 게시물 조작 & 댓글 조작 API',
    'parameters': [
        {
            'name': 'comment',
            'description': '게시물에 등록할 댓글',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'author',
            'description': '게시물 및 댓글의 주인',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'delete',
            'description': '게시물 삭제',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'patch',
            'description': '게시물 수정',
            'in': 'json',
            'type': 'str',
            'required': True
        },
    ],
    'responses': {
        '201': {
            'description': '게시물 수정 완료'
        },
        '401': {
            'description': '게시물 조작 권한이 없습니다.'
        }
    }
}