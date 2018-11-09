from functools import wraps
import gzip
import ujson

import time
from werkzeug.exceptions import HTTPException
from flask import jsonify, after_this_request, request, abort, Response
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.account import AccountModel
from flask_restful import Resource


def after_request(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'deny'

    return response


def exception_handler(e):
    print(e)

    if isinstance(e, HTTPException):
        description = e.description
        code = e.code

    else:
        description = ''
        code = 500

    return jsonify({
        'msg': description
    }), code


def gzip(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        @after_this_request
        def zipper(response):
            if 'gzip' not in request.headers.get('Accept-Encoding', '') \
                    or not 200 <= response.status_code < 300 \
                    or 'Content-Encoding' in response.headers:
                return response

            response.data = gzip.compress(response.data)
            response.headers.update({
                'Content-Encoding': 'gzip',
                'Vary': 'Accept-Encoding',
                'Content-Length': len(response.data)
            })
            return response

        return fn(*args, **kwargs)

    return wrapper


def auth_required(fn):
    @wraps(fn)
    @jwt_required
    def wrapper(*args, **kwargs):
        user = AccountModel.objects(id=get_jwt_identity()).first()
        if not user:
            abort(403)
        return fn(*args, **kwargs)

    return wrapper


def json_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not request.is_json:
            abort(406)
        return fn(*args, **kwargs)

    return wrapper


class BaseResource(Resource):
    def __init__(self):
        self.now = time.strftime('%Y-%m-%d %H:%M:%S')

    @classmethod
    def unicode_safe_json_response(cls, data, status_code=200):
        return Response(
            ujson.dumps(data, ensure_ascii=False),
            status_code,
            content_type='application/json; charset=utf8'
        )


class Router(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        pass