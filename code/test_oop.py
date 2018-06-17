#!/usr/bin/env python3
# _*_coding: utf-8_*_


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name, self.age)


# stone = Student()
# stone.name = "stone"
# stone.age = 2
#
# print(stone.name, stone.age)

stone = Student("stone", 18)
stone.print_info()