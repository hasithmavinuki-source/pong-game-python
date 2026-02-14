from turtle import Turtle
from turtle import Screen
from padle import Paddle
from ball import Ball
from score import Score
import time


paddle_1 = Paddle((350 , 0))
paddle_2 = Paddle((-350 , 0))

my_ball = Ball()

score_board_1 = Score((40,200))
score_board_2 = Score((-40,200))
winner = Score((-150,0))
score_banner = Score((0 , 240))
score_banner.score_banner()

#creating the game screen

game_screen = Screen()
game_screen.setup(800,600)
game_screen.bgcolor("aquamarine4")
game_screen.title("My Pong !!")
game_screen.tracer(0)

#Draw the middle line
margine = Turtle()
margine.hideturtle()
margine.penup()
margine.goto(0 , 240)
margine.pendown()
margine.setheading(270)
margine.forward(600)

#key commands
game_screen.onkeypress(paddle_2.go_up , "w")
game_screen.onkeypress(paddle_2.go_down , "s")
game_screen.onkeypress(paddle_1.go_up , "Up")
game_screen.onkeypress(paddle_1.go_down , "Down")
game_screen.listen()

interval = 0.1
game_is_on = True
while game_is_on :
    time.sleep(interval)
    game_screen.update()
    my_ball.move()

    if my_ball.ycor() > 280 or my_ball.ycor() < -270 :
        my_ball.bounce_vertical()
    if my_ball.distance(paddle_1) < 60 and my_ball.xcor() > 320 and my_ball.x_value > 0 :
        my_ball.bounce_horizontal()
        interval -= 0.004
        score_board_1.update_score()
    if my_ball.distance(paddle_2) < 60 and my_ball.xcor() < -320 and my_ball.x_value < 0:
        my_ball.bounce_horizontal()
        score_board_2.update_score()
        interval -= 0.004
    if my_ball.xcor() > 400 :
        my_ball.reset_position()
        score_board_2.update_score()
    if my_ball.xcor() < -400:
        my_ball.reset_position()
        score_board_1.update_score()
    if score_board_1.score >= 15 :
        winner.winner_player_r()
        my_ball.hideturtle()
        my_ball.goto(0,0)

    if score_board_2.score >= 15 :
        winner.winner_player_l()
        my_ball.hideturtle()
        my_ball.goto(0, 0)

game_screen.exitonclick()
