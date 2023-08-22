from turtle import Turtle
from scoreboard import Scoreboard
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

scoreboard=Scoreboard()
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.number=8
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE
        self.generate_car()
        self.hideturtle()


    def generate_car(self):
        '''create a nwe car. random color and location. car is only generated everytime the random chance value is 1
        this is done in order to speed up car generation after every level gets acccomplished'''
        random_chance=random.randint(1,self.number)
        if random_chance==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        '''move cars'''
        for car in self.all_cars:
            car.setheading(180)
            car.forward(self.car_speed)

    def increase_speed(self):
        '''speed is increased by 10 everytime this funcction gets triggered'''
        self.car_speed+=MOVE_INCREMENT
        self.number-=1

