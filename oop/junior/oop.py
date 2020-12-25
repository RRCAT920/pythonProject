# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running')


class Dog(Animal):
    pass


class Timer(object):
    def run(self):
        print('ticking')


def run_twice(runable):
    runable.run()
    runable.run()


animal = Animal()
timer = Timer()
run_twice(animal)
print()
run_twice(timer)
