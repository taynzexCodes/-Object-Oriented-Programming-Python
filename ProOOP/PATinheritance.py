class Geom:  # example 1
    __name = 'GEom'  # u cant apply to this from outside


    def __init__(self, x1, y1, x2, y2):
        print(f'инициализатор Geom для {self.__class__}')
        self.__verify_coord(x1)
        self._x1 = x1  # protected attributes
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._name = self.__name

"""
class Line(Geom):
    def draw(self):
        print("Рисование линии")
"""

class Rect(Geom):


    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self._fill = fill
    
    
    def get_coords(self):
        return (self._x1, self._y1)  #  warns that it is better not to apply from outside


"""
r = Rect(1, 2, 3, 4)
# print(r._x1)  # dont do this better!
r.get_coords()
print(r.__dict__)
"""