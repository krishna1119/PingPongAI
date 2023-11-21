import turtle
wn= turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup( width=800, height=600)
wn.tracer(0)

scorea=0
scoreb=0

button= turtle.Turtle

#in a single game
#they learn 
#but wai , they have to 

#reset
#reward
#play(action)
#game_iteration
#is_collision


paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")  #20x20 pixels by defaults
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")  #20x20 pixels by defaults
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)


ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")  #20x20 pixels by defaults

ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.1 #move by 2 pixels
ball.dy=0.1

pen= turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier",24,"normal"))

def paddle_b_up():
     y=paddle_b.ycor()
     y+=20
     paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_b_up,"Up")

def paddle_b_down():
     y=paddle_b.ycor()
     y-=20
     paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_b_down,"Down")

def paddle_a_up():
     y=paddle_a.ycor()
     y+=20
     paddle_a.sety(y)

wn.listen()
wn.onkeypress(paddle_a_up,"w")

def paddle_a_down():
     y=paddle_a.ycor()
     y-=20
     paddle_a.sety(y)

wn.listen()
wn.onkeypress(paddle_a_down,"s")

       

while True:   #main game loop
    wn.update()
   
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        scorea+=1
        pen.clear()
        pen.write("Player A: " + str(scorea) + " Player B: " + str(scoreb), align="center", font=("Courier",24,"normal"))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        scoreb+=1
        pen.clear()
        pen.write("Player A: " + str(scorea) + " Player B: " + str(scoreb), align="center", font=("Courier",24,"normal"))

    #collisions
   
    if (ball.xcor()>340 and ball.xcor() <350) and (ball.ycor()<paddle_b.ycor()+ 40 and ball.ycor()> paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx*=-1.1

    if (ball.xcor()< -340 and ball.xcor() > -350) and (ball.ycor()<paddle_a.ycor()+ 40 and ball.ycor()> paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx*=-1.1

    if scorea==3 or scoreb==3:
        break
wn.clear()    
while True:
  if scorea==3 or scoreb==3:       
   
    wn.bgcolor("black")
    if scorea==3:
         pen.goto(0,0)
         pen.write("Player A has won", align= "center", font=("Courier", 24,"normal"))
    else:
         pen.goto(0,0)
         pen.write("Player B has won", align= "center", font=("Courier", 24,"normal")) 
