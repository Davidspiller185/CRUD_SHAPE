from shape import Shape
class Rectangle(Shape):
    def __init__(self, shape_id, shape_type,width,height):
        super().__init__(shape_id, shape_type)
        self.width=width
        self.height=height