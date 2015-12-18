import turtle

def makeDecagon(myTurtle, side):
	myTurtle.forward(side)
	myTurtle.left(36)
	myTurtle.forward(side)
	myTurtle.left(36)
	myTurtle.forward(side)
	myTurtle.left(36)
	myTurtle.forward(side)
	myTurtle.left(36)
	myTurtle.forward(side)
	myTurtle.left(36)
	myTurtle.forward(side)
	myTurtle.left(36)
	myTurtle.forward(side)
        myTurtle.left(36)
	myTurtle.forward(side)
        myTurtle.left(36)
	myTurtle.forward(side)
        myTurtle.left(36)
	myTurtle.forward(side)
        myTurtle.left(36)

logic = turtle.Turtle()
logic.forward(160)
logic.right(150)

length = 100
while length >= 0:
	makeDecagon(logic, length)
	logic.forward(10)
	length = length - 1

turtle.exitonclick()
