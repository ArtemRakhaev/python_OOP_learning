import copy


class Point:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def clone(self):
        return copy.copy(self)


pt = Point(1, 2)
pt_clone = pt.clone()
