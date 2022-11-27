class Rectangle:
    
    def __init__(self, coordinate_1, coordinate_2):
        self.x1 = coordinate_1[0]
        self.y1 = coordinate_1[1]
        self.x2 = coordinate_2[0]
        self.y2 = coordinate_2[1]
    
    def perimeter(self):
        return round(2 * (abs(self.x2 - self.x1) + abs(self.y2 - self.y1)), 2)
    
    def area(self):
        return round(abs(self.x2 - self.x1) * abs(self.y2 - self.y1), 2)
