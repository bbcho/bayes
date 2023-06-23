import numpy as np
import pandas as pd

def outages_monthly(T=3, dt=1/12, p=0.25, nl=10, pl=0.3):
    N = int(T/dt)

    data = np.zeros(N)
    rng = np.random.RandomState(13)

    for i in range(N):
        data[i] = rng.binomial(n=1, p=p)

        if data[i] > 0:
            data[i] = rng.binomial(n=nl, p=pl)

    data = pd.DataFrame(data, columns=['outage'])
    data.index = pd.date_range(start=pd.Timestamp.now().floor('D')-pd.DateOffset(months=len(data)+1), periods=len(data), freq='MS')
    return data

def outages_daily(T=3, dt=1/252, p=0.01, mu=0, sd=7):

    # T = 3
    # dt = 1/252
    # p = 0.01
    #
    # mu = 0
    # sd = 7
    N = int(T/dt)

    data = np.zeros(int(T/dt))

    rng = np.random.RandomState(13)

    i = 0
    out_len = 0

    while i < N:

        if out_len > 0:
            out_len -= 1
            data[i] = 1
        else:
            data[i] = rng.binomial(n=1, p=p)
            if data[i] > 0:
                out_len = abs(rng.normal(mu, sd))
        
        i += 1

    return data
            
