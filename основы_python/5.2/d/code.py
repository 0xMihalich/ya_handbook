class Fraction:
    
    def __init__(self, num, denom=None):
        if isinstance(num, str):
            self.num, self.denom = (int(i) for i in num.split('/'))
        else:
            self.num = num
            self.denom = denom
        self.__gcd__()
    
    def __gcd__(self):
        a = self.num
        b = self.denom
        while a != 0 and b != 0:
            if a > b: 
                a = a - b
            else: 
                b = b - a 
        result = max(a, b)
        self.num //= result
        self.denom //= result
    
    def numerator(self, num=None):
        if num:
            self.num = num
            self.__gcd__()
        return self.num
    
    def denominator(self, denom=None):
        if denom:
            self.denom = denom
            self.__gcd__()
        return self.denom
    
    def __str__(self):
        return f'{self.num}/{self.denom}'
    
    def __repr__(self):
        return f'Fraction({self.num}, {self.denom})'
