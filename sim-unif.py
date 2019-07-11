#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
#from scipy.special import zeta

# params
n = 100000

# degrees
k = np.zeros(n)
k[0] = 1

for t in np.arange(1, n):
    p = np.ones(t) / t
    index = np.random.choice(t, 1, p=p)

    k[index] += 1
    k[t] = 1
    print(t)

# synthetic degree distribution
bins = np.unique(k)
hist, _ = np.histogram(k, np.append(bins, max(bins)+1))

# theoretical degree distribution
k_values = np.arange(np.max(k)) + 1
P_cum = np.exp(1 - k_values)

P = -np.diff(np.append(P_cum, 0))
freq = P * n
freq[freq < 1] = 0  # cut off

# plot degree distribution
fig, ax = plt.subplots()

plt.autoscale(enable=True, tight=True)
plt.semilogy(bins, hist, '.', label='synthetic')
plt.semilogy(k_values, freq, 'g', label='theoretical')
plt.xlabel(r'Degree $k$')
plt.ylabel('Frequency')

ax.legend(loc=1, numpoints=2)

plt.savefig('degr-dist-unif.eps', format='eps')
plt.savefig('degr-dist-unif.png', format='png')

# cumulative degree distribution
hist = np.cumsum(hist[::-1])[::-1]
hist = hist / hist[0]

# theoretical discrete cumulative degree distribution
p = 1 / np.power(k_values, 3)
P_discr = np.cumsum(p[::-1])[::-1]
P_discr = P_discr / P_discr[0]

# plot cumulative degree distribution
plt.clf()
fig, ax = plt.subplots()

plt.autoscale(enable=True, tight=True)
plt.semilogy(bins, hist, label='synthetic')
plt.semilogy(k_values, P_cum, 'g', label='theoretical')
#plt.loglog(k_values, P, 'g', drawstyle='steps-post', label='theo. discr.')
plt.xlabel(r'Degree $k$')
plt.ylabel(r'$P(K \geq k)$')

ax.legend(loc=1, numpoints=2)

plt.savefig('cum-degr-dist-unif.eps', format='eps')
plt.savefig('cum-degr-dist-unif.png', format='png')

