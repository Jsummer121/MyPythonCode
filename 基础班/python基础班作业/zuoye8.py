# -*- coding: utf-8 -*-

class long:
    def __init__(self,long,width):
        self.long = long
        self.width = width

    def area(self):
        area = self.long * self.width
        return area

long = long(5,6)
area = long.area()
print(area)
