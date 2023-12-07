import random

def winner(player, opponent):
    #return true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
def play():
    user = input("What's your choice?\n 'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r','p','s'])
# r>s, s>p, p>r
    if user == computer:
        return 'It\'s a tie.'
    if winner(user, computer):
        return 'You won!'
    return 'You lost!'

print(play())

