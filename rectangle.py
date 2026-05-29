from shape import Shape
class Rectangle(Shape):
    def __init__(self, shape_id, shape_type,width,height):
        super().__init__(shape_id, shape_type)
        self.width=width
        self.height=height

    def get_area(self):
        area=self.width *self.height
        return area
    
    def get_perimeter(self):
        perimeter= 2 * (self.width + self.height)
        return perimeter
    def to_dict(self):
        return {"id":self.id,"type":self.shape_type,"width":self.width,"heigt":self.height,"area":self.get_area(),"perimeter":self.get_perimeter()}