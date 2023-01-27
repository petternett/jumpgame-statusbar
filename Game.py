from drawille import Canvas, line
from time import sleep, time
from sys import exit
from Player import Player
from Keyboard import Keyboard
from Enemy import Enemy
from Text import img_to_font
from Common import map_to_coords


# TODO hit collision
# TODO mouse input
# TODO high score?
# TODO increase spawn rate of enemies over time
# TODO colors? (see drawille github issues)
# TODO split classes into files
# TODO threading on input (see new_press_event in railway)
class Game:
    def __init__(self):
        self.fps   = 30
        self.delay = 1.0/self.fps

        self.height   = 3
        self.pa_width = 50  # play area width

        self.running    = True
        self.debug_text = None
        self.score      = 0

        self.player_offset = 10
        self.player = Player(self)
        self.kb     = Keyboard(self)
        self.enemies = []


    def debug(self, text):
        self.debug_text = text

    def stop(self):
        self.running = False

    def check_collision(self, player_pos, bar):
        # TODO
        pass

    """
    def draw_ground(self):
        for x,y in line(0, 0, 100, 0):
            yield x, y
    """

    def run(self, stdscr):
        c = Canvas()
        stdscr.refresh()

        # Create font array
        img_arr = img_to_font("font.png")
        m = map_to_coords(img_arr[ord('M')])
        a = map_to_coords(img_arr[ord('A')])
        r = map_to_coords(img_arr[ord('R')])
        i = map_to_coords(img_arr[ord('I')])

        while self.running:

            self.player.vel_y += self.player.get_gravity()
            self.player.pos_y += self.player.vel_y

            if self.player.pos_y > self.player.orig_pos_y:
                self.player.pos_y = self.player.orig_pos_y
                self.player.vel_y = 0
                self.player.on_ground = True

            cur_time = time()

            # TODO increase spawn rate of enemies over time
            # TODO implement random time between enemies (always enough room to avoid)
            if len(self.enemies) == 0:
                self.enemies.append(Enemy(self))


            # Draw "borders"
            c.set(0,0)
            c.set(0,self.height)
            c.set(self.pa_width, self.height)
            c.set(self.pa_width, 0)

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
                
                # If just behind player, +1 score
                if enemy.pos_x == self.player.pos_x-1:
                    self.score += 1

                # If in the middle of PA, spawn enemy
                if enemy.pos_x == (self.pa_width//2):
                    self.enemies.append(Enemy(self))

            # Draw a letter (test)
            test_offs = 20
            for x,y in m:
                c.set(x+test_offs,y)
            test_offs += 4

            for x,y in a:
                c.set(x+test_offs,y)
            test_offs += 4

            for x,y in r:
                c.set(x+test_offs,y)
            test_offs += 4

            for x,y in i:
                c.set(x+test_offs,y)
            test_offs += 4

            for x,y in a:
                c.set(x+test_offs,y)
            test_offs += 4






            # Draw ground, except around player
            # for x,y in line(0, self.height, self.pa_width, self.height):
            #     if x not in range(self.player.pos_x-1, self.player.pos_x+3):
            #         c.set(x,y)

            f = c.frame()+'\n'
            stdscr.addstr(0, 0, f)
            stdscr.addstr(0, ((self.pa_width)//2)+2, f"Score: {self.score}")

            if self.debug_text: stdscr.addstr(0, 0, f"DEBUG: {self.debug_text}")

            # Render
            stdscr.refresh()
            c.clear()

            # Sleep
            sleep(cur_time + self.delay - time())


        exit()
