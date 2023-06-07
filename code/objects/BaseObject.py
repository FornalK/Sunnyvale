# Represents common features of all objects in game


class BaseObject:
    def __init__(self, x, y):
        # center of the object
        self.positionx = x
        self.positiony = y

    def set_position(self, x, y):
        self.positionx = x
        self.positiony = y

    def set_positionx(self, x):
        self.positionx = x

    def set_positiony(self, y):
        self.positiony = y

    def get_position(self):
        return self.positionx, self.positiony

    def get_positionx(self):
        return self.positionx

    def get_positiony(self):
        return self.positiony
