import turtle
import time
import random

delay = 0.1
score = 0
highest_score = 0

# Set up the screen
s = turtle.Screen()
s.title(" Asra Naj create the Snake Game")
s.bgcolor("pink")
s.setup(width=600, height=600)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.ht()  # hide initially
food.goto(0, 200)
food.st()  # show when ready

# Score board
sb = turtle.Turtle()
sb.shape("square")
sb.color("black")
sb.penup()
sb.ht()
sb.goto(-250, -250)
sb.write("Score: 0  Highest Score: 0", align="left", font=("Arial", 14, "normal"))

# Snake bodies
bodies = []

# Functions to move the snake
def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":
        head.direction = "right"

def move_stop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Event handling for key mapping
s.listen()
s.onkey(move_up, "Up")
s.onkey(move_down, "Down")
s.onkey(move_left, "Left")
s.onkey(move_right, "Right")
s.onkey(move_stop, "space")

# Main game loop
while True:
    s.update()  # Update the screen

    # Check collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the bodies
        for body in bodies:
            body.ht()

        bodies.clear()
        score = 0
        delay = 0.1
        sb.clear()
        sb.write(f"Score: {score}  Highest Score: {highest_score}", align="left", font=("Arial", 14, "normal"))

    # Check collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("blue")
        new_body.penup()
        bodies.append(new_body)

        # Increase the score
        score += 10
        if score > highest_score:
            highest_score = score
        
        sb.clear()
        sb.write(f"Score: {score}  Highest Score: {highest_score}", align="left", font=("Arial", 14, "normal"))

        # Decrease the delay for faster gameplay
        delay -= 0.001

    # Move the snake bodies
    for index in range(len(bodies) - 1, 0, -1):
        x = bodies[index - 1].xcor()
        y = bodies[index - 1].ycor()
        bodies[index].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # Check collision with snake body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the bodies
            for b in bodies:
                b.ht()

            bodies.clear()
            score = 0
            delay = 0.1
            sb.clear()
            sb.write(f"Score: {score}  Highest Score: {highest_score}", align="left", font=("Arial", 14, "normal"))

    time.sleep(delay)

s.mainloop()
# end the code
