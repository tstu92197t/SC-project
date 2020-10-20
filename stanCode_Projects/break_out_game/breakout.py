"""
File: breakout.py
Name: Wu Ting

stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

Through this program, we can play a game, Brick Break,
as we click the mouse, the game will be started, and when
we fail for three times, we lose. If we break all of the
bricks, we win.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3
COUNT = 0  # used for counting the bricks' number which have been broke


def main():
    graphics = BreakoutGraphics()
    num_lives = NUM_LIVES
    count = COUNT
    # Add animation loop here!
    while True:
        graphics.ball.move(graphics.getter_dx(), graphics.getter_dy())
        if graphics.ball.x >= graphics.window.width - graphics.ball_radius*2 or graphics.ball.x <= 0:  # hitting left or right border
            graphics.setter_new_dx(-graphics.getter_dx())  # rebound
        if graphics.ball.y <= 0:  # hitting upper border
            graphics.setter_new_dy(-graphics.getter_dy())
        if graphics.ball.y >= graphics.window.height - graphics.ball_radius*2:  # the ball falls out of the bottom window (lose)
            num_lives -= 1
            graphics.reset_ball_position()  # Center a filled ball in the graphical window
        if num_lives == 0:  # when the players fail for three times
            break
        # check the point according to this order: (x, y), (x, y+2r), (x+2r, y), (x+2r, y+2r)
        obj1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        if obj1 is None:
            obj2 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+2*graphics.ball_radius)
            if obj2 is None:
                obj3 = graphics.window.get_object_at(graphics.ball.x + 2 * graphics.ball_radius, graphics.ball.y)
                if obj3 is None:
                    obj4 = graphics.window.get_object_at(graphics.ball.x + 2 * graphics.ball_radius, graphics.ball.y+ 2 * graphics.ball_radius)
                    if obj4 is None:
                        pass
                    else:
                        if obj4 is graphics.paddle:
                            if graphics.getter_dy() >= 0:  # fix the problem of the wrong condition of rebounding
                                graphics.setter_new_dy(-graphics.getter_dy())
                            else:
                                pass
                        else:  # obj4 is a brick
                            graphics.setter_new_dy(-graphics.getter_dy())
                            graphics.window.remove(obj4)
                            count += 1
                else:
                    if obj3 is graphics.paddle:
                        pass
                    else:  # obj3 is a brick
                        graphics.setter_new_dy(-graphics.getter_dy())
                        graphics.window.remove(obj3)
                        count += 1
            else:
                if obj2 is graphics.paddle:
                    if graphics.getter_dy() >= 0:
                        graphics.setter_new_dy(-graphics.getter_dy())
                    else:
                        pass
                else:  # obj2 is a brick
                    graphics.setter_new_dy(-graphics.getter_dy())
                    graphics.window.remove(obj2)
                    count += 1
        else:
            if obj1 is graphics.paddle:
                pass
            else:  # obj1 is a brick
                graphics.setter_new_dy(-graphics.getter_dy())
                graphics.window.remove(obj1)
                count += 1
        if count == graphics.brick_cols*graphics.brick_rows:  # when the player hits all of the bricks
            break

        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
