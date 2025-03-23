# create class with functions for calculating perimeter and area
import math

class Circle:
    def __init__(self, radius:str, operation:str):
        self.radius = radius
        self.operation = operation

    def get_perimeter(self) -> float:
        if self.operation == 'perimeter':
            perimeter = float(self.radius) * 2.0 * math.pi
            return perimeter
    
    def get_area(self) -> float:
        if self.operation == 'area':
            area = float(self.radius)* float(self.radius) * math.pi
            return area