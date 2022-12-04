class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, x, y):
        self.x += x
        self.y += y
    
    def length(self, point):
        return round(((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5, 2)


class PatchedPoint(Point):
    
    def __init__(self, x=0, y=0):
        if isinstance(x, tuple):
            x, y = x
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __repr__(self):
        return f'PatchedPoint({self.x}, {self.y})'
    
    def __add__(self, coordinates):
        x, y = coordinates
        return PatchedPoint(self.x + x, self.y + y)
    
    def __iadd__(self, coordinates):
        x, y = coordinates
        self.x += x
        self.y += y
        return self
