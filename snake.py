import turtle
import time
import random

delay = 0.02
body_segments = []
score = 0
high_score = 0

wn = turtle.Screen()
#title
wn.title("Snake Game")
#windows size
wn.setup(width=600, height=600)
#background color
wn.bgcolor('blue')

#head settings
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('white')
head.penup()
head.goto(0,0)
head.direction = "stop"

#Food settings
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0, 100)
food.direction = 'stop'

#Score
text = turtle.Turtle()
text.speed(0)
text.color('white')
text.penup()
text.hideturtle()
text.goto(0, 260)
text.write(f'Score 0        High Score: 0', align="center", font=(30))

#Move settings
def mov():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 10)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 10)
    if head.direction == "right":
        y = head.xcor()
        head.setx(y + 10)
    if head.direction == "left":
        y = head.xcor()
        head.setx(y - 10)

def dirUp():
    if head.direction != "down":  # Evita que vaya hacia abajo si ya está hacia arriba
        head.direction = "up"

def dirDown():
    if head.direction != "up":  # Evita que vaya hacia arriba si ya está hacia abajo
        head.direction = "down"

def dirRight():
    if head.direction != "left":  # Evita que vaya hacia la izquierda si ya está hacia la derecha
        head.direction = "right"

def dirLeft():
    if head.direction != "right":  # Evita que vaya hacia la derecha si ya está hacia la izquierda
        head.direction = "left"


wn.listen()
wn.onkeypress(dirUp, "Up")
wn.onkeypress(dirDown, "Down")
wn.onkeypress(dirRight, "Right")
wn.onkeypress(dirLeft, "Left")

while True:
    wn.update()
    #Colisiones

    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for segment in body_segments:
            segment.goto(1000, -1000)
        body_segments.clear()
        score = 0
        text.clear()
        text.write(f'Score {score}        High Score: {high_score}', align="center", font=(30))

        


    
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        #New segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('white')
        new_segment.penup()
        body_segments.append(new_segment)

        score += 10
        if score > high_score:
            high_score = score
        
        text.clear()
        text.write(f'Score {score}        High Score: {high_score}', align="center", font=(30))


    totalSeg = len(body_segments)

    for i in range(totalSeg - 1, 0, -1):
        x = body_segments[i-1].xcor()
        y = body_segments[i-1].ycor()
        body_segments[i].goto(x, y)
    
    if totalSeg > 0:
        x = head.xcor()
        y = head.ycor()
        body_segments[0].goto(x, y)


    mov()

    for segment in body_segments:
        if segment.distance(head) < 10:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for segment in body_segments:
                segment.goto(1000, -1000)
            
            body_segments.clear()
            score = 0
            text.clear()
            text.write(f'Score {score}        High Score: {high_score}', align="center", font=(30))



    
    time.sleep(delay)

turtle.done()
