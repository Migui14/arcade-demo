import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


class Muñeco_nieve:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  20, arcade.color.WHITE)
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y+25,
                                  15, arcade.color.WHITE)
        arcade.draw_circle_filled(self.position_x-5,
                                  self.position_y+27,
                                  3, arcade.color.BLACK)
        arcade.draw_circle_filled(self.position_x+5,
                                  self.position_y+27,
                                  3, arcade.color.BLACK)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x


        # See if the ball hit the edge of the screen. If so, change direction

        if self.position_x < self.radius:

            self.position_x = self.radius



        if self.position_x > SCREEN_WIDTH - self.radius:

            self.position_x = SCREEN_WIDTH - self.radius



        if self.position_y < self.radius:

            self.position_y = self.radius



        if self.position_y > SCREEN_HEIGHT - self.radius:

            self.position_y = SCREEN_HEIGHT - self.radius



class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.muñeco_nieve = Muñeco_nieve(50, 50, 0, 0, 15, arcade.color.AUBURN)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)

        arcade.draw_lrtb_rectangle_filled(0, 800, 600, 200, arcade.color.AIR_SUPERIORITY_BLUE)

        arcade.draw_circle_filled(425, 325, 75, arcade.color.YELLOW)
        arcade.draw_triangle_filled(300, 200, 1000, 200, 700, 500, arcade.color.GRAY)
        arcade.draw_triangle_filled(0, 200, 500, 200, 250, 450, arcade.color.DARK_GRAY)

        arcade.draw_lrtb_rectangle_filled(120, 130, 225, 200, arcade.color.BROWN)
        arcade.draw_triangle_filled(100, 250, 150, 250, 125, 280, arcade.color.GREEN)
        arcade.draw_triangle_filled(100, 237, 150, 237, 125, 267, arcade.color.GREEN)
        arcade.draw_triangle_filled(100, 225, 150, 225, 125, 255, arcade.color.GREEN)

        arcade.draw_lrtb_rectangle_filled(320, 330, 225, 200, arcade.color.BROWN)
        arcade.draw_triangle_filled(300, 250, 350, 250, 325, 280, arcade.color.GREEN)
        arcade.draw_triangle_filled(300, 237, 350, 237, 325, 267, arcade.color.GREEN)
        arcade.draw_triangle_filled(300, 225, 350, 225, 325, 255, arcade.color.GREEN)

        arcade.draw_lrtb_rectangle_filled(520, 530, 225, 200, arcade.color.BROWN)
        arcade.draw_triangle_filled(500, 250, 550, 250, 525, 280, arcade.color.GREEN)
        arcade.draw_triangle_filled(500, 237, 550, 237, 525, 267, arcade.color.GREEN)
        arcade.draw_triangle_filled(500, 225, 550, 225, 525, 255, arcade.color.GREEN)

        arcade.draw_circle_filled(125, 500, 25, arcade.color.WHITE)
        arcade.draw_circle_filled(160, 525, 25, arcade.color.WHITE)
        arcade.draw_circle_filled(160, 475, 25, arcade.color.WHITE)
        arcade.draw_circle_filled(200, 525, 25, arcade.color.WHITE)
        arcade.draw_circle_filled(200, 475, 25, arcade.color.WHITE)
        arcade.draw_circle_filled(235, 500, 25, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_filled(150, 210, 525, 475, arcade.color.WHITE)

        self.muñeco_nieve.draw()

    def update(self, delta_time):
        self.muñeco_nieve.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.muñeco_nieve.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.muñeco_nieve.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.muñeco_nieve.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.muñeco_nieve.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.muñeco_nieve.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.muñeco_nieve.change_y = 0


def main():
    window = MyGame(800, 600, "Drawing Example")
    arcade.run()


main()