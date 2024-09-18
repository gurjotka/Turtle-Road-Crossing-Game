from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(0,-280)
        self.setheading(90)
        self.x_move = 10
        self.y_move = 10


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        self.speed("fastest")