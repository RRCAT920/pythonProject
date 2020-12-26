# -*- coding: utf-8 -*-
from io import StringIO, BytesIO

f = StringIO('Hello!\nHi!\nGoodbye!')
for line in f.readlines():
    print(line.strip())


f = BytesIO('你好'.encode('utf-8'))
print(f.read().decode('utf-8'))