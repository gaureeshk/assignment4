import numpy as np
favourable_cases=0 #this is the number of cases where X>=Y
x=np.random.poisson(10,100000)#x is an array of random variables having poisson's distribution
y=np.random.exponential(3,100000)#y is an array of random variables having exponential distribution
for a in range(0,100000):
  if (x[a]>=y[a]):
    favourable_cases+=1
sim_prob=favourable_cases/100000
theo_prob=0.941#this is the theoretical value of probability
print(sim_prob,":",theo_prob)