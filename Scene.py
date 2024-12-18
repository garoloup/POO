
from FigureGeo import FigureGeo
from Rectangle import Rectangle

class Scene:

    def __init__(self):
        self._listFigures = []
    
    @property
    def listFigures(self):
        return self._listFigures
    
    @listFigures.setter
    def listFigures(self, lf):
        self._listFigures = lf
    
    def add(self, aFigure: FigureGeo):
        self._listFigures.append(aFigure)

    def __str__(self):
        res = "Scene: "
        for elt in self._listFigures:
            res += str(elt)
        return res

