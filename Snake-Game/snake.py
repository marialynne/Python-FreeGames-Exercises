"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange, randint
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
#Add Color list
color_list = ['green', 'black', 'yellow', 'blue', 'magenta']
#Snake Color
snake_color = ''
#Food Color
food_color = ''

#Create color function
def color(colors):
    #Define random index
    i = randint(0, len(colors)-1)
    j = i + randint(1, 3)
    if j >= len(colors):
        j = j - 5
    #Assign random color
    food = colors[i]
    snake = colors[j]

    return (food, snake)
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    # The food moves randomly through each step of the snake
    food.x = randrange(-15, 15) * 10
    food.y = randrange(-15, 15) * 10
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
#Define colors
food_color, snake_color = color(color_list)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
