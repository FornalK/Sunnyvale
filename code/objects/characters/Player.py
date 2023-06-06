from objects.BaseObject import BaseObject
from key_binds import *


class Player(BaseObject):
    def __init__(self, x, y, width, height, weight, max_speed):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.weight = weight
        self.max_speed = max_speed
        self.act_speed = 0
        self.acceleration = 50
        self.retardation = 250

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


# function which supports horizontal movement of player

    def move_horizontal(self, keys, dt):
        # check if there is A key pressed
        if keys[MOVE_LEFT]:
            # check if player has max speed
            if abs(self.act_speed) < self.max_speed:
                self.act_speed -= self.acceleration * dt
            else:
                self.act_speed = -self.max_speed
        # check if player move in other direction
        else:
            if self.act_speed < 0:
                self.act_speed += self.retardation * dt

        # check if there is D key pressed
        if keys[MOVE_RIGHT]:
            # check if player has max speed
            if abs(self.act_speed) < self.max_speed:
                self.act_speed += self.acceleration * dt
            else:
                self.act_speed = self.max_speed
        # check if player move in other direction
        else:
            if self.act_speed > 0:
                self.act_speed -= self.retardation * dt

        # update player horizontal position
        self.positionx += self.act_speed * dt
