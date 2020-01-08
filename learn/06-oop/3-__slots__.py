"""
python 允许为对象动态设置属性(也就是原本类中并未声明，使用时给对象动态设置一个属性)
__slots__可以限制设置哪些属性
"""
class Person(object):

    # 限定Person对象只能动态设置_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 22)
    person.play()
    #为person对象动态设置_gender属性，由于声明时__slots__放开了该属性，所以可以设置
    person._gender = '男'
    # AttributeError: 'Person' object has no attribute '_is_gay'
    #该属性没有放开 所以设置会抛异常
    # person._is_gay = True