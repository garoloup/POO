
class Point:
    def __init__(self, valx, valy):
        self._x = valx
        self._y = valy
    
    @property
    def x(self):
        return self._x

    
    @property
    def y(self):
        return self._y
    
    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value

    def getX(self):
        return self._x
    
    def __str__(self):
        return "("+str(self.x) + ", " + str(self.y) + ")"

