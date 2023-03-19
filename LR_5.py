import numpy as np

class Matrix:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.matrix = np.random.randint(1,100, size=(n, m))

    def transpose(self):
        return self.matrix.transpose()

    def column_means(self):
        return np.mean(self.data, axis=0)
