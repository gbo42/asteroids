import math

# colors
GRAY = (51, 51, 51)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN  = (0, 255, 0)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def copy(self):
        return Vector(self.x, self.y)

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
