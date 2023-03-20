from turtle import *
from time import *
from random import *

SPACE = 20
MAX_X, MAX_Y = 450, 275
RIGHT, UP, LEFT, DOWN = 0, 90, 180, 270

class Board:

    def __init__(self):
        self.a = [0,0,0,0]
        self.b = [0,0,0,0]
        self.c = [0,0]
        self.d = -MAX_X/2
        self.e = [[0,0,0,0,0],[0,0,0,0,0]]
        self.f = [40,1]
        self.g = ["cyan","lime"]
        self.h = [0,0]
        self.i = [[0,0],[0,0]]
        self.j = 0
        self.k = "left"

    def board_settings(self):
        self.a[0] = Screen()
        self.a[0].screensize(MAX_X,MAX_Y)
        self.a[0].bgcolor('black')
        self.a[0].listen()
        self.a[0].title("Pong")
        self.a[0].setup(900,550)
        self.a[0].tracer(0)

    def score(self):
        for a in range(1,3):
            self.b[a] = Turtle()
            self.b[a].hideturtle()
            self.b[a].color("maroon")
            self.b[a].penup()
            self.b[a].goto( self.d, MAX_Y - 3*SPACE)
            self.b[a].pendown()
            self.b[a].write(f"{self.c[a-1]}",False,"center",("courier",30,"normal"))
            self.d-=self.d*2
    
    def hold_screen(self):
        self.a[0].exitonclick()
    
    def mid_line(self):
        self.b[0] = Turtle()
        self.b[0].color('white')
        self.b[0].width(3)
        self.b[0].penup()
        self.b[0].setposition(0, MAX_Y - SPACE + 9)
        self.b[0].hideturtle()
        self.b[0].setheading(DOWN)
        while self.b[0].ycor() > -MAX_Y + SPACE:
            self.b[0].pendown()
            self.b[0].color("dark khaki")
            self.b[0].forward(SPACE - 5)
            self.b[0].penup()
            self.b[0].forward(SPACE - 5)

    def players(self):
        for a in range(2):
            for b in range(5):
                self.e[a][b] = Turtle("square")
                self.e[a][b].color(f"{self.g[a]}")
                self.e[a][b].penup()
                self.e[a][b].setheading(90)
                self.e[a][b].goto(self.f[1]*(MAX_X-SPACE*2),self.f[0])
                self.f[0] -=SPACE
            self.f[1] = -1
            self.f[0] = 40 

    def ball(self):
        self.b[3] = Turtle("circle")
        self.b[3].color("blue violet")
        self.b[3].penup()
        self.b[3].speed(1)
        self.b[3].setheading(0)

    def ball_moving(self):
        self.b[3].forward(SPACE)

    def score_up(self):
        if self.b[3].xcor() >= MAX_X - SPACE:
            self.b[3].setheading(0)
            self.b[1].clear()
            self.c[0] += 1
            self.b[1].write(f"{self.c[0]}",False,"center",("courier",30,"normal"))
        elif self.b[3].xcor() <= -MAX_X + SPACE:
            self.b[2].clear()
            self.b[3].setheading(180)
            self.c[1] += 1
            self.b[2].write(f"{self.c[1]}",False,"center",("courier",30,"normal"))
    
    def refresh_screen(self):
        self.a[0].update()
        sleep(0.05)

    def goal(self):
        if self.b[3].xcor() >= MAX_X or self.b[3].xcor() <= -MAX_X:
            return True

    def center_ball(self):
        self.b[3].goto(0,0)

    def hit_borders(self):
        if self.b[3].ycor() >= MAX_Y or self.b[3].ycor() <= - MAX_Y:
            return True
    
    def bounce_back(self):
        self.b[3].setheading(-self.b[3].heading())

    def hit_player(self):
        for a in range(len(self.e)):
            for b in range(len(self.e[0])):
                if self.e[a][b].distance(self.b[3]) <=20:
                    return True
        

    def reverse_direction(self):
        if self.b[3].heading() >= 0 and self.b[3].heading() < 90:
            self.b[3].setheading(self.b[3].heading() + randint(120,150))
            self.b[3].forward(SPACE/2)
        elif self.b[3].heading() >= 90 and self.b[3].heading() < 180:
            self.b[3].setheading(self.b[3].heading() - randint(120,150))
            self.b[3].forward(SPACE/2)
        elif self.b[3].heading() >= 180 and self.b[3].heading() < 270:
            self.b[3].setheading(self.b[3].heading() + randint(120,150))
            self.b[3].forward(SPACE/2)
        elif self.b[3].heading() >= 270 and self.b[3].heading() < 360:
            self.b[3].setheading(self.b[3].heading() - randint(120,150))
            self.b[3].forward(SPACE/2)

    def up(self):
        for a in self.e[0]:
            a.forward(SPACE)

    def down(self):
        for a in self.e[0]:
            a.backward(SPACE)

    def up_(self):
        for a in self.e[1]:
            a.forward(SPACE)

    def down_(self):
        for a in self.e[1]:
            a.backward(SPACE)

    def win(self):
        if self.c[0] == 10 or self.c[1] == 10:
            return True
    
    def end(self):
        self.j = Turtle()
        self.j.hideturtle()
        self.j.color("white")
        self.j.penup()
        self.b[0].clear()
        if self.c[1] == 10:
            self.k = "right"
        self.j.write(f"The player on the {self.k} won!",False,"center",("courier",20,"normal"))
        return False

