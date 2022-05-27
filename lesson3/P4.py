import re


def my_f(x,y):
    try:
        total = x ** y
    except TypeError:
        return 'enter positive and negative number'
    return total

print(my_f(4, -2))