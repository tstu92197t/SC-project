"""
File: bouncing_ball.py
Name: Wu Ting
-------------------------
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce reduces
y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
VY = 0

# the global variable
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
count = 3


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(ball)
    onmouseclicked(start)


def start(mouse):
    global REDUCE, VY, ball, count
    if count != 0:
        while True:
            ball.move(VX, VY+GRAVITY)
            VY += GRAVITY
            pause(DELAY)
            if ball.y >= window.height - SIZE:  # hitting the ground
                VY = VY*REDUCE
                if VY > 0:  # making the direction while bouncing back correct
                    VY = -VY
            if ball.x >= window.width:  # out of the window
                break
        ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
        ball.filled = True
        window.add(ball)
        count -= 1
    else:
        pass






if __name__ == "__main__":
    main()
