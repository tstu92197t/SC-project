"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    return GRAPH_MARGIN_SIZE+((width-2*GRAPH_MARGIN_SIZE)/len(YEARS))*year_index+TEXT_DX


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH, fill='black')
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill='black')

    for i in range(len(YEARS)):
        if len(YEARS) != 0:
            year_index = i
            canvas.create_line(get_x_coordinate(CANVAS_WIDTH, year_index)-TEXT_DX, 0, get_x_coordinate(CANVAS_WIDTH, year_index)-TEXT_DX, CANVAS_HEIGHT,
                               width=LINE_WIDTH, fill='black')
            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, year_index), CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[year_index], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    count = 0
    for name in lookup_names:
        for i in range(len(YEARS)):
            for key in name_data[name]:
                if str(YEARS[i]) in str(key):
                    count += 1
            if count == 0:
                name_data[name][str(YEARS[i])] = '1001'
            count = 0
        name_data[name] = dict(sorted(name_data[name].items(), key = lambda x: int(x[0])))
        print(name_data[name])

    index = 0
    value_previous = 0
    color_count = 0
    for name in lookup_names:
        if name in name_data:
            for key, value in name_data[name].items():
                print(key)
                print(index)
                if index == 0:
                    value = name_data[name][key]
                    print(value)
                    if int(value) < 1000:
                        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, index), GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)*int(value)/1000,
                                           text=(name, value), anchor=tkinter.SW, fill=COLORS[color_count % len(COLORS)])
                    else:
                        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, index), CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                           text=(name, '*'), anchor=tkinter.SW, fill=COLORS[color_count % len(COLORS)])
                    index += 1
                else:
                    value = name_data[name][key]
                    if int(value) < 1000:
                        if int(value_previous) < 1000:
                            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, index), GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)*int(value)/1000,
                                               text=(name, value), anchor=tkinter.SW, fill=COLORS[color_count % len(COLORS)])

                            canvas.create_line(get_x_coordinate(CANVAS_WIDTH, index-1)-TEXT_DX, GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)*int(value_previous)/1000,
                                               get_x_coordinate(CANVAS_WIDTH, index)-TEXT_DX, GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)*int(value)/1000,
                                               width=LINE_WIDTH, fill=COLORS[color_count % len(COLORS)])
                        else:
                            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, index), GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)*int(value)/1000,
                                               text=(name, value), anchor=tkinter.SW, fill=COLORS[color_count % len(COLORS)])

                            canvas.create_line(get_x_coordinate(CANVAS_WIDTH, index - 1)-TEXT_DX,
                                               CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                               get_x_coordinate(CANVAS_WIDTH, index)-TEXT_DX,
                                               GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * int(
                                                   value) / 1000,
                                               width=LINE_WIDTH, fill=COLORS[color_count % len(COLORS)])
                    else: # int(value) >= 1000
                        if int(value_previous) < 1000:
                            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, index), CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                               text=(name, '*'), anchor=tkinter.SW,
                                               fill=COLORS[color_count % len(COLORS)])

                            canvas.create_line(get_x_coordinate(CANVAS_WIDTH, index - 1)-TEXT_DX,
                                               GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * int(
                                                   value_previous) / 1000,
                                               get_x_coordinate(CANVAS_WIDTH, index)-TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                               width=LINE_WIDTH, fill=COLORS[color_count % len(COLORS)])
                        else:
                            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, index), CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                               text=(name, '*'), anchor=tkinter.SW,
                                               fill=COLORS[color_count % len(COLORS)])

                            canvas.create_line(get_x_coordinate(CANVAS_WIDTH, index - 1)-TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                               get_x_coordinate(CANVAS_WIDTH, index)-TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                               width=LINE_WIDTH, fill=COLORS[color_count % len(COLORS)])
                    index += 1
                value_previous = value
            color_count += 1
            index = 0


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
