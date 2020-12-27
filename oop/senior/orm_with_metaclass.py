# -*- coding: utf-8 -*-
"""
使用metaclass实现一个简单ORM框架
Object Relational Mapping: 数据库表对应类，行对应对象
"""
from oop.senior.orm import Model, IntField, StringField


class User(Model):
    id = IntField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


# 创建对象
user = User(id=12345, name='Jack', email='orm@qq.com', password='pwd')
# 保存到数据库
user.save()
