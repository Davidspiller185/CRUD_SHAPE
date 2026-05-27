from shape import Shape
class Hexagon(Shape):
    def __init__(self, shape_id, shape_type,side):
        super().__init__(shape_id, shape_type)
        self.side=side