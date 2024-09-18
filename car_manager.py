from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        self.all_cars = []
        self.move_speed = 0.1

    
    def create_car(self):
        random_choice = random.randint(1,6)
        if random_choice == 1:
            cars = Turtle("square")
            cars.penup()
            cars.shapesize(stretch_wid=1, stretch_len=2)
            cars.color(random.choice(COLORS))
            random_x = random.randint(50, 310)
            random_y = random.randint(-240, 240)
            cars.goto(random_x, random_y)
            cars.speed(self.move_speed)
            self.all_cars.append(cars)
        


    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)


    def car_speed_inc(self):
        self.move_speed += MOVE_INCREMENT



    
       