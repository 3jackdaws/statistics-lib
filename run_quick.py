import probability
from distributions import *




if __name__ == '__main__':
    dist = NegativeBinomial(5, 0.1)
    print(dist.pmf())