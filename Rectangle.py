from FigureGeo import FigureGeo
import Point

class Rectangle(FigureGeo):
    def __init__(self, valPoint: Point, color, valLong: int, valLarg: int):
        super().__init__(valPoint, color)
        self._length = valLong
        self._width = valLarg

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value: int):
        print("Rectangle setter length with value = " + value)
        self._length = value


    @property
    def width(self):
        return self._width

    @length.setter
    def width(self, value: int):
        print("Rectangle setter width with value = " + value)
        self.width = value
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return (self.length + self.width) * 2

    def __rep__(self):
        # return "Type Rectangle " + str(type(self)) + str(super()) + " length=" + self.length + " width=" + self.width
        typeR = str(type(self))
        stc = str(self.centre)
        return "Type : "+ typeR +" centre= " + stc + " color=" + str(self.color) + " length=" + str(self.length) + " width=" + str(self.width)

    def __str__(self):
        # return "Type Rectangle " + str(type(self)) + str(super()) + " length=" + self.length + " width=" + self.width
        typeR = str(type(self))
        stc = str(self.centre)
        return "Type : "+ typeR +" centre= " + stc + " color=" + str(self.color) + " length=" + str(self.length) + " width=" + str(self.width)

