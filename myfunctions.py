import turtle

bob = turtle.Turtle()

def jump(x, y):
 bob.penup()
 bob.goto(x, y)
 bob.pendown()



def house(x, y):
    jump(x, y)
    bob.color("orange")
    bob.begin_fill()
    for times in range(4):
       bob.forward(120)
       bob.left(90)
    bob.end_fill()


    jump(x, y + 120)
    bob.color("brown")
    bob.begin_fill()
    bob.goto(x + 60, y + 190)
    bob.goto(x + 120, y + 120)
    bob.goto(x,y + 120)
    bob.end_fill()

    jump(x  + 45, y)
    bob.color("brown")
    bob.begin_fill()
for times in range(2):
    bob.forward(30)
    bob.left(90)
    bob.forward(60)
    bob.left(90)
    bob.end_fill()


                    
def cloud(x, y):
  bob.color("white")
  for times in range(3):
      jump(x + times  * 30, y)
      bob.begin_fill()
      bob.circle(25)
      bob.end_fill()


      
# Sun design
def sun(x,y):
  jump(x,y)
  bob.color("yellow")
  bob.begin_fill()
  bob.circle(40)
  bob.end_fill

def grass(x,y):
    jump(x, y)
    bob.color("green")
    bob.begin_fill()
    for times in range(2):
      bob.forward(800)
      bob.left(90)
      bob.forward(150)
      bob.left(90)
      bob.end_fill()


def lake(x, y):
    jump(x, y)
    bob.color("blue")
    bob.begin_fill()
    for times in range(2):
        bob.forward(180)
        bob.left(90)
        bob.forward(60)
        bob.left(90)
        bob.end_fill()


def mountain(x, y):
     jump(x, y)
     bob.color("gray")
     bob.begin_fill()
     bob.goto(x + 100, y + 180)
     bob.goto(x + 200, y)
     bob.goto(x, y)
     bob.end_fill()

     bob.hideturtle()
