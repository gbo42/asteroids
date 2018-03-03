import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norm(self):
        m = math.sqrt(self.x * self.x + self.y * self.y)
        self.x /= m
        self.y /= m
        return self

def mapFromTo(x,a,b,c,d):
   y=(x-a)/(b-a)*(d-c)+c
   return y

def polarToCart(tetha, r):
    x = r * math.cos(tetha)
    y = r * math.sin(tetha)
    return Vector(x, y)
