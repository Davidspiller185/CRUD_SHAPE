from shape import Shape
class Triangle(Shape):
    def __init__(self, shape_id, shape_type,base,height,side_a,side_b,side_c):
        super().__init__(shape_id, shape_type)
        self.base=base
        self.height=height
        self.side_a=side_a
        self.side_b=side_b
        self.side_c=side_c
