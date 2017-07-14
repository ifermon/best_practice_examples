#!/usr/bin/env python3

class MetaFoo(type):
    @property
    def abc(cls):
        return cls._abc

class Foo(object, metaclass=MetaFoo):
    _abc = 6

    @property
    def abc(self):
        return type(self).abc

    @abc.setter
    def abc(self, v):
        Foo._abc = v


f = Foo()
g = Foo()


print(f.abc)
print(g.abc)

f.abc = 5

print(f.abc)
print(g.abc)
