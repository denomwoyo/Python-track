"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""
EXPECTED_BAKE_TIME=40
print(EXPECTED_BAKE_TIME)
#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.


#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    elapsed_time=EXPECTED_BAKE_TIME-elapsed_bake_time
    return (elapsed_time)

#TODO: Define the 'preparation_time_in_minutes()' function below.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.
    The function multiplies the number of layers by 2 minutes to get the 
    preparation time needed"""
    preparation_time=number_of_layers*2
    return (preparation_time)
    

#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time.
    The function takes the number of layers multiplies it by 2 minutes then adds 
    the elapsed bake time to get the total time"""
    elapsed_time=number_of_layers*2 + elapsed_bake_time
    return (elapsed_time)


# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
