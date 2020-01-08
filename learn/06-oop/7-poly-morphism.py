"""
多态：多态有多种解释以及说法，继承也是多态的表现形式之一，将子类实例赋给父类类型通常被认定为多态。
调用方法时如果子类重写了父类方法则会调用子类中的方法，这种行为被称为虚拟调用。
如果有多个子类重写了父类方法，实例不同子类时会有不同的表现形式，也为多态。
"""
from abc import ABCMeta, abstractmethod

#python不像Java中有抽象类关键字，
#可以通过abc模块的ABCMeta元类和abstractmethod包装器来达到抽象类的效果，
# 如果一个类中存在抽象方法那么这个类就不能够实例化
class Pet(object, metaclass=ABCMeta):
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname

    #抽象方法，声明时不予实现，在子类中实现
    #含有抽象方法的类即为抽象类，则不能被实例化
    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()