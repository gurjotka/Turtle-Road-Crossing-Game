import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
car = CarManager()
score = Scoreboard()


screen.listen()
screen.onkey(tim.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    for vehicles in car.all_cars:
        if vehicles.distance(tim) < 20:
            game_is_on = False
            score.game_over()    
        

    if tim.ycor() > 250:
        score.update_scoreboard()
        tim.goto(0,-280)
        car.car_speed_inc()
        

    
    

screen.exitonclick()