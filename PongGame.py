from data import *
from turtle import Screen
a=Board()
b=Screen()
b.onkey(a.up,"Up")
b.onkey(a.down,"Down")
b.onkey(a.up_,"w")
b.onkey(a.down_,"s")
a.board_settings()
a.mid_line()
a.players()
a.ball()
a.score()
c = True
while c:
    a.ball_moving()
    if a.hit_player():
        a.reverse_direction()
    a.refresh_screen()
    if a.hit_borders():
       a.bounce_back()
    if a.goal():
        a.score_up()
        a.center_ball()
    if a.win():
        c = a.end()

a.hold_screen()