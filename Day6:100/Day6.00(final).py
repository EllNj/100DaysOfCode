"""this was the answer for the final project today, it was a task on reeborgs world
the code doesnt work much without the s-ecific task reeborgs world "maze"""""

def turn_right():
    for i in range(3):
        turn_left()


if not wall_on_right():
   while not wall_on_right():
       turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif wall_in_front():
        turn_left()
    else:
        move()