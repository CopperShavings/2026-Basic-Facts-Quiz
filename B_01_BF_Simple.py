import random
import string
from random import randint
#➕✖️➖➗

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

- To begin, choose the number of questions you would
 like to answer (or press <enter> for infinite mode).


- Then you need to pick whether you would like to use default 
parameters (1, 12) or pick your own!

If you decide to choose your own, select a low number and 
a high number (high must be more than low.)


- You need to try guess get as many answers correct as possible!
You'll be answering addition, subtraction, multiplication, and 
division questions

- Select <xxx> to end the game.

Good luck!


    """)


# int check
def int_check(question):
    while True:
        response = input(question).lower()
        error = "Please enter an integer between 1 and 100."

        # check for inf mode / exit code
        if response == exit_code:
            return response

        high = 100
        low = 1

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(response)

            # Check the integer is not too low
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
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
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")
if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

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

    answer_add = x+y

    print(f"{x}+{y} = ")





    # print("Spoiler Alert: ", answer)
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