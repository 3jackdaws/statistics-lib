from probability import nCr
from math import pow, sqrt, e, factorial

class Binomial:
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

    @property
    def mean(self):
        p = self.success_probability
        n = self.trials
        return n * p

    @property
    def variance(self):
        p = self.success_probability
        n = self.trials
        return n * p * ( 1 - p)

class HyperGeometric:
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

    @property
    def mean(self):
        N = self.population_size
        K = self.success_states
        n = self.selections
        return n * (K // N)

    @property
    def variance(self):
        N = self.population_size
        K = self.success_states
        n = self.selections
        return n * K * (N - K) * (N - n) / (N * N * (N - 1))


class Geometric:
    def __init__(self, probability):
        self.probability = probability

    def pmf(self, *trials):
        p = self.probability
        total = 0
        for k in trials:
            total += pow(1 - p, k-1) * p
        return total

    @property
    def mean(self):
        p = self.probability
        return (1 / p)

    @property
    def variance(self):
        p = self.probability
        return (1 - p) / pow(p, 2)


class NegativeBinomial:
    def __init__(self, failures, probabilty):
        self.failures = failures
        self.probability = probabilty

    def pmf(self, *successes):
        p = self.probability
        r = self.failures
        total = 0
        for k in successes:
            total += nCr(k + r - 1, k) * pow(1 - p, r) * pow(p, k)
        return total

    @property
    def mean(self):
        p = self.probability
        r = self.failures
        return (p * r) / (1 - p)

    @property
    def variance(self):
        p = self.probability
        r = self.failures
        return (p * r) / pow(1 - p, 2)


class Poisson:
    # models the number of times and event occurs in an interval of time or space
    def __init__(self, average_events):
        self.lmb = average_events

    def pmf(self, *occurences):
        lmb = self.lmb
        total = 0
        for k in occurences:
            total += (pow(lmb, k) * pow(e, -k))/factorial(k)
        return total

    @property
    def mean(self):
        return self.lmb

    @property
    def variance(self):
        return self.lmb