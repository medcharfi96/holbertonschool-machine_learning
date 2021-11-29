# binary classification
This is ‘Classification’ tutorial which is a part of the Machine Learning course offered by Simplilearn. We will learn Classification algorithms, types of classification algorithms, support vector machines(SVM), Naive Bayes, Decision Tree and Random Forest Classifier in this tutorial.

## 0. Neuron 
Write a class Neuron that defines a single neuron performing binary classification

## 1. Privatize Neuron
with Private instance attributes

## 2. Neuron Forward Propagation
with sigmoid activation function
 
![alt text](https://www.gstatic.com/education/formulas2/-1/en/sigmoid_function.svg)

## 3. Neuron loss and  Cost
using logistic regression:
* Y is a numpy.ndarray with shape (1, m) that contains the correct labels for the input data
* A is a numpy.ndarray with shape (1, m) containing the activated output of the neuron for each
```sh
loss = -(Y * log(A) + (1 - Y) * log(1 - A))
cost = 1/m (sum(loss))
```
## 4. Evaluate Neuron 
values should be 1 if the output of the network is >= 0.5 and 0 otherwise
## 5. Neuron Gradient Descent
Updates the private attributes __W and __b
```sh
self.__W -= (dw * alpha)
self.__b -= (db * alpha)
```
## 6. Train Neuron

Returns the evaluation of the training data after
iterations of training have occurred
used:
* forward_prop
* gradient_descent
* evaluate

## 7. Upgrade Train Neuron
Update the public method train to def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True, graph=True, step=100)

-------------------------------------------------------------------------------------
## 8. NeuralNetwork 
* class NeuralNetwork that defines a neural network with one hidden layer performing binary classification
## 9. Privatize NeuralNetwork
## 10. NeuralNetwork Forward Propagation
neural network with one hidden layer performing
with sigmoid activation function
* Updates the private attributes __A1 and __A2
## 11. NeuralNetwork Cost
using logistic regression:
* Y is a numpy.ndarray with shape (1, m) that contains the correct labels for the input data
* A is a numpy.ndarray with shape (1, m) containing the activated output of the neuron for each
```sh
loss = -(Y * log(A) + (1 - Y) * log(1 - A))
cost = 1/m (sum(loss))
```
## 12. Evaluate NeuralNetwork
values should be 1 if the output of the network is >= 0.5 and 0 otherwise
the output neuron (prediction)(A2)
## 13. NeuralNetwork Gradient Descent
Updates the private attributes __W1, __b1, __W2, and __b2
not the same for one neuron.
## 14. Train NeuralNetwork 
Returns the evaluation of the training data after
iterations of training have occurred
used:
* forward_prop
* gradient_descent
* evaluate
## 15. Upgrade Train NeuralNetwork
Update the public method train to def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True, graph=True, step=100)

------------------------------------------------------------------------------------
## 16. DeepNeuralNetwork
DeepNeuralNetwork that defines a deep neural network performing binary classification
* layers is a list representing the number of nodes in each layer of the network
 `* The first value in layers represents the number of nodes in the first layer,
* L: The number of layers in the neural network.
* cache: A dictionary to hold all intermediary values of the network. Upon instantiation, it should be set to an empty dictionary.
* weights: A dictionary to hold all weights and biased of the network. 
__New Initialization techniques__
__He initialization__: we just simply multiply random initialization with
![alt text](https://miro.medium.com/max/700/1*zxD6Nr6TyAb8JEG6oXAjkg.png)
## 17. Privatize DeepNeuralNetwork
## 18. DeepNeuralNetwork Forward Propagation
z = np.matmul(wi, Ai-1) + b
Sigmoid_a = 1 / (1 + np.exp(-z))
self.__cache["A"+str(i+1)] = Sigmoid_a
## 19. DeepNeuralNetwork Cost
## 20. Evaluate DeepNeuralNetwork 
## 21. DeepNeuralNetwork Gradient Descent
using backpropagation

![alt text](https://miro.medium.com/max/500/0*ETudkFMzVEMsUrVD.png)

and g(x) = 1 / (1 + np.exp(-z))

dg(x) = g(x)(1- g(x))
## 22. Train DeepNeuralNetwork
Returns the evaluation of the training data after
iterations of training have occurred
used:
* forward_prop
* gradient_descent
* evaluate
## 23. Upgrade Train DeepNeuralNetwork
Update the public method train to 
def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True, graph=True, step=100)
## 24. One-Hot Encode 
def one_hot_encode(Y, classes): 
that converts a numeric label vector into a one-hot matrix
* Y is a numpy.ndarray with shape (m,) containing numeric class labels
* m is the number of examples
* classes is the maximum number of classes found in Y
Returns: a one-hot encoding of Y with shape (classes, m), or None on failure
## 25. One-Hot Decode
converts a one-hot matrix into a vector of labels:
## 26. Persistence is Key
* Create the instance method def save(self, filename):

* Saves the instance object to a file in pickle format
* filename is the file to which the object should be saved

* Create the static method def load(filename):

* Loads a pickled DeepNeuralNetwork object
* filename is the file from which the object should be loaded

## 27. Update DeepNeuralNetwork 
Update the class DeepNeuralNetwork to perform multiclass classification
update the instance methods forward_prop, cost, and evaluate

![alt text](https://miro.medium.com/max/250/1*D4p2CsxVe50MoJIjN0YFNw.png)

![alt text](https://miro.medium.com/max/700/1*ReYpdIZ3ZSAPb2W8cJpkBg.jpeg)

## 28. All the Activations 
Update the class DeepNeuralNetwork to allow different activation functions
activation represents the type of activation function used in the hidden layers
* sig represents a sigmoid activation
* tanh represents a tanh activation

![alt text](https://cdn-images-1.medium.com/max/970/1*KEMiN1powp_MwhVc9MFTSw.png)

```sh
def tanh_prime(z):
	return 1 - np.power(tanh(z), 2)

```

## Author
* **Mouhamed Charfi** - [medcharfi96](https://github.com/medcharfi96)