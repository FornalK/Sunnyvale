from objects.creatures.BaseCreature import BaseCreature


class DynamicCreature(BaseCreature):
    def __init__(self, x, y, width, height, type_, weight, max_speed, acceleration, retardation,jump_start_speed,jump_num):
        super().__init__(x, y, width, height, type_,)
        self.weight = weight
        self.max_speed = max_speed
        self.act_speed = 0
        self.acceleration = acceleration
        self.retardation = retardation
        self.jump_start_speed = jump_start_speed
        self.jump_act_speed = 0
        self.jump_num = jump_num

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