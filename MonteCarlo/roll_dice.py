import random
import matplotlib.pyplot as plt

def rolldice():
    roll = random.randint(1,100)

    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100 > roll > 50:
        return True
#49% chance of winning this game.

def simple_bettor(funds, initial_wager, wager_count):
    value = funds #How much money they have to bet
    wager = initial_wager #How many bets they do

    wX = []
    vY = []

    current_wager = 0

    while current_wager < wager_count:
        if rolldice():
            value += wager
            wX.append(current_wager)
            vY.append(value)
        else:
            value -= wager
            wX.append(current_wager)
            vY.append(value)

        current_wager += 1
    
    if value <= 0:
        value = 'broke'    
    #print('Funds: ', value)
    plt.plot(wX,vY)

x = 0
while x < 100: #How many simulations.
    simple_bettor(10000,100,10000) #100 people have 10.000 funds to bet 10.000 times.
    x += 1

plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()