# -*- coding: utf-8 -*-
# WSGI 处理函数
def hello(environ, resp_fn):
    resp_fn('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello!</h1>']
