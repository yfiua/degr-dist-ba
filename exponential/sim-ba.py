#!/usr/bin/env python3
import numpy as np
import argparse

# cli args
parser = argparse.ArgumentParser(description='Simulate the BA model.')
parser.add_argument('output_file',
                    help='output file')
parser.add_argument('--step', default=0.01,
                    help='discrete time interval (default: 0.01)')

args = parser.parse_args()

# main
output_file = args.output_file
step = args.step

# params
t_max = 8

# corrected value of e and e^2 considering discreteness
e_corr = np.power(1 + step, 1 / step)
e_2_corr = np.power(1 + 2 * step, 1 / step)

# number of initial nodes
N_0 = 10
N = N_0

# degrees
k = np.ones(N)

timeline = np.arange(t_max, step=step) + step
s = np.array([])
k_max = np.array([])

for t in timeline:
    # record max degree
    k_max = np.append(k_max, np.max(k))

    delta_k = np.floor(step * k + np.random.rand(N))
    k = k + delta_k

    delta_N = np.int(np.sum(delta_k))
    k = np.append(k, np.ones(delta_N))

    N += delta_N
    s = np.append(s, N)

    print(t, N)

# theoretical asymptote
timeline_asymp = np.arange(t_max * 0.65, t_max * 0.98, step=step)
growth_asymp = np.power(e_2_corr, timeline_asymp)
growth_asymp = growth_asymp / growth_asymp[0] * s[np.int(len(s) * 0.65)] * 2     # slightly above the actual curve

# degree distribution
bins = np.unique(k)
hist, _ = np.histogram(k, np.append(bins, max(bins)+1))

# theoretical degree distribution
k_values = np.arange(np.max(bins)) + 1
P = np.power(e_2_corr, -np.log(k_values) / np.log(e_corr))
print(P)

# save data
np.savez(output_file, timeline=timeline, s=s, timeline_asymp=timeline_asymp, growth_asymp=growth_asymp, k_max=k_max, bins=bins, hist=hist, k_values=k_values, P=P)

