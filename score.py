from turtle import Turtle

class Score(Turtle) :
    def __init__(self , position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.score = 0

    def score_banner(self) :
       self.write(arg = "SCORE", move=False, align = "center" , font=("Times New Roman", 32, "normal"))


    def update_score(self) :
        self.clear()
        self.score += 1
        self.write(arg= f"{self.score}", move = False, font = ("Times New Roman", 28, "normal") )

    def winner_player_r (self) :
        self.write(arg="GAME OVER\nPlayer R is the Winner !! ", move=False, font=("Times New Roman", 28, "normal"))

    def winner_player_l (self) :
        self.write(arg="GAME OVER\nPlayer L is the Winner !! ", move=False, font=("Times New Roman", 28, "normal"))

