from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-150, 250)
        self.level = 1
        self.write(f"LEVEL {self.level}", align="center", font=FONT)
        self.hideturtle()


    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.hideturtle()
        self.write(f"GAME OVER", align="center", font=FONT)


    def update_scoreboard(self):
        self.clear()
        self.penup()
        self.goto(-150, 250)
        self.hideturtle()
        self.level += 1
        self.write(f"Level {self.level}", align="center", font=FONT)

    

