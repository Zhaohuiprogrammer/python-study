#!/usr/bin/env python3
# _*_coding: utf-8_*_


def not_empty(s):
    return s and s.strip()


print(not_empty("123"))


def _not_divisible(n):
    return lambda x: x % n > 0


print(_not_divisible(2))


def test(x):
    return x % 4 > 0
