# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print(f"{self.__name}:{self.__score}")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        

std = Student('a', 92)
