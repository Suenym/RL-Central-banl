import numpy as np

class DemandShock:
    def __init__(self, sigma: float):
        self.sigma = sigma

    def sample(self):
        return np.random.normal(loc=0.0, scale=self.sigma)
