from probability import nCr
from math import pow

class DiscreteBinomial:
    def __init__(self, success_probability, trials):
        self.success_probability = success_probability
        self.trials = trials

    def pmf(self, *num_successes):
        p = self.success_probability
        n = self.trials
        total = 0
        for k in num_successes:
            total += nCr(n, k) * pow(p, k)  * pow(1 - p, n - k)
        return total

    def mean(self):
        p = self.success_probability
        n = self.trials
        return n * p

    def variance(self):
        p = self.success_probability
        n = self.trials
        return n * p * ( 1 - p)

class DiscreteHyperGeometric:
    def __init__(self, population_size, success_states, selections):
        self.population_size = population_size
        self.success_states = success_states
        self.selections = selections

    def pmf(self, *observed_successes):
        N = self.population_size
        K = self.success_states
        n = self.selections

        total = 0
        for k in observed_successes:
            total += nCr(K,k) * nCr(N - K, n - k) / nCr(N, n)
        return total

    def mean(self):
        N = self.population_size
        K = self.success_states
        n = self.selections
        return n * (K // N)

    def variance(self):
        N = self.population_size
        K = self.success_states
        n = self.selections
        return n * K * (N - K) * (N - n) / (N * N * (N - 1))


