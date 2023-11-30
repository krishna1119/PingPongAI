import turtle
import numpy as np


class PongGame:
    def __init__(self):
        self.wn= turtle.Screen()
        self.wn.title("Pong")
        self.wn.bgcolor("black")
        self.wn.setup( width=800, height=600)
        self.wn.tracer(0)

        self.scorea=0
        self.scoreb=0

        self.button= turtle.Turtle



        self.paddle_a = turtle.Turtle()
        self.paddle_a.speed(0)
        self.paddle_a.shape("square")  #20x20 pixels by defaults
        self.paddle_a.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle_a.color("white")
        self.paddle_a.penup()
        self.paddle_a.goto(-350,0)

        self.paddle_b = turtle.Turtle()
        self.paddle_b.speed(0)
        self.paddle_b.shape("square")  #20x20 pixels by defaults
        self.paddle_b.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle_b.color("white")
        self.paddle_b.penup()
        self.paddle_b.goto(350,0)


        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("square")  #20x20 pixels by defaults

        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0,0)
        self.ball.dx=0.1 #move by 2 pixels
        self.ball.dy=0.1

        self.pen= turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle
        self.pen.goto(0,260)
        self.pen.write("Player A: 0  Player B: 0", align="center", font=("Courier",24,"normal"))

        #here is the action part, so i have to get the sction here, change it to a function
        self.wn.listen()
    # some erros is there i dont know what it is
    def movement(self, action):
        array = np.array(action)
        if np.array_equal(array, [1,0,0]):
            self.paddle_b_up()
        elif np.array_equal(array, [0,1,0]):
            self.paddle_b_down()
        self.wn.onkeypress(self.paddle_a_up,"w")
        self.wn.onkeypress(self.paddle_a_down,"s")

    def paddle_b_up(self):
        y=float(self.paddle_b.ycor())
        y+=0.5
        self.paddle_b.goto(self.paddle_b.xcor(), y)

    def paddle_b_down(self):
        y=self.paddle_b.ycor()
        y-=20
        self.paddle_b.sety(y)



    def paddle_a_up(self):
        y=self.paddle_a.ycor()
        y+=20
        self.paddle_a.sety(y)



    def paddle_a_down(self):
        y=self.paddle_a.ycor()
        y-=20
        self.paddle_a.sety(y)

    

       
    def run_game(self):
        while True:   #main game loop
            self.wn.update()
            action = [1,0,0]
            self.movement(action)

            self.ball.setx(self.ball.xcor()+ self.ball.dx)
            self.ball.sety(self.ball.ycor() + self.ball.dy)

    #border checking
            if self.ball.ycor()>290:
                self.ball.sety(290)
                self.ball.dy*=-1

            if self.ball.ycor()<-290:
                self.ball.sety(-290)
                self.ball.dy*=-1

            if self.ball.xcor()>390:
                self.ball.goto(0,0)
                self.ball.dx*=-1
                self.scorea+=1
                self.pen.clear()
                self.pen.write("Player A: " + str(self.scorea) + " Player B: " + str(self.scoreb), align="center", font=("Courier",24,"normal"))

            if self.ball.xcor()<-390:
                self.ball.goto(0,0)
                self.ball.dx*=-1
                self.scoreb+=1
                self.pen.clear()
                self.pen.write("Player A: " + str(self.scorea) + " Player B: " + str(self.scoreb), align="center", font=("Courier",24,"normal"))

    #collisions
   
            if (self.ball.xcor()>340 and self.ball.xcor() <350) and (self.ball.ycor()<self.paddle_b.ycor()+ 40 and self.ball.ycor()> self.paddle_b.ycor() -40):
                self.ball.setx(340)
                self.ball.dx*=-1.1

            if (self.ball.xcor()< -340 and self.ball.xcor() > -350) and (self.ball.ycor()<self.paddle_a.ycor()+ 40 and self.ball.ycor()> self.paddle_a.ycor() -40):
                self.ball.setx(-340)
                self.ball.dx*=-1.1

            if self.scorea==3 or self.scoreb==3:
                self.scoreUpdate()
                break

    def scoreUpdate(self):
        self.wn.clear()    
        while True:
            if self.scorea==3 or self.scoreb==3:       
   
                self.wn.bgcolor("black")
                if self.scorea==3:
                    self.pen.goto(0,0)
                    self.pen.write("Player A has won", align= "center", font=("Courier", 24,"normal"))
                else:
                    self.pen.goto(0,0)
                    self.pen.write("Player B has won", align= "center", font=("Courier", 24,"normal")) 


if __name__ == "__main__":
    game = PongGame()
    game.run_game()

