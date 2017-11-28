"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Kynon Johnson.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

blue_turtle = rg.SimpleTurtle('turtle')
blue_turtle.pen = rg.Pen('blue', 3)
blue_turtle.speed = 15  # Fast

orange_turtle = rg.SimpleTurtle('turtle')
orange_turtle.pen = rg.Pen('orange', 3)
orange_turtle.speed = 15  # Fast


# Start position for blue turtle
blue_turtle.pen_up()
blue_turtle.left(175)
blue_turtle.forward(260)
blue_turtle.right(175)
blue_turtle.left(95)
blue_turtle.pen_down()

# Start position for orange turtle
orange_turtle.pen_up()
orange_turtle.right(5)
orange_turtle.forward(260)
orange_turtle.left(5)
orange_turtle.right(85)
orange_turtle.pen_down()

# The first star will have sides of 50 pixels:
size = 25

# Do the indented code 13 times.  Each time draws a star.
for k in range(7):

    # Put the pen down, then draw a star for blue turtle of the given size:

    blue_turtle.forward(size)
    blue_turtle.right(72)
    blue_turtle.forward(size)
    blue_turtle.left(144)
    blue_turtle.forward(size)
    blue_turtle.right(72)
    blue_turtle.forward(size)
    blue_turtle.left(144)
    blue_turtle.forward(size)
    blue_turtle.right(72)
    blue_turtle.forward(size)
    blue_turtle.left(144)
    blue_turtle.forward(size)
    blue_turtle.right(72)
    blue_turtle.forward(size)
    blue_turtle.left(144)
    blue_turtle.forward(size)
    blue_turtle.right(72)
    blue_turtle.forward(size)
    blue_turtle.left(144)

    # Put the pen down, then draw a star for orange turtle of the given size:

    orange_turtle.forward(size)
    orange_turtle.right(72)
    orange_turtle.forward(size)
    orange_turtle.left(144)
    orange_turtle.forward(size)
    orange_turtle.right(72)
    orange_turtle.forward(size)
    orange_turtle.left(144)
    orange_turtle.forward(size)
    orange_turtle.right(72)
    orange_turtle.forward(size)
    orange_turtle.left(144)
    orange_turtle.forward(size)
    orange_turtle.right(72)
    orange_turtle.forward(size)
    orange_turtle.left(144)
    orange_turtle.forward(size)
    orange_turtle.right(72)
    orange_turtle.forward(size)
    orange_turtle.left(144)

    # Move a little below and to the right of where the previous
    # square started.  Do this with the pen up (so nothing is drawn).
    blue_turtle.pen_up()
    blue_turtle.right(25)
    blue_turtle.forward(size + size)
    blue_turtle.left(5)

    # Move a little below and to the right of where the previous
    # square started.  Do this with the pen up (so nothing is drawn).
    orange_turtle.pen_up()
    orange_turtle.right(25)
    orange_turtle.forward(size + size)
    orange_turtle.left(5)

    # Put the pen down again (so drawing resumes).
    # Make the size for the NEXT square be 12 pixels smaller.
    blue_turtle.pen_down()
    orange_turtle.pen_down()
    size = size + 10

window.close_on_mouse_click()
