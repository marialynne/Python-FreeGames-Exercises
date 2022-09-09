"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.

"""

from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
counter = 0
couple = 0

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    i = index(x, y)
    down()

    #Add different colors for the different rows
    if i > 55:
        color('black', 'darkblue')
    elif i > 47:
        color('black', 'blueviolet')
    elif i > 39:
                color('black', 'deeppink')
    elif i > 31:
                color('black', 'crimson')
    elif i > 23:
                color('black', 'darkorange')
    elif i > 15:
                color('black', 'gold')
    elif i > 7:
                color('black', 'yellowgreen')
    elif i >= 0:
                color('black', 'mediumaquamarine')

    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        global couple
        couple =+ 1
        
   
    #Each taps increments by 1
    global counter
    counter = counter + 1

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        if len(str(tiles[mark])) > 1:
            goto(x, y)
            color('black')
            write(tiles[mark], font=('Arial', 28, 'normal'))
        else:
            goto(x + 14, y)
            color('black')
            write(tiles[mark], font=('Arial', 28, 'normal'))
                 
    
    #Write the number of taps
    global counter
    up()
    goto(-205, 205)
    color('black')
    write(f"Taps:{counter}", font=('Arial', 12, 'normal'))
    
    up()
    goto(140, 205)
    color('black')
    write(f"Pairs:{couple}", font=('Arial', 12, 'normal'))
    
    if couple == 32:
        up()
        goto(-115, 205)
        color('blue')
        write("All cards are uncovered!", font=('Arial', 12, 'normal'))
    
    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(490, 490, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
