from Common import map_to_coords


class Player:
    def __init__(self, game):
        self.game = game

        self.map = [
            [1,1],
            [1,1]
        ]
        self.coords = map_to_coords(self.map)
        self.distance_to_roof = game.height - len(self.map) + 1

        self.jump_height          = self.distance_to_roof
        self.jump_time_to_peak    = 7
        self.jump_time_to_descent = 5

        self.jump_vel     = ((2 * self.jump_height) / self.jump_time_to_peak) * -1
        self.jump_gravity = ((-2 * self.jump_height) / pow(self.jump_time_to_peak, 2)) * -1
        self.fall_gravity = ((-2 * self.jump_height) / pow(self.jump_time_to_descent, 2)) * -1

        self.pos_x = game.player_offset
        self.pos_y = self.distance_to_roof
        self.orig_pos_y = self.pos_y

        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = True


    def get_gravity(self):
        return self.jump_gravity if self.vel_y < 0 else self.fall_gravity
    
    def start_jump(self):
        if self.on_ground:
            self.vel_y = self.jump_vel
            self.on_ground = False

    # def end_jump(self):
    #     if self.vel_y <= -0.5:
    #         self.vel_y = -0.5
