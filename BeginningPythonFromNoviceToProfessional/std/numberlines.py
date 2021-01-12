# -*- coding: utf-8 -*-                            #  1
import fileinput                                   #  2
                                                   #  3
for line in fileinput.input(inplace=True):         #  4
    line = line.rstrip()                           #  5
    no = fileinput.lineno()                        #  6
    print(f'{line:<50} # {no:2d}')                 #  7
