"""This program allows the user to draw the American flag on a created white
background with the turtle class"""

# import the time and turtle module
import turtle
import time

# creating a screen
# For me, python tells me that turtle.getScreen() is an error,
# but the program needs this line to work
scr = turtle.getscreen()
scr.title("Flag of America")
scr.bgcolor("white")

# Set the turtle object and speed of the turtle

t = turtle.Turtle()
t.speed(20)
t.penup()

# flag height and width
FLAGHEIGHT = 250
FLAGWIDTH = 475

# starting points of the flag
X1 = -250
Y1 = 120

# red and white stripes (total 13 stripes in flag)
STRIPEHEIGHT = FLAGHEIGHT/13
STRIPEWIDTH = FLAGWIDTH
# star size
STARSIZE = 12


def draw_rectangle(coord_x, coord_y, height, width, color):
    """Called from drawing stripes function. draws the outside of the box, then
    fills in with the given colors to make different colored stripes"""
    t.goto(coord_x, coord_y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.end_fill()
    t.penup()


def star_shape(coord_x, coord_y, color, length):
    """The functions that create different amounts of stars per rows call this one,
    which is what actually uses the turtle functions to draw the stars"""
    t.goto(coord_x, coord_y)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.color(color)
    for turn in range(0, 5):
        t.forward(length)
        t.right(144)
        t.forward(length)
        t.right(144)
    t.end_fill()
    t.penup()


def draw_stripes():
    """function to create stripes of flag"""
    coord_x = X1
    coord_y = Y1
    # draw 6 red and 7 white strips
    for stripe in range(0, 6):
        for color in ["red", "white"]:
            draw_rectangle(coord_x, coord_y, STRIPEHEIGHT, STRIPEWIDTH, color)
            # decrease value of y by stripe_height
            coord_y = coord_y - STRIPEHEIGHT

    # create last red stripe
    draw_rectangle(coord_x, coord_y, STRIPEHEIGHT, STRIPEWIDTH, 'red')
    coord_y = coord_y - STRIPEHEIGHT


def draw_square():
    """this function create navy color square"""
    square_ht = (7/13) * FLAGHEIGHT
    square_wdt = (0.76) * FLAGHEIGHT
    draw_rectangle(X1, Y1, square_ht, square_wdt, 'navy')


def stars1():
    """This is the function for drawing a row of 6 stars"""
    dist_of_stars = 30
    dist_bet_lines = STRIPEHEIGHT + 6
    coord_y = 112
    # create 5 rows of stars
    for row in range(0, 5):
        coord_x = -234
        # create 6 stars in each row
        for star in range(0, 6):
            star_shape(coord_x, coord_y, 'white', STARSIZE)
            coord_x = coord_x + dist_of_stars
        coord_y = coord_y - dist_bet_lines


def stars_five():
    """This is the function for drawing a row of 5 stars"""
    dist_of_stars = 30
    dist_bet_lines = STRIPEHEIGHT + 6
    coord_y = 100
    # create 4 rows of stars
    for row in range(0, 4):
        coord_x = -217
        # create 5 stars in each row
        for star in range(0, 5):
            star_shape(coord_x, coord_y, 'white', STARSIZE)
            coord_x = coord_x + dist_of_stars
        coord_y = coord_y - dist_bet_lines


# Call all the functions
# start after 5 seconds.
time.sleep(5)
# draw 13 stripes
draw_stripes()
# draw squares
draw_square()
# draw 30 stars, 6 * 5
stars1()
# draw 20 stars, 5 * 4
stars_five()
# hides the turtle
t.hideturtle()


# With this project, I learned how turtle works,
# along with how to create a background screen to be able to draw on.
