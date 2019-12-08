import math

class Circle:
    def __init__(self, radius = 1.0, color = "red"):
        self.radius = radius
        self.color = color


    def getRadius(self):
        return self.radius


    def setRadius(self, radius):
        self.radius = radius

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def __repr__(self):
        return {"color":self.color, "radius": self.radius}

    def getArea(self):
        return (self.radius**2) *math.pi


circle1 = Circle()
circle2 = Circle(4)
circle3 = Circle(5, "pink")
print(circle2.getColor())
print(circle3.__repr__())
print(circle1.__repr__())
circle1.setColor("green")
circle1.setRadius(6)
print(circle1.__repr__())

class Cylinder (Circle) :
    def __init__(self, height = 1.0):
        super().__init__(radius = 1.0, color = "red")
        self.height = height


    def getHeight(self):
        return self.height

    def setHeight(self, height):
        self.height = height

    def __repr__(self):
        return {"height" : self.height}

    def getVolume(self):
        volume = math.pi* self.radius*2* self.height
        return volume

cylinder1 = Cylinder()
cylinder2 = Cylinder(3)
print(cylinder2.getVolume())




