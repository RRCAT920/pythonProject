# -*- coding: utf-8 -*-
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f'Student object (name: {self.name})'

    __repr__ = __str__

    def __call__(self, color):
        print(f'My name is {self.name} and my favorite color is {color}')


Student('huzihao')('red')


class Fib:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10_0000:
            raise StopIteration()
        return self.a


for n in Fib():
    print(n)


class FibList:
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for i in range(n):
                a, b = b, a + b
            return a

        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0

            a, b = 1, 1
            lst = []
            for i in range(stop):
                if i >= start:
                    lst.append(a)
                a, b = b, a + b
            return lst


f = FibList()
for i in range(10):
    print(f[i])

print(f[:5])


class Foo:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        if item == 'age':
            return 18
        raise AttributeError(f"'Foo' object has no attribute '{item}'")


f = Foo('bar')
try:
    a = f.abc
except AttributeError:
    print("exed")


# __getattr__
class GithubChain:
    def __init__(self, path='GET '):
        self._path = path

    def __str__(self):
        return self._path

    __repr__ = __str__

    def __getattr__(self, path):
        if path == 'users':
            return lambda username: GithubChain(f"{self._path}/:{username}")
        return GithubChain(f"{self._path}/{path}")


print(GithubChain().users('michael').repos)
