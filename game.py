import turtle
import random
import time
import tkinter

LIVES = 3
SCORE = 0

wn = turtle.Screen()
wn.title("Mening O'yinim")
wn.bgcolor("#1e1e2f")
wn.setup(700, 700)
wn.setworldcoordinates(-350, -350, 350, 350)


bottom_border = turtle.Turtle()
bottom_border.color("#ff5733")
bottom_border.speed(0) # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
bottom_border.width(5)
bottom_border.penup()
bottom_border.goto(x=-350, y=-250)
bottom_border.pendown()
bottom_border.forward(700)
bottom_border.hideturtle()




border = turtle.Turtle()
border.shape("turtle")
border.width(5)
border.color("#ffcc00")
border.speed(0)
border.penup()
border.goto(x=-350, y=350)
border.pendown()

for i in range(4):
    border.forward(700)
    border.right(90)
border.hideturtle()

status_writer = turtle.Turtle()
status_writer.hideturtle()
status_writer.penup()
status_writer.goto(x=-330, y=300)
status_writer.pendown()
status_writer.color("white")


def update_status():
    status_writer.clear()
    status_writer.write(f"Urunishlar Soni: {LIVES}\n Ball: {SCORE}",
                        font=("Arial", 16, "bold"))

update_status()



def handler_ball(x, y, ball):
    global SCORE
    SCORE += 1
    update_status()
    ball.hideturtle()
    create_ball()


def game_over():
    border.clear()
    bottom_border.clear()
    over_writer = turtle.Turtle()
    over_writer.hideturtle()
    over_writer.color("red")
    over_writer.penup()
    over_writer.goto(x=-220, y=0)
    over_writer.pendown()
    over_writer.write("GAME OVER", font=("Arial", 52, "bold"))

def create_ball():
    for o in range(10):
        x_cor = random.randint(-350, 350)
        size = random.randint(1, 3)
        ball = turtle.Turtle()
        ball.turtlesize(size, size)
        ball.hideturtle()
        ball.shape("turtle")
        ball.color("white")
        ball.penup()
        ball.goto(x_cor, 350)
        ball.showturtle()
        ball.right(90)

        ball.onclick(lambda x, y: handler_ball(x, y, ball))

        try:
            while ball.ycor() > -250:
                ball.forward(10)
                time.sleep(0.02)
            ball.hideturtle()

            global LIVES
            if LIVES <= 0:
                LIVES = LIVES - 1
                game_over()
                break

            LIVES -= 1
            update_status()
        except tkinter.TclError:
            return
        except turtle.Terminator:
            return





create_ball()
wn.mainloop()


