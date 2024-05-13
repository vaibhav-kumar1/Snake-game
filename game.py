# Snake Game : Design a game where the user controls a snake that grows as it eats food, while avoiding obstacles and its own tail
import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Set up the screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("yellow")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Snake food (laddu)
food = turtle.Turtle()
colors = ["red", "green", "blue", "orange", "yellow", "purple", "pink", "brown"]
food.speed(0)
food.shape("circle")
food.color(random.choice(colors))
food.penup()
food.goto(0, 100)

segments = []

# Pen (for displaying score)
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

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

def check_collision():
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        return True

    for segment in segments[1:]:
        if segment.distance(head) < 20:
            return True

    return False

def generate_food():
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    food.goto(x, y)

def update_score():
    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

# Keyboard bindings
screen.listen()
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_left, "a")
screen.onkey(go_right, "d")

# Main game loop
while True:
    screen.update()

    # Check for collision with food
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape("square")
        segment.color("white")
        segment.penup()
        segments.append(segment)
        score += 10

        if score > high_score:
            high_score = score

        update_score()
        generate_food()

    # Move the end segments first
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # Check for collision with wall or tail
    if check_collision():
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()
        score = 0
        update_score()

    move()

    time.sleep(delay)

turtle.done()
