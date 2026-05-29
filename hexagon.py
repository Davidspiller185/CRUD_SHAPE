from shape import Shape
from math import sqrt
class Hexagon(Shape):
    def __init__(self, shape_id, shape_type,side):
        super().__init__(shape_id, shape_type)
        self.side=side
    
    def get_area(self):
        area=(3 * sqrt(3) *self.side**2)/2
        return area
    
    def get_perimeter(self):
        perimeter=6 * self.side
        return perimeter
    
    def to_dict(self):
        return {"id":self.id,"type":self.shape_type,"side":self.side,"Area":self.get_area(),"Perimeter":self.get_perimeter()}