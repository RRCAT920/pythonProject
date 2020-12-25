# -*- coding: utf-8 -*-
class Student(object):
    __slots__ = 'name', 'age'


s = Student()
s.name = 'Jack'
s.age = 12
try:
    s.score = 98
except AttributeError as e:
    print("Error:", e)


class GraduateStudent(Student):
    __slots__ = 'score'


g = GraduateStudent()
g.score = 2
print(g.score)
g.name = 'hello0'
print(g.name)
