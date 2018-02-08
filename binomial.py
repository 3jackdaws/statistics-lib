import probability
from distributions import DiscreteBinomial, DiscreteHyperGeometric




if __name__ == '__main__':
    dist = HyperGeometric(50, 5, 4)
    output = dist.pmf(1)
    output = dist.variance()
    print(output)