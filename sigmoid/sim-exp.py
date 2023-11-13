#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
#from scipy.special import zeta

# params
n_max = 1000000 # rough number of nodes
t_max = 200

# eta distribution
eta_step = 0.005
lambd = 2.5

# decay function
gamma = 1
t_step = 0.005   # only for decay function

# number of initial nodes
N_0 = 6

# rho
eta_values = np.arange(1, step=eta_step) + eta_step / 2  # possible eta values
rho = np.power(1 - eta_values, lambd)
rho = rho / np.sum(rho)

# network size growth as exponential function of time
t = np.arange(1, t_max)

# an exponential function
n = np.exp(0.05 * t)
n = n / n[-1] * n_max

n = np.round(n).astype(int)

# calculate the exact total number of nodes
n_max = n[-1] + N_0
print('n_max =', n_max)

# power law decay function
def f_decay(tau, gamma):
    return np.power(tau + 1., -gamma)

# plot network size growth
fig, ax = plt.subplots()

plt.autoscale(enable=True, tight=True)
plt.semilogy(t, n, 'b')
plt.xlabel('Time $t$')
plt.ylabel('Network size $n$')

plt.savefig('net-size-exp.pdf', format='pdf')

# delta n
dn = np.diff(n)

# plot delta n
plt.clf()
fig, ax = plt.subplots()

plt.autoscale(enable=True, tight=True)
plt.semilogy(t[1:], dn, 'b')
plt.xlabel('Time $t$')
plt.ylabel(r'$\Delta n$')

plt.savefig('delta-n-exp.pdf', format='pdf')

# degrees
k = np.ones(n_max, dtype=int)

# initial nodes
N = N_0

# node birth times
t_0 = np.zeros(n_max, dtype=int)

# fitness
eta = np.random.choice(eta_values, n_max, p=rho)

for t_ in np.arange(1, t_max-2):
    Pi = k[0:N] * eta[0:N] * f_decay((t_ - t_0[0:N]) * t_step, gamma)
    index = np.random.choice(N, dn[t_], p=Pi/np.sum(Pi))

    k[index] += 1

    # set up new nodes
    t_0[N : N+dn[t_]] = t_

    N += dn[t_]
    print(t_)

# synthetic degree distribution
bins = np.unique(k)
hist, _ = np.histogram(k, np.append(bins, max(bins)+1))

# plot degree distribution
fig, ax = plt.subplots()

plt.autoscale(enable=True, tight=True)
plt.loglog(bins, hist, '.', label='synthetic')
plt.xlabel(r'Degree $k$')
plt.ylabel('Frequency')

ax.legend(loc=1, numpoints=2)

plt.savefig('degr-dist-exp.pdf', format='pdf')

