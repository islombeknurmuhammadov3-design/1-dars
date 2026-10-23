import turtle

window = turtle.Screen()
window.title("1-dars")

tr = turtle.Turtle()
tr.shape("turtle")

tr.color("green")

for j in range(6):
    tr.forward(100)
    tr.left(90)

for i in range(3):

    tr.forward(100)
    tr.right(120)

tr.forward(300)
tr.right(120)
tr.forward(100)
tr.right(60)
tr.forward(200)
tr.left(180)
tr.forward(200)
tr.left(60)
tr.forward(100)
tr.left(30)
tr.forward(100)
tr.left(90)
tr.forward(200)

tr.speed(0)
# colors = ["red", "yellow", "green", "blue"]
#
# for i in range(500):
#     for color in colors:
#         tr.color(color)
#         fr = 50 + i
#         tr.forward(fr)
#         tr.left(91)


window.mainloop()


