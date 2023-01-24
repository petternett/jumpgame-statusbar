from drawille import Canvas, line
from time import sleep, time
from sys import exit
from Player import Player
from Keyboard import Keyboard
from Enemy import Enemy


class Game:
    def __init__(self):
        self.fps   = 30
        self.delay = 1.0 / self.fps

        self.height = 3  # 3
        self.width = 50

        self.running = True
        self.debug_text = None
        self.player_offset = 10

        self.player = Player(self)
        self.enemies = []
        self.kb = Keyboard(self)


    def debug(self, text):
        self.debug_text = text

    def stop(self):
        self.running = False

    def check_collision(self, player_pos, bar):
        pass

    """
    def draw_ground(self):
        for x,y in line(0, 0, 100, 0):
            yield x, y
    """

    def run(self, stdscr):
        c = Canvas()
        stdscr.refresh()

        while self.running:

            self.player.vel_y += self.player.get_gravity()
            self.player.pos_y += self.player.vel_y

            if self.player.pos_y > self.player.orig_pos_y:
                self.player.pos_y = self.player.orig_pos_y
                self.player.vel_y = 0
                self.player.on_ground = True

            cur_time = time()

            if len(self.enemies) == 0:
                self.enemies.append(Enemy(self))


            # Draw "borders"
            c.set(0,0)
            c.set(0,self.height)
            c.set(self.width, self.height)
            c.set(self.width, 0)

            # Draw player
            for x,y in self.player.coords:
                c.set(x+self.player.pos_x,y+self.player.pos_y)

            # Draw enemies
            for enemy in self.enemies:
                for x,y in enemy.coords:
                    c.set(x+enemy.pos_x,y+enemy.pos_y)

                # Remove enemy when out of frame
                enemy.pos_x -= 1
                if enemy.pos_x <= 0:
                    self.enemies.remove(enemy)


            # Draw ground, except around player
            # for x,y in line(0, self.height, self.width, self.height):
            #     if x not in range(self.player.pos_x-1, self.player.pos_x+3):
            #         c.set(x,y)

            f = c.frame()+'\n'
            stdscr.addstr(0, 0, f)

            if self.debug_text: stdscr.addstr(0, 0, f"DEBUG: {self.debug_text}")

            # Render
            stdscr.refresh()
            c.clear()

            # Sleep
            sleep(cur_time + self.delay - time())


        exit()
