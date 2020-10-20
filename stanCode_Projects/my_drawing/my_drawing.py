"""
File: Anpanman.py
Name: Wu Ting
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GPolygon, GLabel
from campy.graphics.gwindow import GWindow

GAP = 20
SIZE_FACE = 175
SIZE_MOUTH = 100
SIZE_nose = 45
SIZE_cheek = 50
SIZE_nose_light = 9
SIZE_cheek_light = 8
EYE_WIDTH = 15
EYE_HEIGHT = 20
SIZE_eyebrow_width = 35
SIZE_eyebrow_height = 55
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, title='Anpanman.py')


def main():
    """
    Through this program, I exhibit a drawing of the anpanman (bread superhero) flying at the sky.
    Since I really love this cartoon character, so I choose this character. Moreover, anpanman always give me positive
    energy. Therefore, I use this drawing to encourage myself to continue coding and never give up.
    """
    background = GRect(WINDOW_WIDTH, WINDOW_HEIGHT, x=0, y=0)
    background.filled = True
    background.fill_color = 'skyblue'
    background.color = 'skyblue'
    window.add(background)

    cloak = GPolygon()  # the cloak of the anpanman
    cloak.add_vertex((300, 390))
    cloak.add_vertex((150, 250))
    cloak.add_vertex((450, 200))
    window.add(cloak)
    cloak.filled = True
    cloak.fill_color = 'saddlebrown'
    cloak.color = 'saddlebrown'

    cloak_circle = GOval(80, 60, x=190, y=229)  # I use an oval to retouch the border of the cloak
    cloak_circle.filled = True
    cloak_circle.fill_color = 'saddlebrown'
    cloak_circle.color = 'saddlebrown'
    window.add(cloak_circle)

    cloak_circle = GOval(70, 40, x=350, y=205)
    cloak_circle.filled = True
    cloak_circle.fill_color = 'saddlebrown'
    cloak_circle.color = 'saddlebrown'
    window.add(cloak_circle)

    cloak_circle = GOval(21, 13, x=425, y=199)
    cloak_circle.filled = True
    cloak_circle.fill_color = 'saddlebrown'
    cloak_circle.color = 'saddlebrown'
    window.add(cloak_circle)

    cloak_circle = GOval(23, 13, x=153, y=245)
    cloak_circle.filled = True
    cloak_circle.fill_color = 'saddlebrown'
    cloak_circle.color = 'saddlebrown'
    window.add(cloak_circle)

    cloak_circle = GOval(13, 23, x=209, y=293)
    cloak_circle.filled = True
    cloak_circle.fill_color = 'saddlebrown'
    cloak_circle.color = 'saddlebrown'
    window.add(cloak_circle)

    cloak_circle = GOval(13, 23, x=378, y=264)
    cloak_circle.filled = True
    cloak_circle.fill_color = 'saddlebrown'
    cloak_circle.color = 'saddlebrown'
    window.add(cloak_circle)

    red = GOval(WINDOW_WIDTH, WINDOW_HEIGHT, x=WINDOW_WIDTH/2, y=WINDOW_HEIGHT/2)  # the red part of the rainbow
    red.filled = True
    red.fill_color = 'red'
    red.color = 'red'
    window.add(red)

    orange = GOval(WINDOW_WIDTH-GAP, WINDOW_HEIGHT-GAP, x=WINDOW_WIDTH/2+GAP, y=WINDOW_HEIGHT/2+GAP)
    orange.filled = True
    orange.fill_color = 'orange'
    orange.color = 'orange'
    window.add(orange)

    yellow = GOval(WINDOW_WIDTH-GAP*2, WINDOW_HEIGHT-GAP*2, x=WINDOW_WIDTH/2+GAP*2, y=WINDOW_HEIGHT/2+GAP*2)
    yellow.filled = True
    yellow.fill_color = 'yellow'
    yellow.color = 'yellow'
    window.add(yellow)

    green = GOval(WINDOW_WIDTH-GAP*3, WINDOW_HEIGHT-GAP*3, x=WINDOW_WIDTH/2+GAP*3, y=WINDOW_HEIGHT/2+GAP*3)
    green.filled = True
    green.fill_color = 'green'
    green.color = 'green'
    window.add(green)

    blue = GOval(WINDOW_WIDTH-GAP*4, WINDOW_HEIGHT-GAP*4, x=WINDOW_WIDTH/2+GAP*4, y=WINDOW_HEIGHT/2+GAP*4)
    blue.filled = True
    blue.fill_color = 'blue'
    blue.color = 'blue'
    window.add(blue)

    dark_blue = GOval(WINDOW_WIDTH-GAP*5, WINDOW_HEIGHT-GAP*5, x=WINDOW_WIDTH/2+GAP*5, y=WINDOW_HEIGHT/2+GAP*5)
    dark_blue.filled = True
    dark_blue.fill_color = 'dark_blue'
    dark_blue.color = 'dark_blue'
    window.add(dark_blue)

    purple = GOval(WINDOW_WIDTH-GAP*6, WINDOW_HEIGHT-GAP*6, x=WINDOW_WIDTH/2+GAP*6, y=WINDOW_HEIGHT/2+GAP*6)
    purple.filled = True
    purple.fill_color = 'purple'
    purple.color = 'purple'
    window.add(purple)

    background2 = GOval(WINDOW_WIDTH-GAP*7, WINDOW_HEIGHT-GAP*7, x=WINDOW_WIDTH/2+GAP*7, y=WINDOW_HEIGHT/2+GAP*7)
    background2.filled = True
    background2.fill_color = 'skyblue'
    background2.color = 'skyblue'
    window.add(background2)

    face = GOval(SIZE_FACE, SIZE_FACE, x=(WINDOW_WIDTH-SIZE_FACE)/2, y=(WINDOW_HEIGHT-SIZE_FACE)/2)
    face.filled = True
    face.fill_color = 'peru'
    window.add(face)

    left_eyebrow = GOval(SIZE_eyebrow_width, SIZE_eyebrow_height, x=face.x+47, y=face.y+20)
    left_eyebrow.filled = True
    left_eyebrow.fill_color = 'peru'
    window.add(left_eyebrow)

    rect_cover = GRect(SIZE_eyebrow_width, SIZE_eyebrow_height, x=left_eyebrow.x, y=left_eyebrow.y+left_eyebrow.height/2-5)
    rect_cover.filled = True
    rect_cover.fill_color = 'peru'
    rect_cover.color = 'peru'
    window.add(rect_cover)

    right_eyebrow = GOval(SIZE_eyebrow_width, SIZE_eyebrow_height, x=left_eyebrow.x+45, y=face.y+20)
    right_eyebrow.filled = True
    right_eyebrow.fill_color = 'peru'
    window.add(right_eyebrow)

    rect_cover = GRect(SIZE_eyebrow_width, SIZE_eyebrow_height, x=right_eyebrow.x, y=left_eyebrow.y+left_eyebrow.height/2-5)
    rect_cover.filled = True
    rect_cover.fill_color = 'peru'
    rect_cover.color = 'peru'
    window.add(rect_cover)

    mouth = GOval(SIZE_MOUTH, SIZE_MOUTH-5, x=face.x+40, y=face.y+50)
    mouth.filled = True
    mouth.fill_color = 'darkred'
    mouth.color = 'black'
    window.add(mouth)

    mouth_cover = GRect(SIZE_MOUTH, SIZE_MOUTH/2+15, x=face.x+40, y=face.y+50)
    mouth_cover.filled = True
    mouth_cover.fill_color = 'peru'
    mouth_cover.color = 'peru'
    window.add(mouth_cover)

    upper_mouth = GLine(face.x+40, mouth_cover.y+SIZE_MOUTH/2+15, face.x+135, mouth_cover.y+SIZE_MOUTH/2+15)
    window.add(upper_mouth)

    nose = GOval(SIZE_nose+5, SIZE_nose, x=(WINDOW_WIDTH-SIZE_nose)/2, y=(WINDOW_HEIGHT-SIZE_nose)/2)
    nose.filled = True
    nose.fill_color = 'red'
    window.add(nose)

    left_cheek = GOval(SIZE_cheek, SIZE_cheek, x=(WINDOW_WIDTH-SIZE_nose)/2-SIZE_cheek, y=(WINDOW_HEIGHT-SIZE_nose)/2)
    left_cheek.filled = True
    left_cheek.fill_color = 'salmon'
    window.add(left_cheek)

    right_cheek = GOval(SIZE_cheek, SIZE_cheek, x=(WINDOW_WIDTH-SIZE_nose)/2+SIZE_nose+5, y=(WINDOW_HEIGHT-SIZE_nose)/2)
    right_cheek.filled = True
    right_cheek.fill_color = 'salmon'
    window.add(right_cheek)

    nose_light = GRect(SIZE_nose_light, SIZE_nose_light, x=(WINDOW_WIDTH-SIZE_nose_light)/2+1, y=(WINDOW_HEIGHT-SIZE_nose_light)/2-1)
    nose_light.filled = True
    nose_light.fill_color = 'white'
    nose_light.color = 'white'
    window.add(nose_light)

    left_eye = GOval(EYE_WIDTH, EYE_HEIGHT, x=nose.x - 7, y=nose.y-27)
    left_eye.filled = True
    window.add(left_eye)

    right_eye = GOval(EYE_WIDTH, EYE_HEIGHT, x=left_eye.x + SIZE_nose, y=nose.y-27)
    right_eye.filled = True
    window.add(right_eye)

    cheek_light = GRect(SIZE_cheek_light, SIZE_cheek_light, x=nose_light.x+(SIZE_nose+SIZE_cheek)/2, y=(WINDOW_HEIGHT-SIZE_nose_light)/2-1)
    cheek_light.filled = True
    cheek_light.fill_color = 'white'
    cheek_light.color = 'white'
    window.add(cheek_light)

    cheek_light = GRect(SIZE_cheek_light, SIZE_cheek_light, x=nose_light.x - (SIZE_nose + SIZE_cheek) / 2,
                        y=(WINDOW_HEIGHT - SIZE_nose_light) / 2 - 1)
    cheek_light.filled = True
    cheek_light.fill_color = 'white'
    cheek_light.color = 'white'
    window.add(cheek_light)

    hand = GOval(80, 70, x=face.x-20, y=face.y+SIZE_FACE-45)
    hand.filled = True
    hand.fill_color = 'yellow'
    window.add(hand)

    stancode = GLabel('Stancode!', x=hand.x+5, y=hand.y+40)
    stancode.color = 'black'
    stancode.font = 'Courier-10-italic'
    window.add(stancode)







if __name__ == '__main__':
    main()
