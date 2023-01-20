# print("Functions module will get executed as soon as import functions is executed")
import numpy as np

FREEZING_POINT = 0
BOILING_POINT = 100

FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
     to-do-items.
     """
    # file = open(FILEPATH, 'r')
    with open(FILEPATH, 'r') as file_local:
        todos_local = file_local.readlines()
        #   file.close()
        return todos_local


# print(help(get_todos))

# Multiline Text can be written using 3 double quotes too. This does carriage return on its own
text = """
Principles of productivity
Managing your inflow
Systemizing everything that repeats
"""
# print(text)

# vs

text1 = "Principles of productivity \n" \
        "Managing your inflow \n" \
        "Systemizing everything that repeats \n"


# print(text1) # you hv to enter \n to get text on separate lines


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a text file by passing the list of items to write
     """
    # file = open(FILEPATH, 'w')
    with open(FILEPATH, 'w') as file:
        file.writelines(todos_arg)
    #   file.close()


def find_state_of_water(tempr):
    if tempr <= FREEZING_POINT:
        return "Solid"
    elif FREEZING_POINT < tempr < BOILING_POINT:
        return "Liquid"
    else:
        return "Gas"


def count(phrase):
    return phrase.count('.')


def convert(feet, inches):
    meter = float(inches) / float(feet)
    meter = np.round(meter, 2)
    return meter
