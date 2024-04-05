import turtle as t
import random
import tkinter as tk

w = 500  # Width of box
h = 500  # Height of box
food_size = 10  # Size of food
delay = 100  # in milliseconds

# Values by which snake will move in direction when given direction
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

global SCORE
SCORE = 0
# Default position of game scene


def reset():
    global snake, snake_dir, food_position, pen, SCORE

    SCORE = 0  # Reset score
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    snake_dir = "up"  # default snake direction
    food_position = get_random_food_position()
    food.goto(food_position)  # render food on scene
    move_snake()
    update_score()


def move_snake():
    global snake_dir, SCORE

    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[snake_dir][0]
    new_head[1] = snake[-1][1] + offsets[snake_dir][1]

    if new_head in snake[:-1] or is_collision(new_head):  # Check if snake hits itself or the wall
        game_over()
        return
    else:
        snake.append(new_head)

        if not food_collision():
            snake.pop(0)

        if snake[-1][0] > w / 2:
            snake[-1][0] -= w
        elif snake[-1][0] < - w / 2:
            snake[-1][0] += w
        elif snake[-1][1] > h / 2:
            snake[-1][1] -= h
        elif snake[-1][1] < -h / 2:
            snake[-1][1] += h

        pen.clearstamps()

        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()

        screen.update()
        t.ontimer(move_snake, delay)


# If snake collides with food
def food_collision():
    global food_position, SCORE
    if get_distance(snake[-1], food_position) < 20:
        SCORE += 1  # Increase score by 1
        food_position = get_random_food_position()
        food.goto(food_position)
        update_score()
        return True
    return False


# Random position for food
def get_random_food_position():
    x = random.randint(- w / 2 + food_size, w / 2 - food_size)
    y = random.randint(- h / 2 + food_size, h / 2 - food_size)
    return (x, y)


def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance


def update_score():
    score_pen.clear()
    score_pen.write("Score: {}".format(SCORE), align="center", font=("Courier", 24, "normal"))


# Check if snake hits the wall
def is_collision(pos):
    x, y = pos
    if x >= w/2 or x <= -w/2 or y >= h/2 or y <= -h/2:
        return True
    return False


# Function to display "Game Over" in the Turtle window
def game_over():
    pen.clear()
    pen.goto(0, 0)
    pen.write("Game Over", align="center", font=("Courier", 36, "normal"))


# Control
def go_up():
    global snake_dir
    if snake_dir != "down":
        snake_dir = "up"


def go_down():
    global snake_dir
    if snake_dir != "up":
        snake_dir = "down"


def go_left():
    global snake_dir
    if snake_dir != "right":
        snake_dir = "left"


def go_right():
    global snake_dir
    if snake_dir != "left":
        snake_dir = "right"


#define screen setup
screen = t.Screen()
screen.setup(w, h)
screen.title("Snake Game")
screen.bgcolor("lightgrey")
screen.tracer(0)

#define snake setup
pen = t.Turtle("square")
pen.penup()

#define food setup
food = t.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(food_size / 20)
food.penup()

#define score pen
score_pen = t.Turtle()
score_pen.penup()
score_pen.goto(0, h // 2 - 40)
score_pen.hideturtle()

#define control setup
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

reset()
t.done()
