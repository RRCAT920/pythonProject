# -*- coding: utf-8 -*-

class Animal:
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class RunnableMixIn:
    def run(self):
        print('Running')


class FlyableMixIn:
    def fly(self):
        print('Flying')


class Dog(Mammal, RunnableMixIn):
    pass


class Bat(Mammal, FlyableMixIn):
    pass
