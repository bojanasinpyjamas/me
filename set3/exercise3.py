"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random

def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    while True:
        user_input = input(message)
        try:
            k = int(user_input)
            return k
        except Exception:
            print(f"Put in an actual number ({user_input})")


def super_asker(low, high):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    """
    while True:
        try:
            m = int(input(f"Enter a number between {low} and {high}:"))
            print(m)  
            if m in range (low, high):
                return m
            else:
                print("Try a number in the range")
        except Exception:
            print("Try a number")

def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print("\nNumber guessing game?!")
    lowerBound = super_asker(-1000, 1000)
    upperBound = super_asker(lowerBound + 2,1000)
    actualNumber = random.randint(lowerBound, upperBound)
    while True:
        guessedNumber = not_number_rejector(f"OK then, a number between {lowerBound} and {upperBound}: ")
        if guessedNumber == actualNumber:
            return "You got it!"
        elif guessedNumber < actualNumber:
            print("Too smol, try again")
        else:
            print("Too big, try again")
    # the tests are looking for the exact string "You got it!". Don't modify that!

if __name__ == "__main__":
    print(advancedGuessingGame())
