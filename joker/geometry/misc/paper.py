#!/usr/bin/env python3
# coding: utf-8

import math


def conv_mm_to_inch(val: float):
    return val / 25.4


class StandardPaperSize:
    __slots__ = ['width']
    sqrt2 = math.sqrt(2)

    def __init__(self, width: float = None):
        width = width or 840.8964152537146
        self.width = width

    @property
    def length(self):
        return self.width * self.sqrt2

    def pair(self, ndigits=64):
        width = self.width
        length = self.width * self.sqrt2
        if ndigits == 64:
            return width, length
        return round(width, ndigits), round(length, ndigits)

    def bisect(self, repeat: int = 1):
        r = self.sqrt2 ** repeat
        return self.__class__(self.width / r)

    def __repr__(self):
        cn = self.__class__.__name__
        return f'{cn}({self.width})'

    def __str__(self):
        width, length = self.pair(3)
        return f'{width}x{length}'

    @classmethod
    def a_series_mm(cls, n: int = 0):
        return cls().bisect(n)

    @classmethod
    def a_series_cm(cls, n: int = 0):
        return cls(84.08964152537146).bisect(n)

    @classmethod
    def a_series_inch(cls, n: int = 0):
        return cls(33.10615808085491).bisect(n)

    @classmethod
    def b_series_mm(cls, n: int = 0):
        return cls(1000.).bisect(n)

    @classmethod
    def b_series_cm(cls, n: int = 0):
        return cls(100.).bisect(n)

    @classmethod
    def b_series_inch(cls, n: int = 0):
        return cls(39.37007874015748).bisect(n)

    @classmethod
    def c_series_mm(cls, n: int = 0):
        return cls(917.0040432046713).bisect(n)

    @classmethod
    def c_series_cm(cls, n: int = 0):
        return cls(91.70040432046713).bisect(n)

    @classmethod
    def c_series_inch(cls, n: int = 0):
        return cls(36.102521386010686).bisect(n)
