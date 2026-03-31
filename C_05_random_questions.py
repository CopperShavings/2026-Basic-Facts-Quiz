import random


def generate_equation():
    # Random coefficients and constants
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 50)

    # Random operator
    op = random.choice(['+', '-'])

    # Generate equation string: "ax + b = c"
    equation = f"{a}x {op} {b} = {c}"
    return equation


# Generate and print 5 random equations
for _ in range(5):
    print(generate_equation())


# my_list = [
#     num_1 * num_2,  # Multiplication
#     num_1 - num_2,  # Subtraction
#     num_1 + num_2,  # Addition
#     num_1 / num_2  # Division
# ]
#
# print(my_list)