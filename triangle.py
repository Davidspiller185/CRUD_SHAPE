from shape import Shape
class Triangle(Shape):
    def __init__(self, shape_id, shape_type,base,height,side_a,side_b,side_c):
        super().__init__(shape_id, shape_type)
        self.base=base
        self.height=height
        self.side_a=side_a
        self.side_b=side_b
        self.side_c=side_c
    def get_area(self):
        area=(self.base * self.height)
        return area
    def get_perimeter(self):
        perimeter=self.side_a + self.side_b + self.side_c
        return perimeter
    def to_dict(self):
        return {"id":self.id,"type":self.shape_type,"base":self.base,"heigt":self.height,"side_a":self.side_a,"side_b":self.side_b,"side_c":self.side_c,"area":self.get_area(),"perimeter":self.get_perimeter()}
