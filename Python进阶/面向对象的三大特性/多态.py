# -*- coding: utf-8 -*-


class Animal:
    def call(self):
        print("汪汪汪")


class Cat(Animal):
    def call(self):
        print("喵喵喵")


class Dog(Animal):
    pass


class Bird(Animal):
    def call(self):
        print("唧唧唧")


if __name__ == '__main__':
    cat = Cat()
    bird = Bird()
    dog = Dog()
    cat.call()
    bird.call()
    dog.call()
