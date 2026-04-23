import random
import operator
import string
from random import randint
#➕✖️➖➗📄♾️✅

# string checker (y/n)
def string_checker(question, valid_ans=("yes", "no")):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item


            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()

# game instructions - how to play
def instructions():
    """Prints instructions"""

    print("""
 *** Instructions ****

📄 -  To begin, choose the number of questions you would
 like to answer (or press <enter> for infinite mode).
--------

📄 -  Then you need to pick whether you would like to use default 
parameters (1, 12) or pick your own!

If you decide to choose your own, the numbers you pick must be
between 1 and 100.
--------

📄 - You need to try get as many answers correct as possible!
You have one guess per question, so be careful with your answer!

You'll be answering addition, subtraction, multiplication, and 
division questions
--------

📄 - Select <xxx> to end the game.

Good luck!

    """)

# int check
def int_check(question):
    error = "Please enter an integer between 1 and 100."
    high = 100
    low = 1

    while True:
        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        # check for inf mode / exit code
        if to_check == exit_code:
            return exit_code

        try:
            response = int(to_check)

            if response < low or response > high:
                print(error)
            # if the response is valid, return it
            else:
                return response


        except ValueError:
            print(error)


# Main routine starts

# Initialise game variables
mode = "regular"
rounds_played = 0
num_rounds = 0
end_game = "no"
feedback = ""
symbols_list = ['x', '+', '-', '/']
game_history = [ ]
score = 0
exit_code = 'xxx'

# Welcome the user
print()
print("➕➖.. Welcome to: Basic Facts Quiz! ..✖️➗")
print()

# Give user the option to see instructions
# Checks user enters yes (y) or no (n)
want_instructions = string_checker("Do you want to read the instructions?")
if want_instructions == "yes":
    instructions()

# Ask for the number / amount of questions the user would
# like to answer, or give them the option to select (inf mode)

print()
num_rounds = int_check("How many questions would you like? Push <enter> for infinite mode: ")
if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5
    print("Infinite mode chosen")

else:
    print(f"{num_rounds} round/s chosen")


# ask user if they want to customise the number range
# Let the user select default parameters (1, 12) or let them choose their own

print()
default_params = string_checker("Would you like to use default parameters (1 - 12)? ")
if default_params == "yes":
        num1 = 1
        num2 = 12
else:
    print()
    num1 = int_check(question="Num 1?: ")
    num2 = int_check(question="Num 2?: ")

# Game loop starts here

while rounds_played < num_rounds:

    # Rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n♾️️♾️ Question {rounds_played + 1} (Infinite Mode) ♾️♾️"
    else:
        rounds_heading = f"\n❓❓ Question {rounds_played + 1} of {num_rounds} ❓❓"

    print(rounds_heading)
    print()

# create the question for the user...
    x = random.randint(num1, num2)
    y = random.randint(num1, num2)

    if symbols_list == '+':
        answer = x+y
    elif symbols_list == '-':
        answer = x-y
    elif symbols_list == 'x':
        answer = x*y
    elif symbols_list == '/':
        answer = x/y



    print()
    user_guess = int_check(f"{x}{symbols_list}{y} = ")
    if user_guess == answer:
        print ("correct answer!")
    else:
        print(f"incorrect...")





    # print("Spoiler Alert: ", correct_answer)
    #
    # guess = ""
    # while guess != answer:
    #
    #     # ask the user to guess the number
    #     guess = int_check(question="Guess :")
    #
    #     # check that they don't want to quit
    #     if guess == "xxx":
    #         # set end_game to use so that outer loop can be
    #         end_game = "yes"
    #         break
    #


# Stats here

# if rounds_played > 0:
#     rounds_won = rounds_played - rounds_tied - rounds_lost
#     percent_won = rounds_won / rounds_played * 100
#     percent_lost = rounds_lost / rounds_played * 100
#     percent_tied = 100 - percent_won - percent_lost