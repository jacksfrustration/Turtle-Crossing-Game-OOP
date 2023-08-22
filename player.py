from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.generate_player()


    def generate_player(self):
        '''generates player at startup position'''
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        ''''moves the player every time this function is triggered'''
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        '''if player's position is not in the bottom corner then the player moves backwards each time this function is triggered'''
        if self.pos()[1]>-180:
            self.backward(MOVE_DISTANCE)
    def is_at_finish_line(self):
        '''returns if the current y position of player reaches the top of the screen'''
        return self.ycor()>FINISH_LINE_Y
