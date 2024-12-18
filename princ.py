from Point import Point
from FigureGeo import FigureGeo
from Rectangle import Rectangle
from Scene import Scene

p1 = Point(1 , 2)

print("p1 getX =" , p1.getX())
print("p1 getter X =" , p1.x)
p1.x = 2

print("p1 getX=" , p1.getX())

print("p1 =" , p1)

f1= FigureGeo(p1, 3)
print("f1 centre =", f1.centre)
print("f1 color =", f1.color)

print("f1 centre X=" , f1.centre.x)
print("f1 centre X=" , f1.centre.y)

r1 = Rectangle(p1, 4, 2, 5)
print("r1 = ", r1)

maScene = Scene()
print(maScene)
maScene.add(Rectangle)
print(maScene)
