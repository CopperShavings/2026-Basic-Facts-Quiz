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

def int_check2(question):
    error = "Please enter an integer between 1 and 100."
    high = 10000
    low = -11111

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
incorrect = 0
correct = 0

feedbackgood_list = ["Correct - Good job!", "Correct - Nice work!", "Correct - Cool!", "Correct - Great answer!", "Correct! - Awesomeness!", "Correct! - Wow!"]
feedbackbad_list = ["Incorrect - You'll get em next time!", "Incorrect - Uh oh!", "Incorrect - Nice try", "Incorrect - There's always next time!"]

history = [ ]
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

    # when user choice is the exit code, break loop
    if mode == exit_code:
        break

    rounds_played += 1


    # if users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1


# create the question for the user...
    symbol = random.choice(symbols_list)
    feedback_bad = random.choice(feedbackbad_list)
    feedback_good = random.choice(feedbackgood_list)
    x = random.randint(num1, num2)
    y = random.randint(num1, num2)

    if symbol == '+':
        answer = x + y
    elif symbol == '-':
        answer = x - y
    elif symbol == 'x':
        answer = x * y
    elif symbol == '/':
        x = x * y  # makes it divisible
        answer = x // y

    if num1 < num2 and symbol == '-':
            x, y = y, x

    print("Spoiler Alert: ", answer)
    user_guess = int_check2(f"{x} {symbol} {y} = ")


    if user_guess == answer:
        print (feedback_good)
        correct += 1
        continue

    if user_guess == exit_code:
        see_stats = string_checker("You selected the exit code. Would you like to see your stats?")
        if see_stats == "yes":

        else:
            break

    else:
        print (feedback_bad)
        incorrect += 1
        continue


# #calc stats
    if exit_code or rounds_played > 0:

        questions_correct = rounds_played - incorrect
        questions_incorrect = rounds_played - correct
        percent_correct = questions_correct / rounds_played * 100
        percent_wrong = questions_incorrect / rounds_played * 100
        average_score = sum(rounds_played)/len(rounds_played)




        final_results = ("\n 📈📊 Statistics 📊📉"
                         f"Number of questions answered: {rounds_played}"
                         f"Correct: {questions_correct} || Incorrect: {questions_incorrect}"
                         f"Overall, you got {percent_correct}% correct | {percent_wrong}% incorrect | {average_score}")

        history.append(final_results)






        # Display the game history on request
        see_history = string_checker("Do you want to see your stats? ")
        print()
        if see_history == "yes":
            for item in history:
                print(item)

        print ()
        print("Thank you for playing")

    else:
        print("xxx! Uh oh - you chickened out !xxx")


