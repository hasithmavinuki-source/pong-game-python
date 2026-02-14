from turtle import Turtle

class Paddle(Turtle) :
    def __init__(self , position):
        super().__init__()
        self.shape("square")
        self.color("orange")
        self.shapesize(5 , 1 ,1)
        self.penup()
        self.speed(0)
        self.goto(position)

    def go_up(self):
        if self.ycor() <= 220 :
            new_y = self.ycor() + 60
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() >= -220:
            new_y = self.ycor() - 60
            self.goto( self.xcor() , new_y)


