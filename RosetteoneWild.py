import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow"]
# Ask the user for the number of circles in their rosette, default to 6
number_of_circles = int(turtle.numinput("Number of circles",
                                        "How many circles in your rosette?", 6))
for x in range(number_of_circles):
    t.pencolor(colors[1])
    t.circle(50)
    t.pencolor(colors[0])
    t.circle(100)
    t.left(360/number_of_circles)
turtle.done()