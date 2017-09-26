# Programa en Python  de Sebastian Raschka sobre el perceptron

import numpy as np

class Perceptron(object):

    def __init__(self, eta=0.01, epochs=50):
        self.eta = eta
        self.epochs = epochs

    def entrenamiento(self, X, y):

        self.w_ = np.zeros(1 + X.shape[1])
        self.errores_ = []

        for _ in range(self.epochs):
            errores = 0
            for xi, objetivo in zip(X, y):
                actualiza = self.eta * (objetivo - self.predict(xi))
                self.w_[1:] +=  actualiza * xi
                self.w_[0] +=  actualiza
                errores += int(actualiza != 0.0)
            self.errores_.append(errores)
        return self

    def entrada(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        return np.where(self.entrada(X) >= 0.0, 1, -1)

