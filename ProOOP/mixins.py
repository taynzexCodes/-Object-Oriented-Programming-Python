class Items:
    def __init__(self, name, weight, price):
        super().__init__()
        print("init Good")
        self.name = name
        self.weight = weight
        self.price = price

    
    def print_info(self):
        print(f'{self.name}, {self.weight}, {self.price}')


class MixinLog:
    ID = 0

    def __init__(self):
        super().__init__()
        print("init MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID


    def save_sell_log(self):
        print(f'{self.id}: товар был продан в 00:00 часов')


class MixinLog2:
    def __init__(self):
        super().__init__()
        print("init MixinLog 2")


class NoteBook(Items, MixinLog):
    pass


"""
n = NoteBook("MacBook", 1.5, 50000)
n.print_info()
n.save_sell_log()
print(NoteBook.__mro__)
"""