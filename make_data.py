import numpy as np
import pandas as pd
from scipy.sparse import random
import scipy.stats as st

seed = 12345

# Make Outage Data for PYMC example

rng = np.random.default_rng(seed)

T = 5
dt = 1/12
N = int(T/dt)

is_unit_down = rng.binomial(1, 0.3, size=N)
num_outage = is_unit_down.sum()
length_of_outage = st.halfnorm.rvs(loc=1, scale=10, size=num_outage, random_state=seed).round(0)
length_of_outage = np.clip(length_of_outage, 1, 28)

print(list(length_of_outage))
print(list(is_unit_down))

