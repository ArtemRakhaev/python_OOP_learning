class Person:

    def __init__(self, name, old) -> None:
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old
        
    @old.setter
    def old(self, old):
        self.__old = old

    


p = Person("Ivan", 20)
print(p.old)
p.old = 35
print(p.old)

