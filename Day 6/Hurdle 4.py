def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    count=0
    while not right_is_clear():
        move()
        count+=1
    turn_right()
    move()
    turn_right()
    while count>0:
        move()
        count-=1
    turn_left()
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
