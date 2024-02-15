import time

import arcade
import random
__name__ = "__siu__"
a = [random.randint(25, 475),random.randint(25, 475),random.randint(25, 475)]
b = [random.randint(50, 120),random.randint(50, 120),random.randint(50, 120)]
def base(a,b):
    arcade.draw_circle_filled(300,300,30,color=arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(335,300,30,color=arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(265,300,30,color=arcade.color.WHITE_SMOKE)
    arcade.draw_lrtb_rectangle_filled(0,500,280,0,color=arcade.color.BLUE_SAPPHIRE)

    arcade.draw_circle_filled(100,250,30,color=arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(135,250,35,color=arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(65,250,40,color=arcade.color.WHITE_SMOKE)
    arcade.draw_lrtb_rectangle_filled(0,500,230,0,color=arcade.color.BLUE_SAPPHIRE)
    arcade.draw_lrtb_rectangle_filled(0,500,25,0,arcade.color.BUD_GREEN)
    i=0
    while i<=2:

        arcade.draw_lrtb_rectangle_filled(a[i],a[i]+10,b[i]+5,25,color=arcade.color.DARK_OLIVE_GREEN)
        if i==0:
            arcade.draw_circle_filled(a[i]+5,b[i],10,color=arcade.color.WHITE_SMOKE)
        elif i==1:
            arcade.draw_circle_filled(a[i] + 5, b[i], 10, color=arcade.color.RED_DEVIL)
        else:
            arcade.draw_circle_filled(a[i] + 5, b[i], 10, color=arcade.color.VIOLET)
        arcade.draw_triangle_filled(a[i]+5,b[i]-3,a[i]-5,b[i]+10,a[i]+15,b[i]+10,color=arcade.color.BLUE_SAPPHIRE)
        arcade.draw_ellipse_filled(a[i]+20,b[i]/1.2,25,10,arcade.color.DARK_OLIVE_GREEN,tilt_angle=-30)
        arcade.draw_ellipse_filled(a[i]-10,b[i]/1.5,25,10,arcade.color.DARK_OLIVE_GREEN,tilt_angle=30)

        i=i+1
def aleatorio():
    i = 0
    while i < 25:
        a = random.randint(25,170)
        b = random.randint(25,220)

        arcade.draw_rectangle_filled(a,b,3,10,color=arcade.color.BLUE_GREEN)
        i = i+1

    i=0
    while i<25:
        a=random.randint(235,365)
        b=random.randint(25,270)

        arcade.draw_rectangle_filled(a,b,3,10,color=arcade.color.BLUE_GREEN)
        i=i+1


def on_key_press(key,modifiers):
    if key == arcade.key.R:
        start_time = time.time()
        while time.time() - start_time <3:
            arcade.start_render()
            base(a, b)
            aleatorio()
            arcade.finish_render()

    if key == arcade.key.ESCAPE:
        arcade.close_window()


def main():
    arcade.open_window(500, 400, window_title="EJEMPLO")
    arcade.set_background_color(arcade.color.BLUE_SAPPHIRE)

    arcade.get_window().push_handlers(on_key_press)
    arcade.start_render()

    base(a, b)
    aleatorio()
    arcade.finish_render()

    arcade.run()


if __name__ == "__siu__":
    main()
