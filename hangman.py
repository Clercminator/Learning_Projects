import json
import random
import string

f = open('words.json')
words = list(json.load(f))

def get_valid_word(words):
    word = random.choice(words) #randomly chooses a word
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_lowercase)
    used_letters = set() #what the user has guessed

    lives = int(input('Let\'s play hangman! How many tries you want to have? Type a number...'))

    #Getting user input
    while len(word_letters) > 0 and lives > 0:
        #letters used
        print('You have', lives, 'lives left and you have used these letters: ',''.join(used_letters))

        #what current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ',' '.join(word_list))

        user_letter = input('Guess a letter: ').lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives -1 #takes away a life for each wrong guess.
                print('Letter is not in word.')
                
        elif user_letter in used_letters:
            print('You have already used that letter. Try another one.')
        else:
            print('Invalid character. Try a new letter.')
    
    #gets here when len(word_letters == 0 or when lives == 0)
    if lives == 0:
        print('Sorry! You have died. The word was', word,'.')
    else:
        print('Congrats! You have correctly guessed the word, ',word,'.')

hangman()