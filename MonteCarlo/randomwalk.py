import random

#random walk function: There are two ways to create this function.

def random_walk_1(n): #n is the number of blocks to walk.
    """Return coordinates after 'n' block random walk."""
    #Your initial position in the map is (0,0)
    x = 0
    y = 0 
    for i in range(n):
        step = random.choice(['N','S','E','W'])#a random step to any of the four possible directions.
        if step == 'N':
            y = y + 1
        elif step == 'S':
            y = y - 1
        elif step == 'E':
            x = x + 1
        else:
            x = x - 1
    return (x,y) #return the coordinates.

#to test the function let's do 25 random walks of 10 random steps each one.   
for i in range(25):
    walk = random_walk_1(10)
    print(walk, "Distance from home ", abs(walk[0]) + abs(walk[1]))#abs is absolute value and it's used because we want to know distance.


def random_walk_2(n):
    """Return coordinates after 'n' block random walk."""
    #Your initial position in the map is (0,0)
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0,1),(0,-1),(1,0),(-1,0)])#randomly choose a pair of numbers.
        x += dx # == x = x + dx
        y += dy # == y = y + dy
    return (x,y)

for i in range(25):
    walk = random_walk_2(10)
    print(walk, "Distance from home ", abs(walk[0]) + abs(walk[1]))#abs is absolute value and it's used because we want to know distance.

#Now that we have the random walk function, we'll try to answer the following question.
"""¿What's the longest random walk you can take so that on average you will end up 4 blocks or fewer from home?"""

#To answer that question, we'll simulate 100.000 random walks for each walk size.
number_of_randomwalks = 100000

#Let's estimate the probability you will walk home for walks of length 1 to 30 blocks.
for walk_length in range(1, 31): #the range function stops before the final number.
    no_transport = 0 #A counter to keep track of the number of walks 4 or fewer blocks from home.
    for i in range(number_of_randomwalks): #montecarlo loop of 100.000 samples.
        (x,y) = random_walk_2(walk_length) #get a random walk of length = walk_length.
        distance = abs(x) + abs(y) #distance from home.
        if distance <= 4:
            no_transport += 1
    no_transport_percentage = float(no_transport) / number_of_randomwalks
    print("Walk size = ", walk_length, " / % of no transport = ", 100*no_transport_percentage)