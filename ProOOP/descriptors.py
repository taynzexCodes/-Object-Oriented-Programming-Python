class Integer:
    
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")
    
    
    def __set_name__(self, owner, name):
        self.name = "_" + name

    
    def __get__(self, instance, owner):
        return getattr(instance, self.name)


    def __set__(self, instance, value):
        self.verify_coord(value)
        setattr(instance, self.name, value)


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()


    def __init__(self, x, y, z):
        self.x = x
        self.z = z
        self.y = y


# p = Point3D(1, 2, 3)
# print(p.__dict__)

# Non-data descriptor

class ReadIntX:
    
    
    def __set_name__(self, owner, name):
        self.name = "x"

    
    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Point4D:
    xr = ReadIntX


    def __init__(self, x, y, z):
        self.x = x
        self.z = z
        self.y = y


# p4 = Point4D(1, 2, 4)
# p4.xr = 5
# print(p4.xr)