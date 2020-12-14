# -*- coding: utf-8 -*-
from collections import namedtuple

circle_model = namedtuple("Circle", ["x", "y", "r"])

c1 = circle_model(1, 2, 3)
c2 = circle_model(2, 3, 4)
print(c1)  # Circle(x=1, y=2, r=3)
print(c2.x, c2.y, c2.r, sep="  |  ")  # 2  |  3  |  4
print(c2.__doc__)  # Circle(x, y, r)


users_message = [
    ("summer",20,"www.123@qq.com"),
    ("july",20,"www.12@qq.com"),
    ("lixi",20,"www.1251@qq.com")
]

page_info = namedtuple("user_messages",["name","age","email"])
for User in users_message:
    user = page_info(*User)
    print(user)
# user_messages(name='summer', age=20, email='www.123@qq.com')
# user_messages(name='july', age=20, email='www.12@qq.com')
# user_messages(name='lixi', age=20, email='www.1251@qq.com')

# namedtuple("winter",["first","last"])
# year1 = winter(9,12)
# print(year1)  # NameError: name 'winter' is not defined
