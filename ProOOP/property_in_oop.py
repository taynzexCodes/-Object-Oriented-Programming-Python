class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    
    @property
    def old(self):
        return self.__old

    
    @old.setter
    def old(self, old):
        self.__old = old


    @old.deleter
    def old(self):
        del self.__old

    # old = property(get_old, set_old) # Автоматический определяет функцию


p = Person('James', 16)
# p.old = 18
# print(p.old)