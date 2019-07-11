#!/usr/bin/env python3
import numpy as np
import sys
from matplotlib import pyplot as plt

# init
input_file = sys.argv[1]
output_file = sys.argv[2]

# read data
data = np.load(input_file)
for var_name in data.files:
    exec(var_name + " = data['" + var_name + "']")

hist = np.cumsum(hist[::-1])[::-1]
hist = hist / hist[0]

# plot cumulative degree distribution
fig, ax = plt.subplots()
plt.autoscale(enable=True, tight=True)

plt.loglog(bins, hist, label='Synthetic')
plt.loglog(k_values, P, 'g', label='Theoretical')
plt.xlabel(r'Degree $k$')
plt.ylabel(r'$P(K \geq k)$')

ax.legend(loc=3, numpoints=2)

plt.savefig(output_file, format='eps', bbox_inches='tight')

