import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats
from scipy.special import factorial

%matplotlib notebook

N=10000
num_bins=50

# normal distributions
samples=np.random.normal(size=N) #generate 10000 different values
plt.hist(samples, num_bins) #If bins is an integer, it defines the number of equal-width bins in the range.

y=np.linspace(-4, 4, 1000)
bin_width=(np.max(samples) - np.min(samples)) / num_bins
dist=stats.norm.pdf(y)*N*bin_width

plt.plot(y, dist)

# Poisson distributon
lam=3
samples=np.random.poisson(size=N, lam=lam)
plt.hist(samples, num_bins)

x=np.arange(0, 10, 0.1)
t=(np.exp(-lam)*np.power(lam, x))/factorial(x)
t=t*N

plt.plot(x, t)

# chi-squared distribution
deg_freedom=4
samples=np.random.chisquare(size=N, df=deg_freedom)
plt.hist(samples, num_bins)

y=np.linspace(0, 25, 1000)
bin_width=(np.max(samples)-np.min(samples))/num_bins
dist=stats.chi2.pdf(y, df=deg_freedom) * N * bin_width

plt.plot(y, dist)