import numpy as np

T = 3
dt = 1/252
p = 0.1

mu = 0
sd = 7

data = np.zeros(size=int(T/dt))

rng = np.random.RandomState(13)


