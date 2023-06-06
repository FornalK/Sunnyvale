from objects.BaseObject import BaseObject


class Player(BaseObject):
    def __init__(self, x, y, width, height, weight, max_speed):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.weight = weight
        self.max_speed = max_speed

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_max_speed(self):
        return self.max_speed

    def get_dimensions(self):
        return self.width, self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def set_weight(self, weight):
        self.weight = weight

    def set_max_speed(self, max_speed):
        self.max_speed = max_speed

    def set_dimensions(self, width, height):
        self.width = width
        self.height = height