import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle=Player()
cars=CarManager()
screen.listen()
score=Scoreboard()
screen.onkey(key="Up",fun=turtle.move_up)
screen.onkey(key="Down",fun=turtle.move_down)
game_is_on = True
print(turtle.pos())
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.generate_car()
    cars.move_cars()
    for car in cars.all_cars:
        if turtle.distance(car)<20:
            score.game_over()
            game_is_on=False
    if turtle.is_at_finish_line():
        turtle.generate_player()
        cars.increase_speed()
        score.add_point()



screen.exitonclick()


