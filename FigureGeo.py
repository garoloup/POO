from abc import ABC, abstractmethod
from Point import Point

class FigureGeo:
    def __init__(self, valPoint: Point, color):
        self._centre = valPoint
        self._color = color
    
    @property
    def centre(self):
        return self._centre
    
    @centre.setter
    def centre(self, value: Point):
        print("FigureGeo setter centre with value = " + value)
        self._centre = value

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value):
        print("FigureGeo setter color with value = " + value)
        self._color = value

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass





