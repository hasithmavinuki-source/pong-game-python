from turtle import Turtle

class Ball(Turtle) :
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("pink")
        self.penup()
        self.x_value = 15
        self.y_value = 15

    def move(self):

        new_x = self.xcor() + self.x_value
        new_y = self.ycor() + self.y_value
        self.goto(new_x , new_y)

    def bounce_vertical(self):
        self.y_value *= -1

    def bounce_horizontal(self):
        self.x_value *= -1

    def reset_position(self):
        self.goto(0,0)
        self.x_value *= -1