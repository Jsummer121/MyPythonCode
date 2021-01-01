# -*- coding: utf-8 -*-


class Foo:
    def zero(self):
        pass

    @property
    def one(self):
        return 100

    @property
    def two(self, arg):
        return 100


if __name__ == '__main__':
    fo = Foo()
    fo.zero()
    # fo.one()
    fo.one
    # fo.two
    fo.two(1)
