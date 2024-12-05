#!/usr/bin/env python3

# looping.py

def happy_new_year():
    count = 10
    while count > 0:
        print(count)
        count -= 1
    print("Happy New Year!")


def square_integers(int_list):
    return [x ** 2 for x in int_list]


