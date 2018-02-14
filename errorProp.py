"""
Class for a data value which also handles error propogation
By Kadin Tucker
"""

class ErrVal():
    def __init__(self, value, error):
        self.value = value
        self.error = error #+/- value, should always be positive
        
    def __add__(self, other):
        return ErrVal(self.value + other.value, self.error + other.error)
    
    def __sub__(self, other):
        return ErrVal(self.value - other.value, self.error - other.error)
    
    def __mul__(self, other):
        return ErrVal(self.value * other.value, 
            ((self.error / self.value) + (other.error / other.value)) * (self.value * other.value))
        
    def __truediv__(self, other):
        return ErrVal(self.value / other.value, 
            ((self.error / self.value) + (other.error / other.value)) * (self.value / other.value))
    
    def __str__(self):
        return str(self.value) + " +/- " + str(self.error)
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __le__(self, other):
        return self.value <= other.value
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __ge__(self, other):
        return self.value >= other.value