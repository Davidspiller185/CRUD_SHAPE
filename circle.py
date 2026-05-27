from shape import Shape
class circle(Shape):
    def __init__(self, shape_id, shape_type,radius):
        super().__init__(shape_id, shape_type)
        self.radius=radius