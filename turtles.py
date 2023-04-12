import turtle


#figure 1 

turtle.fillcolor("blue")
turtle.begin_fill()
turtle.right(45)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.end_fill()
turtle.done()

##########   figure 2  ########

turtle.circle(30)

turtle.penup()
turtle.goto((80,0))

turtle.pendown()
turtle.circle(30) 

turtle.penup()
turtle.goto((160,0))

turtle.pendown()
turtle.circle(30) 

turtle.penup()
turtle.goto((45,-30))

turtle.pendown()
turtle.circle(30) 

turtle.penup()
turtle.goto((125,-30))

turtle.pendown()
turtle.circle(30) 

turtle.done()



##########   figure 3  ########



turtle.goto(0,0)
turtle.setheading(0)
turtle.forward(200)
turtle.write("West")

turtle.penup()
turtle.goto(0,0)
turtle.pendown()

turtle.setheading(180)
turtle.forward(200)
turtle.write("East")

turtle.penup()
turtle.goto(0,0)
turtle.pendown()

turtle.setheading(90)
turtle.forward(200)
turtle.write("North")

turtle.penup()
turtle.goto(0,0)
turtle.pendown()

turtle.setheading(270)
turtle.forward(200)
turtle.write("South")

turtle.penup()

turtle.goto(-30,0)
turtle.pendown()
turtle.circle(30)

turtle.done()




##########   figure 4  ########


turtle.goto(0,0)
turtle.dot()

turtle.setheading(45)
turtle.forward(100)
turtle.dot()

turtle.penup()
turtle.goto(0,0)
turtle.pendown()

turtle.setheading(225)
turtle.forward(100)
turtle.dot()

turtle.penup()
turtle.goto(0,0)
turtle.pendown()

turtle.setheading(135)
turtle.forward(100)
turtle.dot()

turtle.penup()
turtle.goto(0,0)
turtle.pendown()

turtle.setheading(315)
turtle.forward(100)
turtle.dot()

turtle.setheading(90)
turtle.forward(145)


turtle.setheading(180)
turtle.forward(15)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.forward(30)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.forward(30)
turtle.penup()
turtle.forward(20)
turtle.penup()
turtle.forward(10)
turtle.pendown()

turtle.setheading(270)
turtle.forward(145)

turtle.setheading(0)
turtle.forward(15)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.forward(30)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.forward(30)
turtle.penup()
turtle.forward(20)
turtle.penup()
turtle.forward(10)

turtle.done()





##########   figure 5  ########

turtle.fillcolor("blue")
turtle.begin_fill()
turtle.goto(100,0)
turtle.goto(50,50)
turtle.goto(0,0)
turtle.end_fill()

turtle.goto(100,0)
turtle.goto(50,100)
turtle.goto(0,0)

turtle.done()


##########   figure 6  ########

turtle.forward(80)
print(turtle.position())

turtle.setheading(315)
turtle.forward(100)
print(turtle.position())


turtle.setheading(270)
turtle.forward(80)
print(turtle.position())


turtle.setheading(180)
turtle.forward(80)
print(turtle.position())


turtle.setheading(135)
turtle.forward(100)
print(turtle.position())

turtle.setheading(90)
turtle.forward(80)
print(turtle.position())

turtle.goto(150.71,-150.71)
turtle.penup()
turtle.goto(80,0)
turtle.pendown()
turtle.goto(70.71,-150.71)
turtle.goto(0,-80)
turtle.goto(150.71,-70.71)

turtle.done()












