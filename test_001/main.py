import arcade
import csv
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"

FRAMETIME =0.005

PIX_PER_METER = SCREEN_HEIGHT / 2.0

FLOOR_HEIGHT = 20.0
LABDA_RADIUS = 10.0

COLL_CENTER = FLOOR_HEIGHT + LABDA_RADIUS

acceleration = -9.81 * PIX_PER_METER

class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """
    yPos = SCREEN_HEIGHT * 0.5
    yVel = 0.0
    prev_yPos = yPos
    prev_yVel = yVel

    def updateVelocity(self, DT:float):
        self.prev_yVel = self.yVel
        self.yVel += DT * acceleration

    def updatePosition(self, DT:float):
        self.prev_yPos = self.yPos
        self.yPos += DT * self.yVel

        if self.yPos < COLL_CENTER:
            self.yVel = -1.0 * self.prev_yVel
            self.yPos = COLL_CENTER + math.fabs(self.yPos - COLL_CENTER)


    def __init__(self, width, height, title):
        super().__init__(width, height, title, update_rate=FRAMETIME, vsync=False)

        arcade.set_background_color(arcade.color.DARK_BLUE)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        self.yPos = SCREEN_HEIGHT * 0.5
        self.yVel = 0.0

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        # Call draw() on all your sprite lists below
        arcade.draw_circle_filled(center_x=SCREEN_WIDTH*0.5, center_y=self.yPos, radius=LABDA_RADIUS, color=arcade.color.ALMOND)
        arcade.draw_line(start_x=0, start_y=FLOOR_HEIGHT, end_x=SCREEN_WIDTH, end_y=FLOOR_HEIGHT, color=arcade.color.AMARANTH)
        arcade.draw_line(start_x=0, start_y=SCREEN_HEIGHT * 0.5, end_x=SCREEN_WIDTH, end_y=SCREEN_HEIGHT * 0.5, color=arcade.color.BLUE_GRAY)

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.updateVelocity(DT=delta_time)
        self.updatePosition(DT=delta_time)        
        print(f"{delta_time}\t\t{self.yPos}\t\t{self.yVel}")

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main function """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()