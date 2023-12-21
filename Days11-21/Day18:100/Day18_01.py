import turtle
# Trying different import methods

tim = turtle.Turtle()   # have to name the module and the class to call it


from turtle import Turtle

tom = Turtle()  # this saves having to do the 'turtle.' each time


from turtle import *    # imports everything, so it can be used as if it is in the current file,
# but makes it harder to see where methods came from

# alias a module
import turtle as t

# this is an alias, we can just write t to represent the entire module
ted = t.Turtle()


# on pycharm importing a module that isn't installed obviously won't work, but it's easy to install, just clicking the
# red bulb and you can install from there
import heroes
