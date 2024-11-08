from turtle import *

def draw_moon():
    speed(3)  # Painting speed control
    bgcolor("Midnight Blue")  # Background color
    penup()
    goto(0, -100)  # Starting position
    pendown()
    color("Light Gray")
    begin_fill()
    circle(100)  # Draw the full moon
    end_fill()

    # Add some craters for realism
    penup()
    goto(-20, 30)
    pendown()
    color("Gray")
    begin_fill()
    circle(10)
    end_fill()

    penup()
    goto(40, 60)
    pendown()
    begin_fill()
    circle(15)
    end_fill()

    penup()
    goto(20, -40)
    pendown()
    begin_fill()
    circle(8)
    end_fill()

    penup()
    goto(-50, -30)
    pendown()
    begin_fill()
    circle(12)
    end_fill()

    done()  # Finish drawing

# Run the moon drawing function
draw_moon()
