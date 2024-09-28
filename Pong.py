from turtle import Turtle

#class to create the ping pong ball
class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.05

#movement of the ball
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

#physics for the bounce of the ball
    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def y_bounce(self):
        self.y_move *= -1


    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.05
        self.x_bounce()
