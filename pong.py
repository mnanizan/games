"""
Simple POng in Python 3 for beginner

"""
import turtle
import winsound

# The window
wn = turtle.Screen() # wn is window
wn.title("Pong by @mnoranzn")
wn.bgcolor("black") # background color
wn.setup(width = 800, height = 600) # size of the window
wn.tracer(0) #stop the window from updating thus speed up the game

# Score
score_a = 4740
score_b = 5555


# Paddle A
paddle_a = turtle.Turtle() #turtle refers to the module, Turtle refers to class name
paddle_a.speed(0) #the speed of the animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid= 5, stretch_len= 1)
paddle_a.penup() #to not draw a line in the game
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle() #turtle refers to the module, Turtle refers to class name
paddle_b.speed(0) #the speed of the animation
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid= 5, stretch_len= 1) #size of the paddle
paddle_b.penup() #to not draw a line in the game
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle() #turtle refers to the module, Turtle refers to class name
ball.speed(0) #the speed of the animation
ball.shape("square")
ball.color("white")
ball.penup() #to not draw a line in the game
ball.goto(0, 0)
ball.dx = 0.3 #ball movement at x-axis with a speed of 0.5 pixel
ball.dy = -0.3 #ball movement at y-axis with a speed of 0.5 pixel

# Score board
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("New Cases: 0 Discharge: 0", align="center", font=("Courier", 24, "normal"))

# Function to move the paddle using keyboard
def paddle_a_up():
    y = paddle_a.ycor() #'y'coordinate
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() #'y'coordinate
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() #'y'coordinate
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() #'y'coordinate
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"d")
wn.onkeypress(paddle_b_up,"8")
wn.onkeypress(paddle_b_down,"4")

# Main game loop
while True:
    wn.update() #evertime the loop runs, the window will update

    #to move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    #to bounce the ball once it touch the top & bottom border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("ball_bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("ball_bounce.wav", winsound.SND_ASYNC)

    #to get the ball back at center once it pass the left & right border
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("New Cases: {} Discharge: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("New Cases: {}  Discharge: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    #paddle & ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("ball_bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("ball_bounce.wav", winsound.SND_ASYNC)







