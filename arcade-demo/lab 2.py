import arcade

arcade.open_window(800, 600, "Drawing Example")
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)

arcade.draw_circle_filled(0, 0, 400, arcade.color.LIGHT_BLUE)
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


arcade.draw_circle_filled(500, 100, 20, arcade.color.WHITE)
arcade.draw_circle_filled(500, 125, 15, arcade.color.WHITE)
arcade.draw_circle_filled(495, 127, 3, arcade.color.BLACK)
arcade.draw_circle_filled(505, 127, 3, arcade.color.BLACK)
arcade.draw_triangle_filled(500, 123, 500, 118, 480, 120, arcade.color.ORANGE)

arcade.draw_circle_filled(125, 500, 25, arcade.color.WHITE)
arcade.draw_circle_filled(160, 525, 25, arcade.color.WHITE)
arcade.draw_circle_filled(160, 475, 25, arcade.color.WHITE)
arcade.draw_circle_filled(200, 525, 25, arcade.color.WHITE)
arcade.draw_circle_filled(200, 475, 25, arcade.color.WHITE)
arcade.draw_circle_filled(235, 500, 25, arcade.color.WHITE)
arcade.draw_lrtb_rectangle_filled(150, 210, 525, 475, arcade.color.WHITE)

arcade.finish_render()
arcade.run()