import random

def pc_guess():
    low = int(input("Give me a range of numbers and I will guess what number you're thinking.\
                        First give me a low number..."))
    high = int(input("Thanks! Now give me a high number..."))
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H), too low (L), or correct?').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Amazing! The pc guessed your number, {guess}, correctly.')
pc_guess()