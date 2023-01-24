import threading
from pynput import keyboard


class Keyboard:
    def __init__(self, game):
        self.game = game
        self.new_press_event = threading.Event()
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def on_press(self, key):
        self.game.player.start_jump()

    def on_release(self, key):
        self.new_press_event.set()
        self.key_pressed = True
        # self.game.player.end_jump()

        # Quit if q is pressed
        if hasattr(key, 'char'):
            if key.char == 'q':
                self.game.stop()
