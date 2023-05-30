import numpy as np

a = 2.3
b = 4.1
mu = 0
sd = 12.2
size = 200

rng = np.random.RandomState(13)

x = rng.uniform(0,10, size=size)

y = a + b*x + rng.normal(mu, sd, size=size) 
