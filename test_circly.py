# create class with functions for calculating perimeter and area
import math
import pytest 
from circle import Circle
        
class test_Circle:         
    def test_get_perimeter(self):
        Cc = Circle()
        assert Cc.get_perimeter(0) == 0, "A circle without a radius of zero cannot have a perimeter."
        assert Cc.get_perimeter(1) == 2*math.pi, "A circle without a radius of one, has a perimeter of 2 times pi."
        assert Cc.get_perimeter(1) == 20*math.pi, "A circle without a radius of ten, has a perimeter of 20 times pi."

    def test_get_area(self):
        Cc = Circle()
        assert Cc.get_area(0) == 0, "A circle without a radius of zero cannot have a area." 
        assert Cc.get_area(1) == math.pi, "A circle without a radius of one, has an area of pi." 
        assert Cc.get_area(10) == 100*math.pi, "A circle without a radius of ten, has an area of 100 times pi." 

