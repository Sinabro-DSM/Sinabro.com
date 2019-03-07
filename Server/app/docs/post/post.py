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

POSTCONTENT_GET = {
    'tags': ['게시물 정보 확인 & 댓글 저장'],
    'descriptions': '등록된 게시물 조작 API',
    'parameters': [
        {
            'name': 'post',
            'description': '게시물 확인',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'comments',
            'description': '게시물 댓글 저장',
            'in': 'json',
            'type': 'str',
            'required': True
        },
    ],
    'responses': {
        '201': {
            'description': '해당 게시물에 댓글저장완료'
        },
        '400': {
            'description': '올바른 접근이 아닙니다. 로그인을 먼저 해주세요'
        }
    }
}

POSTCONTENT_DELETE = {
    'tags': ['게시글 삭제'],
    'descriptions': '등록된 게시물 삭제 API',
    'parameters': [
        {
            'name': 'post',
            'description': '삭제 게시물 확인',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'user',
            'description': '삭제요청자 권한확인',
            'in': 'json',
            'type': 'str',
            'required': True
        },
    ],
    'responses': {
        '201': {
            'description': '해당 게시물 삭제'
        },
        '401': {
            'description': '삭제권한이 없습니다.'
        }
    }
}

POSTCONTENT_PATCH = {
    'tags': ['해당 게시글 업데이트'],
    'descriptions': '등록된 게시물 수정 API',
    'parameters': [
        {
            'name': 'post',
            'description': '수정할 게시물 확인',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'author',
            'description': '수정 요청자 권한확인',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'category',
            'description': '카테고리 확인',
            'in': 'json',
            'type': 'str',
            'required': True
        },
    ],
    'responses': {
        '200': {
            'description': '해당 게시물 업데이트 성공'
        },
        '204': {
            'description': '게시물이 존재하지않음'
        },
        '401': {
            'description': '수정권한 없음'
        }
    }
}