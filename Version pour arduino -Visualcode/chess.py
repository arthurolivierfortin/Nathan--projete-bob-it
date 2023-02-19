import turtle

# set up the screen and turtle
screen = turtle.Screen()
screen.bgcolor('white')
turtle = turtle.Turtle()
turtle.speed(0)
turtle.hideturtle()

# set the square size and number of squares
square_size = 50
num_squares = 8

# draw the chessboard
for i in range(num_squares):
    for j in range(num_squares):
        # calculate the square's position
        x_pos = (j - num_squares/2) * square_size
        y_pos = (i - num_squares/2) * square_size

        # draw the square
        turtle.penup()
        turtle.goto(x_pos, y_pos)
        turtle.pendown()

        if (i + j) % 2 == 0:
            turtle.fillcolor('white')
        else:
            turtle.fillcolor('gray')
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(square_size)
            turtle.right(90)
        turtle.end_fill()

# keep the screen open until it's manually closed
screen.mainloop()
