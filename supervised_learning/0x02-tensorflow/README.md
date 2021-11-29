# 0x02. Tensorflow


## 1. Layers
* tf.layers.Dense
Densely-connected layer class.
This layer implements the operation: outputs = activation(inputs * kernel + bias) Where activation is the activation function passed as the activation argument (if not None), kernel is a weights matrix created by the layer, and bias is a bias vector created by the layer (only if use_bias is True).

## 2. Forward Propagation
forward_prop  n time tf.layers.Dense
to get the output prediction Y

## 3. Accuracy
* Calculate the correct predictions
* Calculate accuracy on the test set


## 4. Loss
tf.losses.softmax_cross_entropy(
    onehot_labels,
    logits,
    weights=1.0,
    label_smoothing=0,
    scope=None,
    loss_collection=tf.GraphKeys.LOSSES,
    reduction=Reduction.SUM_BY_NONZERO_WEIGHTS
)

Note that onehot_labels and logits must have the same shape, e.g. [batch_size, num_classes]
* onehot_labels: One-hot-encoded labels.
* logits: Logits outputs of the network.

## Author
* **Mouhamed Charfi** - [medcharfi96](https://github.com/medcharfi96)