import turtle
wn = turtle.Screen()
wn.setup(400, 400)

tr = turtle.Turtle()
tr.shape("turtle")
tr.penup()
tr.goto(x=0, y=-100)
tr.pendown()
tr.fillcolor("yellow")
tr.begin_fill()
tr.circle(100)
tr.end_fill()

# for eye right
eye1 = turtle.Turtle()
eye1.penup()
eye1.goto(x=30, y=20)
eye1.pendown()
eye1.fillcolor("white")
eye1.begin_fill()
eye1.circle(20)
eye1.end_fill()



eye3 = turtle.Turtle()
eye3.penup()
eye3.goto(x=30, y=30)
eye3.pendown()
eye3.fillcolor("black")
eye3.begin_fill()
eye3.circle(10)
eye3.end_fill()




# for eye left
eye2 = turtle.Turtle()
eye2.penup()
eye2.goto(x=-30, y=20)
eye2.pendown()
eye2.fillcolor("white")
eye2.begin_fill()
eye2.circle(20)
eye2.end_fill()



eye4 = turtle.Turtle()
eye4.penup()
eye4.goto(x=-30, y=30)
eye4.pendown()
eye4.fillcolor("black")
eye4.begin_fill()
eye4.circle(10)
eye4.end_fill()

mouth = turtle.Turtle()
mouth.penup()
mouth.goto(x=-40, y=-40)
mouth.pendown()
mouth.right(120)
mouth.width(5)
mouth.circle(50, -120)



wn.mainloop()