from turtle import Turtle, Screen
import time
import random
snake = []

screen = Screen()
screen.bgcolor("black")
screen.title("Snake_game")
screen.setup(width=1400, height=1000)
screen.listen()
screen.tracer(0)

score = Turtle()
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 350)
score.write("Score: 0", align="center", font=("Arial", 20, "bold"))
points = 0

starting_position = [(0,0), (20,0), (40,0)]
for position in starting_position:
    segment = Turtle()
    segment.shape("square")
    segment.color("red")
    segment.penup()
    segment.goto(position)
    snake.append(segment)

def add_segment():
    segment_new = Turtle()
    segment_new.shape("square")
    segment_new.color("green")
    segment_new.penup()

    segment_new.goto(snake[0].position())
    snake.insert(0, segment_new)
    print("TOTAL:", len(snake))

def game_over():
    screen.clear()
    screen.bgcolor("black")

    game_over_text = Turtle()
    game_over_text.color("white")
    game_over_text.hideturtle()
    game_over_text.write(
        "GAME OVER",
        align="center",
        font=("Arial", 40, "bold")
    )

food = Turtle()
food.color("red")
food.shape("circle")
food.shapesize(0.5)
food.penup()
food.goto(random.randint(-600,600),random.randint(-400,400))

direction = 0

def move_up():
    global direction
    if direction != 270:
        direction = 90
        snake[-1].setheading(direction)

def move_down():
    global direction
    if direction != 90:
        direction = 270
        snake[-1].setheading(direction)

def move_left():
    global direction
    if direction != 0:
        direction = 180
        snake[-1].setheading(direction)

def move_right():
    global direction
    if direction != 180:
        direction = 0
        snake[-1].setheading(direction)
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

game_on = True
while game_on:
    for i in range(len(snake) - 1):
        x = snake[i + 1].xcor()
        y = snake[i + 1].ycor()
        snake[i].goto(x, y)

    snake[-1].forward(20)

    # Wall collision
    if snake[-1].xcor() > 680 or snake[-1].xcor() < -680:
        game_over()
        game_on = False

    if snake[-1].ycor() > 480 or snake[-1].ycor() < -480:
        game_over()
        game_on = False
    # Self collision
    for segment in snake[:-1]:
        if snake[-1].distance(segment) < 10:
            game_over()
            game_on = False

    if snake[-1].distance(food) < 15:
        points += 1
        score.clear()
        score.write(f"Score: {points}", align="center", font=("Arial", 20, "bold"))
        food.goto(random.randint(-600, 600), random.randint(-400, 400))
        add_segment()

    screen.update()
    time.sleep(0.2)







screen.exitonclick()














