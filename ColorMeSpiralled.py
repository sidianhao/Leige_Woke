import turtle                     # Set up turtle graphics
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
# Set up a list of any 8 valid python color names
colors=['red', 'yellow', 'blue', 'green', 'orange',
        'purple', 'white', 'gray', 'brown', 'sea green']
# Ask the user for the number of sides, between 1 and 8, with a default of 4
your_name = turtle.textinput("Enter your name", "What is your name? ")
sides = int(turtle.numinput("Number of sides",
            "How many sides do you want (1-8)?", 4,1,8))
times = int(turtle.numinput('loops of times','Please enter the number of loops',100))
for x in range(times):
    t.pencolor(colors[x % sides]) # Only use the right number of sides
    t.penup()
    t.forward(x * 3 / sides + x)  # Change the size to match number of sides
    t.pendown()
    t.left(360 / sides + 1)       # Turn 360 degrees/number of sides, plus 1
    t.write(your_name, font = ("Arial", int( (x + 4) / 4), "bold") )   # Make the pen larger as it goes outward
turtle.done()