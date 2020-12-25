# -*- coding: utf-8 -*-
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
                       'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(f'{name} => {member} = {member.value}')


@unique
class Weekday(Enum):
    Sun = 7
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


assert Weekday.Mon == Weekday['Mon']
assert Weekday.Mon.value == 1
assert Weekday.Mon == Weekday(1)

try:
    Weekday(0)
except ValueError as e:
    print(e)

try:
    Weekday.Mon = 5
except AttributeError as e:
    print(e)
