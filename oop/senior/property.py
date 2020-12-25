# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name, score, birth):
        self._name = name
        self._score = score
        self._birth = birth

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, val):
        if not isinstance(val, int):
            raise ValueError('score must be an integer')
        if val < 0 or val > 100:
            raise ValueError('score must between 0 and 100')
        self._score = val

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, val):
        self._birth = val

    # 只读属性
    @property
    def age(self):
        import datetime
        return datetime.date.today().year - self._birth


s = Student('Jack', 98, 1999)
print(s.age)
try:
    s.age = 100
except AttributeError as e:
    print('Error:', e)
