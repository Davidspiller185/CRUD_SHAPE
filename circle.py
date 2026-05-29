from shape import Shape
class Circle(Shape):
    def __init__(self, shape_id, shape_type,radius):
        super().__init__(shape_id, shape_type)
        self.radius=radius

    def get_area(self):
        area=3.14 * self.radius**2
        return area
    
    def get_perimeter(self):
        perimeter=2 * 3.14 * self.radius
        return perimeter
    
    def to_dict(self):
        return {"id":self.id,"type":self.shape_type,"radius":self.radius,"Area":self.get_area(),"perimeter":self.get_perimeter()}