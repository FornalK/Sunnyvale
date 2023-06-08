from objects.BaseObject import BaseObject


class BaseCreature(BaseObject):
    def __init__(self, x, y,  width, height, type_):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.type_ = type_

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_dimensions(self):
        return self.width, self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def set_dimensions(self, width, height):
        self.width = width
        self.height = height