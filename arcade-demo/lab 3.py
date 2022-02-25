import arcade

def draw_muñeco_nieve(x,y):
    arcade.draw_circle_filled(500 + x, 100 + y, 20, arcade.color.WHITE)
    arcade.draw_circle_filled(500 + x, 125 + y, 15, arcade.color.WHITE)
    arcade.draw_circle_filled(495 + x, 127 + y, 3, arcade.color.BLACK)
    arcade.draw_circle_filled(505 + x, 127 + y, 3, arcade.color.BLACK)
    arcade.draw_triangle_filled(500 + x, 123 + y, 500 + x, 118 + y, 520 + x, 120 + y, arcade.color.ORANGE)

def draw_muñeco_nieve_2(x,y):
    arcade.draw_circle_filled(500 + x, 100 + y, 20, arcade.color.WHITE)
    arcade.draw_circle_filled(500 + x, 125 + y, 15, arcade.color.WHITE)
    arcade.draw_circle_filled(495 + x, 127 + y, 3, arcade.color.BLACK)
    arcade.draw_circle_filled(505 + x, 127 + y, 3, arcade.color.BLACK)
    arcade.draw_triangle_filled(500 + x, 123 + y, 500 + x, 118 + y, 480 + x, 120 + y, arcade.color.ORANGE)

def draw_sol(x,y):
    arcade.draw_circle_filled(425 + x, 325 + y, 75, arcade.color.YELLOW)

def draw_nube(x,y):
    arcade.draw_circle_filled(125 + x, 500 + y, 25, arcade.color.WHITE)
    arcade.draw_circle_filled(160 + x, 525 + y, 25, arcade.color.WHITE)
    arcade.draw_circle_filled(160 + x, 475 + y, 25, arcade.color.WHITE)
    arcade.draw_circle_filled(200 + x, 525 + y, 25, arcade.color.WHITE)
    arcade.draw_circle_filled(200 + x, 475 + y, 25, arcade.color.WHITE)
    arcade.draw_circle_filled(235 + x, 500 + y, 25, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(150 + x, 210 + x, 525 + y, 475 + y, arcade.color.WHITE)


def on_draw(delta_time):
    arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

    arcade.start_render()

    draw_sol(0,on_draw.sol2_y + 650)
    on_draw.sol2_y += -1

    draw_sol(0,on_draw.sol1_y - 50)
    on_draw.sol1_y += 1

    draw_nube(on_draw.nube1_x + 250, 0)
    draw_nube(on_draw.nube1_x - 250, 0)
    draw_nube(on_draw.nube1_x - 750, 0)
    on_draw.nube1_x += 1

    arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)

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

    arcade.draw_lrtb_rectangle_filled(720, 730, 225, 200, arcade.color.BROWN)
    arcade.draw_triangle_filled(700, 250, 750, 250, 725, 280, arcade.color.GREEN)
    arcade.draw_triangle_filled(700, 237, 750, 237, 725, 267, arcade.color.GREEN)
    arcade.draw_triangle_filled(700, 225, 750, 225, 725, 255, arcade.color.GREEN)


    draw_muñeco_nieve_2(on_draw.muñeco_nieve_21_x, 50)
    on_draw.muñeco_nieve_21_x -= 1

    draw_muñeco_nieve(on_draw.muñeco_nieve2_x - 300, -50)
    draw_muñeco_nieve(on_draw.muñeco_nieve2_x - 850, 0)
    on_draw.muñeco_nieve2_x += 1

on_draw.muñeco_nieve_21_x = 90
on_draw.muñeco_nieve2_x = 90
on_draw.sol1_y = 90
on_draw.sol2_y = 90
on_draw.nube1_x = 90


def main():
    arcade.open_window(800, 600, "lab 3")
    arcade.schedule(on_draw, 1/60)
    arcade.run()

main()