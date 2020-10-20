"""
File: draw_line.py
Name: Wu Ting
-------------------------
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line appears
at the condition where the circle disappears as the user clicks
on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# constant
SIZE = 10

# global variable
window = GWindow()
count = 1
first_mouse_x = 0
first_mouse_y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(mouse):
    global count, first_mouse_x, first_mouse_y
    if count % 2 == 1:  # the first click
        oval = GOval(SIZE, SIZE, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
        oval.filled = True
        oval.fill_color = 'white'
        window.add(oval)
        count += 1
        first_mouse_x = mouse.x  # the x value of the first click
        first_mouse_y = mouse.y  # the y value of the first click
    else:  # the second click
        first_oval = window.get_object_at(first_mouse_x, first_mouse_y)
        window.remove(first_oval)  # remove the oval which is created at the first click
        line = GLine(first_mouse_x, first_mouse_y, mouse.x, mouse.y)
        window.add(line)
        count += 1


if __name__ == "__main__":
    main()
