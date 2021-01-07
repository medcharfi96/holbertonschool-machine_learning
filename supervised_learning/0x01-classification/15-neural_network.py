#!/usr/bin/env python3
"""
classe description
"""
import numpy as np
import matplotlib.pyplot as plt


class NeuralNetwork():
    """
    classe neurone network
    """
    def __init__(self, nx, nodes):
        """
        constructeur parametré
        :param nx: int
        :param nodes: int
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(nodes) is not int:
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")
        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.normal(size=(1, nodes))
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W2(self):
        """
        get w2
        :return:
        """
        return self.__W2

    @property
    def b2(self):
        """
        get b2
        :return:
        """
        return self.__b2

    @property
    def A2(self):
        """
        get A2
        :return:
        """
        return self.__A2

    @property
    def W1(self):
        """
        get w1
        :return:
        """
        return self.__W1

    @property
    def b1(self):
        """
        get b1
        :return:
        """
        return self.__b1

    @property
    def A1(self):
        """
        get A1
        :return:
        """
        return self.__A1

    def forward_prop(self, X):
        """
        fonction de propagation
        :param X: ndarray
        :return:
        """
        v1 = np.matmul(self.__W1, X, None) + self.__b1
        res = 1 / (1 + np.exp(-v1))
        self.__A1 = res
        v2 = np.matmul(self.__W2, res, None) + self.__b2
        res2 = 1 / (1 + np.exp(-v2))
        self.__A2 = res2
        return (self.__A1, self.__A2)

    def cost(self, Y, A):
        """
        calcule le cout du lensemble de modele de regression
        :param Y: ndarray
        :param A: ndarray  represent y chapeau
        :return:
        """
        m = Y.shape[1]
        za = 1.0000001 - A
        cost = (np.sum(Y * np.log(A) + (1 - Y) * np.log(za)))/m
        return (-1 * cost)

    def evaluate(self, X, Y):
        """
        eval de prediction
        :param X: ndarray
        :param Y: ndarray
        :return:
        """

        A1, A2 = self.forward_prop(X)
        ras = np.round(A2)
        lal = self.cost(Y, A2)
        return (ras.astype(np.int), lal)

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """
        calcule de gradient
        :param X: ndarray
        :param Y: ndarray
        :param A: ndarray
        :param alpha: taux dapprentissage
        :return:
        """
        m = Y.shape[1]
        """
        for the first arg A1
        """
        deriv = A1 * (1 - A1)
        var1 = np.matmul(self.__W2.T, A2 - Y)
        db1 = np.sum(var1 * deriv, axis=1, keepdims=True) / m
        dW1 = np.matmul(X, (var1 * deriv).T, None)/m
        """
        for A2  mean for the second one argument
        """
        db2 = np.sum(A2-Y, axis=1, keepdims=True) / m
        dW2 = np.matmul(A1, (A2 - Y).T, None)/m
        """
        reinisialisation des variable
        """
        self.__W1 = self.__W1 - (alpha * dW1).T
        self.__b1 = self.__b1 - alpha * db1
        self.__W2 = self.__W2 - (alpha * dW2).T
        self.__b2 = self.__b2 - alpha * db2

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """
        des
        """
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations < 0:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha < 0:
            raise ValueError("alpha must be positive")
        for i in range(iterations):
            self.__A1, self.__A2 = self.forward_prop(X)
            self.gradient_descent(X, Y, self.__A1, self.__A2, alpha)
        return self.evaluate(X, Y)

    def train(self, X, Y, iterations=5000, alpha=0.05,
              verbose=True, graph=True, step=100):
        """
        :param X:
        :param Y:
        :param iterations:
        :param alpha:
        :return:
        """
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations < 0:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha < 0:
            raise ValueError("alpha must be positive")
        if graph is True or verbose is True:
            if type(step) is not int:
                raise TypeError("step must be an integer")
            if step > iterations or step < 0:
                raise ValueError("step must be positive and <= iterations")
        m = Y.shape[1]
        cl = []
        sl = []
        for count in range(0, iterations):
            self.__A1, self.__A2 = self.forward_prop(X)
            self.gradient_descent(X, Y, self.__A1, self.__A2, alpha)
            if count == iterations or count % step == 0:
                ad = self.cost(Y, self.__A2)
                sl.append(count)
                cl.append(ad)
                if verbose:
                    print("Cost after {} iterations: {}".
                          format(count, ad))
        if graph is True:
            plt.plot(sl, cl)
            plt.xlim(0, 5000)
            plt.ylabel('cost')
            plt.xlabel('iteration')
            plt.title('Training Cost')
            plt.show()
        z = self.forward_prop(X)
        ras = np.round(z)
        lal = self.cost(Y, z)
        return(ras.astype(np.int), lal)
