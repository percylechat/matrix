from typing import Union, overload
import math


class Vector:
    # def __init__(self):
    #     self.components = []

    # @overload
    def __init__(self, components: list):
        self.components = []
        for el in components:
            self.components.append(el)

    # @overload
    # def __init__(self, other: Vector):
    #     self.components = []
    #     for el in other.components:
    #         self.components.append(el)

    def printable(self):
        print(self.components)

    def comp_size(self, other):
        if len(self.components) != len(other.components):
            return False
        return True

    def add(self, other):
        if not isinstance(other, Vector):
            return None
        if len(self.components) != len(other.components):
            return None
        new = []
        for i in range(len(self.components)):
            new.append(self.components[i] + other.components[i])
        self.components = new
        return self

    def sub(self, other):
        if not isinstance(other, Vector):
            return None
        if len(self.components) != len(other.components):
            return None
        new = []
        for i in range(len(self.components)):
            new.append(self.components[i] - other.components[i])
        self.components = new
        return self

    def scl(self, other):
        new = []
        for i in range(len(self.components)):
            new.append(self.components[i] * other)
        self.components = new
        return self

    def dot(self, other):
        if not isinstance(other, Vector):
            return None
        if not self.comp_size(other):
            return None
        temp = []
        for index in range(len(self.components)):
            temp.append(self.components[index] * other.components[index])
        res = 0
        for index in range(len(self.components)):
            res += temp[index]
        return res

    # is sum of absolute values
    # dumb way to het absolute value for neg numbers but oh well
    def norm1(self):
        res = 0
        for index in range(len(self.components)):
            if self.components[index] < 0:
                res += -self.components[index]
            else:
                res += self.components[index]
        return res

    # all values squared and then square rooted result
    def norm(self):
        res = 0
        for index in range(len(self.components)):
            res += self.components[index] * self.components[index]
        return math.sqrt(res)

    # biggest absolut value of vector
    def norm_inf(self):
        res = 0
        for el in self.components:
            if el < 0:
                if -el > res:
                    res = -el
            else:
                if el > res:
                    res = el
        return res
