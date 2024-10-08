class Person(object):

    # 动态添加，限定Person对象只能绑定_name, _age和_gender属性
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
            print('gender = %s' % self._gender)
        else:
            print('%s正在玩斗地主.' % self._name)
            print('gender = %s' % self._gender)


def main():
    person = Person('王大锤', 22)
    person._gender = '男'
    person.play()
    # AttributeError: 'Person' object has no attribute '_is_gay'
    # person._is_gay = True

if __name__ == '__main__':
        main()