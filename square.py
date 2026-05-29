from shape import Shape
class Square(Shape):
    def __init__(self, shape_id, shape_type,side):
        super().__init__(shape_id, shape_type)
        self.side=side
    def get_area(self):
        area=self.side * self.side
        return area
    def get_perimeter(self):
        perimeter=4 * self.side
        return perimeter
    
    def to_dict(self):
        return {"id":self.id,"type":self.shape_type,"side":self.side,"area":self.get_area(),"perimeter":self.get_perimeter()}