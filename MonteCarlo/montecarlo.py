import numpy as np
import matplotlib.pyplot as plt

#MonteCalor Simulation
#Step 1: Set up the Predictive Model: Identify the dependent and independent variables.
#Step 2: Specify the probability distribution of the independent variables: By using historical data or subjective judgement to define a range of likely values and assign probability weights for each.
#Step 3: Run: Simulations repeatedly generating random values of the independent variables until you can make up a representative sample of the infinite number of possible combinations.

#The more you sample, the more accurate your sampling range, and then the better your estimation.

#Problem 1
#You have two create two reports (A and B) and they could take anywhere from 1 to 5 hrs and 2 to 6 hrs to complete, respectively.
#You have 9 hours to complete these reports if you want to go to your friend's barbecue.
#We assume a uniform probability distribution for these two reports because we can assume that the relative likelihood of all outcomes between a defined min (1hr and 2hrs) and a defined max (5hrs and 6 hrs) are the same.

sims = 1000000 #number of simulations/samples

A = np.random.uniform(1, 5, sims)
B = np.random.uniform(2, 6, sims)

duration = A + B #total time to complete the two reports

plt.figure(figsize=(3, 1.5))
plt.hist(duration, density=True)
plt.axvline(9, color ='r') #vertical red line at the value 9 as the party is in just 9 hours (threshold)
plt.show()
print((duration > 9).sum()/sims) #% of simulations that exceeded a total of 9 hours.