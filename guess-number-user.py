import random

# 3 ways to concatenate strings
#name = David
#print("subscribe to" + name)
#print("subscribe to {}".format(name))
#print(f"subscribe to {name}"")


def number(x):
    random_number = random.randint(0, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 0 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    print(f'Amazing! You have guessed the number {random_number} correctly.')

number(10)