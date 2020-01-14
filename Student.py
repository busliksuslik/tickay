class Student():
    def __init__(self,name):
        self.__name = name
        self.__secname = ''
        self.__dmg = 1
    def get_name(self):
        print(self.__name)
    def set_name(self,name):
        self.__name = name
    def get_secname(self):
        print(self.__secname)
    def set_secname(self,name):
        self.__secname = name
    def fun (self):
        print("""
    _________________
    | |   ____   |   |
    | |   |   |  |   |
    | |__ |___|  |__ |
    |________________|

    """)
    def pinat (self):
        return(self.__dmg)
class Dog():
    def __init__(self):
        self.hp = 10
    def damage(self, dmg):
        self.hp -=dmg
        if self.hp <=0:
            print('вы убили собаку')
a = Student('')
a.set_secname('kek')
a.get_name()
a.get_secname()
a.set_name('kek')
a.set_secname('lol')
a.get_name()
a.get_secname()
b = Student('Nikita')
b.get_name()
b.fun()
dog = Dog()
for i in range(10):
    dog.damage(b.pinat())
        
    