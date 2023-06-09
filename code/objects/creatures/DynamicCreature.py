from objects.creatures.BaseCreature import BaseCreature


class DynamicCreature(BaseCreature):
    def __init__(self, x, y, width, height, type_, weight, max_speed, acceleration, retardation):
        super().__init__(x, y, width, height, type_,)
        self.weight = weight
        self.max_speed = max_speed
        self.act_speed = 0
        self.acceleration = acceleration
        self.retardation = retardation
        self.move_direction = 0  # 1 = right, -1 = left

    def get_weight(self):
        return self.weight

    def get_max_speed(self):
        return self.max_speed

    def set_weight(self, weight):
        self.weight = weight

    def set_max_speed(self, max_speed):
        self.max_speed = max_speed

    def set_act_speed(self, act_speed):
        self.act_speed = act_speed

    def get_move_direction(self):
        return self.move_direction

    def set_move_direction(self, move_direction):
        self.move_direction = move_direction