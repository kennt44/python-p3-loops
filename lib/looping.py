#!/usr/bin/env python3

def happy_new_year():
    # code goes here!def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")
    pass

def square_integers(int_list):
    # code goes here!def square_integers(integers):
    return [x ** 2 for x in integers]

    pass

def fizzbuzz():
    # code goes here!def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    pass
