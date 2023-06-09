from objects.creatures.DynamicCreature import DynamicCreature
from key_binds import *
from settings import *


class Player(DynamicCreature):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_WIDTH, PLAYER_HEIGHT, TYPE_PLAYER, PLAYER_WEIGHT,
                         PLAYER_MAX_SPEED, PLAYER_ACCELERATION, PLAYER_RETARDATION)
        self.in_air = False
        self.after_jump = False

    def get_in_air(self):
        return self.in_air

    def change_in_air(self):
        self.in_air = not self.in_air

    def get_after_jump(self):
        return self.after_jump

    def change_after_jump(self):
        self.after_jump = not self.after_jump

    # function which supports horizontal movement of player
    def move_horizontal(self, keys, dt):
        flag = True
        # check if there is A key pressed
        if keys[MOVE_LEFT]:
            self.move_direction = -1
            flag = False
        if keys[MOVE_RIGHT]:
            self.move_direction = 1
            flag = False

        # check if player has max speed
        if abs(self.act_speed) < self.max_speed:
            self.act_speed += self.move_direction * self.acceleration * dt
        else:
            self.act_speed = self.move_direction * self.max_speed

        # check if player move in other direction
        if flag:
            if self.act_speed < 0:
                self.act_speed += self.retardation * dt
            if self.act_speed > 0:
                self.act_speed -= self.retardation * dt

        # update player horizontal position
        self.positionx += self.act_speed * dt

    # TODO: Do usunięcia po implementacji skoku
    # a method that trivially implements gravity
    def fall(self, keys):
        if not keys[JUMP]:
            self.positiony += 0.5

    # a method that trivially implements lifting
    def fly(self):
        self.positiony -= 0.25
        self.in_air = True
        # self.after_jump = True

    def move_up(self, keys):
        # check if there is SPACE key pressed
        if keys[JUMP]:
            self.fly()