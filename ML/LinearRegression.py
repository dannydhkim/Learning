import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Linear regression formular is as follows:
y = B1 * X + B0
where B1 is the weight vector and B0 is the bias vector
"""

class AnalyticalLinearRegression():
    def __init__(self):
        self.b0 = 0
        self.b1 = 0

    def mean(self, X):
        return np.sum(X) / float(len(X))         

    def variance(self, X):
        return np.sum((X - np.mean(X))**2)

    def covariance(self, X, y):
        return np.sum((X - self.mean(X)) * (y - self.mean(y)))

    def fit(self, X, y):
        self.b1 = self.covariance(X, y) / self.variance(X)
        self.b0 = self.mean(y) - self.b1 * self.mean(X)

    def predict(self, x):
        return (self.b1 * x) + self.b0


class GradientDescentLinearRegression():
    def __init__(self):
        self.b0 = 0
        self.b1 = 0

    #Use MSE as cost function -- to simplify gradient descent
    def cost_function(true, predicted):
        return np.sum((true - predicted)**2) / len(predicted)

    #gradient descent
    def fit(self, X, y, learning_rate = 0.01, iterations = 100):
        size = len(X)
        cost_log = []

        for _ in range(iterations):

            error = y - (self.b1 * X + self.b0)

            #Derivative of cost function respect to b1 * learning rate:
            self.b1 -= learning_rate * (-2.0 * X.T.dot(error).sum()/ size)
            #Derivative of cost function respect to b0 * learning rate:
            self.b0 -= learning_rate * (-2.0 * error.sum() / size)

            cost_log.append(self.b1)

        return cost_log

    def predict(self, X):
        return (self.b1 * X) + self.b0

def main():
    X = 5 * np.random.rand(100,1)
    y = 2* X + np.random.randn(100,1)

    plt.scatter(X,y)
    plt.show()

    anly_model = AnalyticalLinearRegression()
    anly_model.fit(X,y)
    print('y = {} * X + {}'.format(anly_model.b1, anly_model.b0))

    plt.scatter(X, y, s=200, c='#087E8B', alpha=0.65, label='Source data')
    plt.plot(X, anly_model.predict(X), color='#000000', lw=3, label=f'Best fit line > B0 = {anly_model.b0:.2f}, B1 = {anly_model.b1:.2f}')
    plt.title('Best fit line', size=20)
    plt.xlabel('X', size=14)
    plt.ylabel('Y', size=14)
    plt.legend()
    plt.show()

    gd_model = GradientDescentLinearRegression()
    history = gd_model.fit(X,y)
    print('y = {} * X + {}'.format(gd_model.b1, gd_model.b0))

    plt.scatter(X, y, s=200, c='#087E8B', alpha=0.65, label='Source data')
    plt.plot(X, gd_model.predict(X), color='#000000', lw=3, label=f'Best fit line > B0 = {gd_model.b0:.2f}, B1 = {gd_model.b1:.2f}')
    plt.title('Best fit line', size=20)
    plt.xlabel('X', size=14)
    plt.ylabel('Y', size=14)
    plt.legend()
    plt.show()

if __name__ == "__main__" : 
    main()

