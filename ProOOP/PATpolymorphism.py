
class Geom:
    def get_pr(self):
        raise NotImplementedError("В дочернем классе должен быть переопределен метод get_pr()")


class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    
    def get_pr(self):
        return 2*(self.w+self.h)

    
class Square(Geom):
    def __init__(self, a):
        self.a = a


    def get_pr(self):
        return 4*self.a


class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    
    def get_pr(self):
        return self.a + self.b + self.c


geom = [Square(10), Rectangle(1, 2), Triangle(1, 2, 3)]
# for g in geom:
#    print(g.get_pr())
