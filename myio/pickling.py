# -*- coding: utf-8 -*-
import json


class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return f'Student object (name: {self.name}, age: {self.age}, score: {self.score}) '


s = Student('Jack', 18, 98)
file = 'student.txt'
with open(file, 'w') as fp:
    json.dump(s, fp, default=lambda o: o.__dict__)

with open(file, 'r') as fp:
    s_unjs = json.load(fp, object_hook=lambda d: Student(d['name'], d['age'],
                                                         d['score']))
    print(s_unjs)
