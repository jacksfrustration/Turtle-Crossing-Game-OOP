FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.level=1
        self.hideturtle()
        self.color("black")
        self.update_scoreboard()

    def update_scoreboard(self):
        '''updates scoreboard'''
        self.clear()
        self.penup()
        self.goto(-50,250)
        self.write(f"Level: {self.level}",font=("Arial",24,"normal"))


    def add_point(self):
        '''adds a point'''
        self.score+=1
        self.level+=1
        self.update_scoreboard()

    def game_over(self):
        '''game over algorithm. will output total score'''
        self.clear()
        self.goto(-100,50)
        self.write(f"GAME OVER\n Score: {self.score}",font=("Arial",24,"normal"))


