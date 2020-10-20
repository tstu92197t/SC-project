"""
File: breakoutgraphics.py
Name: Wu Ting

stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

we create a class named Breakoutgraphics here by
creating the constructor and several methods such
as paddle_move, start, reset_ball_position, getter
and setter
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.window_width = window_width
        self.window_height = window_height
        self.brick_cols = brick_cols
        self.brick_rows = brick_rows

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2, y= window_height-paddle_offset-paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle)
        self.paddle_offset = paddle_offset
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius, ball_radius, x=window_width/2-ball_radius, y=window_height/2-ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)
        self.ball_radius = ball_radius

        # Default initial velocity for the ball.
        self.__dy = 0
        self.__dx = 0

        # Initialize our mouse listeners.
        onmousemoved(self.paddle_move)
        onmouseclicked(self.start)

        # Draw bricks.
        window_width = brick_cols*brick_width+(brick_cols-1)*brick_spacing

        for i in range(brick_offset, brick_offset+brick_rows*brick_height+(brick_rows-1)*brick_spacing, brick_height+brick_spacing):
            for j in range(0, window_width, brick_width+brick_spacing):
                brick1 = GRect(brick_width, brick_height)
                brick1.filled = True
                if i <= brick_offset+brick_height+brick_spacing:  # the first two rows
                    brick1.fill_color = 'red'
                elif brick_offset+brick_height+brick_spacing < i <= brick_offset+3*(brick_height+brick_spacing):  # the third and forth rows
                    brick1.fill_color = 'orange'
                elif brick_offset+3*(brick_height+brick_spacing) < i <= brick_offset+5*(brick_height+brick_spacing):
                    brick1.fill_color = 'yellow'
                elif brick_offset+5*(brick_height+brick_spacing) < i <= brick_offset+7*(brick_height+brick_spacing):
                    brick1.fill_color = 'green'
                elif brick_offset+7*(brick_height+brick_spacing) < i <= brick_offset+9*(brick_height+brick_spacing):
                    brick1.fill_color = 'blue'
                self.window.add(brick1, x=j, y=i)

    def paddle_move(self, mouse):  # when the mouse move, the paddle will also move
        self.paddle.y = self.window_height-self.paddle_offset
        if mouse.x >= self.window_width-self.paddle_width/2:
            self.paddle.x = self.window_width-self.paddle_width
        elif mouse.x <= self.paddle_width/2:
            self.paddle.x = 0
        else:
            self.paddle.x = mouse.x - self.paddle.width / 2

    def start(self, mouse):  # when we click the mouse, we will see whether the condition is at the initial condition, if yes, then set the value of dx, dy
        if self.__dy == 0 and self.__dx == 0:
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def reset_ball_position(self):
        self.ball.x = self.window_width/2-self.ball_radius
        self.ball.y = self.window_height/2-self.ball_radius
        self.__dy = 0
        self.__dx = 0

    def getter_dx(self):
        return self.__dx

    def getter_dy(self):
        return self.__dy

    def setter_new_dx(self, new_dx):
        self.__dx = new_dx

    def setter_new_dy(self, new_dy):
        self.__dy = new_dy
