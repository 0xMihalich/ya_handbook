class RedButton:
    
    def __init__(self):
        self.cnt = 0
    
    def click(self):
        self.cnt += 1
        print('Тревога!')
    
    def count(self):
        return self.cnt
