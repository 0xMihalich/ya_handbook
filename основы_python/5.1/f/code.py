# не проходит 20 тест, возможно, ошибка в тестировании, но не точно
class Rectangle:
    
    def __init__(self, coordinate_1, coordinate_2):
        if coordinate_1[0] <= coordinate_2[0]:
            self.x1, self.x2 = coordinate_1[0], coordinate_2[0]
        else:
            self.x1, self.x2 = coordinate_2[0], coordinate_1[0]
        if coordinate_1[1] <= coordinate_2[1]:
            self.y1, self.y2 = coordinate_1[1], coordinate_2[1]
        else:
            self.y1, self.y2 = coordinate_2[1], coordinate_1[1]
        self.x1 = round(self.x1, 2)
        self.x2 = round(self.x2, 2)
        self.y1 = round(self.y1, 2)
        self.y2 = round(self.y2, 2)
    
    def perimeter(self):
        return round(2 * (abs(self.x2 - self.x1) + abs(self.y2 - self.y1)), 2)
    
    def area(self):
        return abs(round((self.x2 - self.x1) * (self.y2 - self.y1), 2))
    
    def get_pos(self):
        return self.x1, self.y2
    
    def get_size(self):
        return round(abs(self.x2 - self.x1), 2), round(abs(self.y2 - self.y1), 2)
    
    def move(self, dx, dy):
        self.x1 = round(self.x1 + dx, 2)
        self.y1 = round(self.y1 + dy, 2)
        self.x2 = round(self.x2 + dx, 2)
        self.y2 = round(self.y2 + dy, 2)
    
    def resize(self, width, height):
        self.x2 = round(self.x1 + width, 2)
        self.y1 = round(self.y2 + height, 2)
