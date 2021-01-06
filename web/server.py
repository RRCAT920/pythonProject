# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server
import app


server = make_server('', 8080, app.hello)
server.serve_forever()