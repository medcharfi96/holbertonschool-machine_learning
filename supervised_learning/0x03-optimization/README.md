# 0x03. Optimization
 
Feature scaling is a method used to normalize the range of independent variables or features of data. In data processing, it is also known as data normalization and is generally performed during the data preprocessing step.

## 1. Normalize
In machine learning, we can handle various types of data. audio signals and pixel values for image data, and this data can include multiple dimensions. Feature standardization makes the values of each feature in the data have zero-mean (when subtracting the mean in the numerator) and unit-variance. This method is widely used for normalization in many machine learning algorithms

![alt text](https://wikimedia.org/api/rest_v1/media/math/render/svg/b0aa2e7d203db1526c577192f2d9102b718eafd5)

Where x is the original feature vector, x bar  is the mean of that feature vector, and sigma  is its standard deviation.

## 3. Mini-Batch
Batch gradient descent is a variation of the gradient descent algorithm that calculates the error for each example in the training dataset, but only updates the model after all training examples have been evaluated
What is Mini-Batch Gradient Descent?
Mini-batch gradient descent is a variation of the gradient descent algorithm that splits the training dataset into small batches that are used to calculate model error and update model coefficients.

Implementations may choose to sum the gradient over the mini-batch which further reduces the variance of the gradient.
## 5. Momentum optimization algorithm
that updates a variable using the gradient descent with momentum optimization algorithm:

* alpha is the learning rate
* beta1 is the momentum weight
* var is a numpy.ndarray containing the variable to be updated
* grad is a numpy.ndarray containing the gradient of var
* v is the previous first moment of var
* Returns: the updated variable and the new moment, respectively

```sh
    v = (beta1*dw_prev) + ((1- beta1)*dw)
    w = w - (alpha *v)
```
## 7. RMSProp optimization algorithm
* alpha is the learning rate
* beta2 is the RMSProp weight
* epsilon is a small number to avoid division by zero
* var is a numpy.ndarray containing the variable to be updated
* grad is a numpy.ndarray containing the gradient of var
* s is the previous second moment of var
* Returns: the updated variable and the new moment, respectively
```sh
    vdw = (beta2 * s) + ((1 - beta2)*grad**2)
    new = var - alpha * (grad / (np.sqrt(vdw)+epsilon))
```
## 9.Adam optimization algorithm
>Adam use  Momentum optimization algorithm and  RMSProp optimization algorithm

* alpha is the learning rate
* beta1 is the weight used for the first moment
* beta2 is the weight used for the second moment
* epsilon is a small number to avoid division by zero
* var is a numpy.ndarray containing the variable to be updated
* grad is a numpy.ndarray containing the gradient of var
* v is the previous first moment of var
* s is the previous second moment of var
* t is the time step used for bias correction
* Returns: the updated variable, the new first moment, and the new second moment, respectively
## 11. Learning Rate Decay  
The learning rate is a hyperparameter that controls how much to change the model in response to the estimated error each time the model weights are updated. Choosing the learning rate is challenging as a value too small may result in a long training process that could get stuck, whereas a value too large may result in learning a sub-optimal set of weights too fast or an unstable training process.

Write the function def learning_rate_decay(alpha, decay_rate, global_step, decay_step): that updates the learning rate using inverse time decay in numpy:

* alpha is the original learning rate
* decay_rate is the weight used to determine the rate at which alpha will decay
* global_step is the number of passes of gradient descent that have elapsed
* decay_step is the number of passes of gradient descent that should occur before  alpha is decayed further
* the learning rate decay should occur in a stepwise fashion
* Returns: the updated value for alpha

## 13. Batch Normalization
>Batch normalization is a technique for training very deep neural networks that 
>standardizes the inputs to a layer for each mini-batch. This has the effect of 
>stabilizing the learning process and dramatically reducing the number of training 
>epochs required to train deep networks.

Write the function def batch_norm(Z, gamma, beta, epsilon): that normalizes an unactivated output of a neural network using batch normalization:

* Z is a numpy.ndarray of shape (m, n) that should be normalized
* m is the number of data points
* n is the number of features in Z
* gamma is a numpy.ndarray of shape (1, n) containing the scales used for batch normalization
* beta is a numpy.ndarray of shape (1, n) containing the offsets used for batch normalization
* epsilon is a small number used to avoid division by zero
* Returns: the normalized Z matrix

## 14. Batch Normalization Upgraded

the function def create_batch_norm_layer(prev, n, activation): that creates a batch normalization layer for a neural network in tensorflow:

* prev is the activated output of the previous layer
* n is the number of nodes in the layer to be created
* activation is the activation function that should be used on the output of the layer
* you should use the tf.layers.Dense layer as the base layer with kernal initializer tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
* your layer should incorporate two trainable parameters, gamma and beta, initialized as vectors of 1 and 0 respectively
* you should use an epsilon of 1e-8
* Returns: a tensor of the activated output for the layer
## Author
* **Mouhamed Charfi** - [medcharfi96](https://github.com/medcharfi96)