class Programmer:
    positions = {'Junior': 10, 'Middle': 15, 'Senior': 20}
    
    def __init__(self, name, position):
        self.name = name
        self.price = self.positions[position]
        self.work_hours = 0
        self.payment = 0
    
    def work(self, time):
        self.work_hours += time
        self.payment += time * self.price
    
    def rise(self):
        if self.price < 20:
            self.price += 5
        else:
            self.price += 1
    
    def info(self):
        return f'{self.name} {self.work_hours}ч. {self.payment}тгр.'
