"""Snake, classic arcade game.

Excercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
speed = 40
snake = [vector(0, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -300 < head.x < 300 and -300 < head.y < 300

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 10, 'black')
        "죽음표시"
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-29, 29) * 10
        food.y = randrange(-29, 29) * 10
    else :
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 10, 'red')
    "스네이크색"

    square(food.x, food.y, 10, 'blue')
    "점 색"
    
    update()

    ontimer(move, speed)
    "속도부분"

setup(600, 600, 300, 0)
"크기부분"
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
