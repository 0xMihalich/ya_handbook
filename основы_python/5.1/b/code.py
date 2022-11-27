class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, x, y):
        self.x += x
        self.y += y
    
    def length(self, point):
        return round(((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5, 2)
