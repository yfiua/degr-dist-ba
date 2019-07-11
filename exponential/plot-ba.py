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

N = s[-1]
P = -np.diff(np.append(P, 0))      # differentiate
P = P / np.sum(P) * N       # normalization
P[ P < 1 ] = 0      # cut off

# plot degree distribution
fig, ax = plt.subplots()
plt.autoscale(enable=True, tight=True)

plt.loglog(bins, hist, '.', label='Synthetic')
plt.loglog(k_values, P, 'g', label='Theoretical')
plt.xlabel(r'Degree $k$')
plt.ylabel('Frequency')

ax.legend(loc=3, numpoints=2)

# plot growth
left, bottom, width, height = [0.54, 0.465, 0.35, 0.4]
ax_inset = fig.add_axes([left, bottom, width, height])

ax_inset.semilogy(timeline, s, 'ro', label='Network Size')
ax_inset.semilogy(timeline_asymp, growth_asymp, 'g', label='Theo. Asymp.')
ax_inset.semilogy(timeline, k_max, 'b.', label='Max Degree')
ax_inset.set_xlabel(r'Physical Time $t$')
ax_inset.set_xlim(xmin=0)
ax_inset.set_ylim(ymin=1)

ax_inset.legend(loc=2, numpoints=2, prop={'size': 8})

plt.savefig(output_file, format='eps', bbox_inches='tight')

