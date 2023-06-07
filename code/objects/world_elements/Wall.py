from objects.BaseObject import BaseObject


class Wall(BaseObject):
    def __init__(self, x, y, width, height, rotation: bool):
        super().__init__(x, y)
        self.width = width
        self.height = height
        # rotation - True == horizontal, False == Vertical
        self.rotation = rotation

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

    def rotate90(self):
        temp = self.width
        self.width = self.height
        self.height = temp
        self.rotation = not self.rotation

    def get_rotation(self):
        return self.rotation