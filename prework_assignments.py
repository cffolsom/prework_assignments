def hello_name(user_name):
    """Simply says hello to a given username."""
    print("Hello, " + user_name.title() + "!")

def first_odds():
    """Calculates the odds from 0 - 100"""
    number = 0
    while number < 100:
        number += 1
        if (number % 2) == 1:
            print(number)

def max_num_in_list(a_list):

    """Gives the maximum number of a given list"""

    max_num = len(a_list)
    print(max_num)

def is_leap_year(a_year):

    """Calculates if the given year is a leap year"""
    if (a_year % 400 == 0) and (a_year % 100 == 0):
        return True
    elif (a_year % 4 ==0) and (a_year % 100 !=0):
        return True
    else:
        return False

def is_consecutive(b_list):
    """Calculates a list full of number to ensure that it's all consecutive"""
    return sorted(b_list) == list(range(min(b_list), max(b_list)+1))

