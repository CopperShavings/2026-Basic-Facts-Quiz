import random

def generate_equation():
    # Random coefficients and constants
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 50)

    # Random operator
    op = random.choice(['+', '-', 'x', '/'])

