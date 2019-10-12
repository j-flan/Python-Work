import turtle  # graphing library
newlist = [4, 2, 5, 1, 3]  # this is the data to graph

wn = turtle.Screen()
chartT = turtle.Turtle()
wn.setworldcoordinates(-1, -1, 6, 6)
chartT.hideturtle()
# chartT.width(width=5)  using default width
# chartT.shape(name='turtle') a cute turtle!

chartT.up()         # pick up the pen
chartT.goto(0,0)    # move the pen to this location
chartT.down()       # put the pen on the drawing surface
chartT.goto(6, 0)   # draw over to this location
chartT.up()         # pick up the pen

chartT.goto(-1,0)   # move the pen to the bottom left margin of the graph
chartT.write("0", font=("Helvetica",16,"bold")) # write 0 to the left of the y axis
chartT.goto(-1,5)   # move the pen to the highest point of the left margin
chartT.write("5", font=("Helvetica", 16, "bold"))# write 5 to the left of the y axis 

# now iterate through the list and graph it
for index in range(len(newlist)):
    chartT.goto(index, -1)
    chartT.write(str(newlist[index]), font=("Helvetica",16,"bold"))

    chartT.goto(index,0)
    chartT.down()
    chartT.goto(index, newlist[index])
    chartT.up()
wn.exitonclick()
