# 0x04. Autoencoders
 
Autoencoder is an unsupervised artificial neural network that learns how to efficiently compress and encode data then learns how to reconstruct the data back from the reduced encoded representation to a representation that is as close to the original input as possible.
Autoencoder, by design, reduces data dimensions by learning how to ignore the noise in the data.
- data denoising and dimensionality reduction for data
##  Autoencoder Components
**1- Encoder:** In which the model learns how to reduce the input dimensions and compress the input data into an encoded representation.
**2- Bottleneck:** which is the layer that contains the compressed representation of the input data. This is the lowest possible dimensions of the input data.
**3- Decoder:** In which the model learns how to reconstruct the data from the encoded representation to be as close to the original input as possible.
**4- Reconstruction Loss:** This is the method that measures measure how well the decoder is performing and how close the output is to the original input.

The training then involves using back propagation in order to minimize the network’s reconstruction loss.
![alt text](https://miro.medium.com/max/700/1*2ijh2-e0PcYgYKbWYkbdsw.png)

## 0. "Vanilla" Autoencoder
![alt text](https://miro.medium.com/max/700/1*V_YtxTFUqDrmmu2JqMZ-rA.png)

## 1. Sparse Autoencoder

A sparse autoencoder is simply an autoencoder whose training criterion involves a sparsity penalty. In most cases, we would construct our loss function by penalizing activations of hidden layers so that only a few nodes are encouraged to activate when a single sample is fed into the network.
The intuition behind this method is that, for example, if a man claims to be an expert in mathematics, computer science, psychology, and classical music, he might be just learning some quite shallow knowledge in these subjects. However, if he only claims to be devoted to mathematics, we would like to anticipate some useful insights from him. And it’s the same for autoencoders we’re training — fewer nodes activating while still keeping its performance would guarantee that the autoencoder is actually learning latent representations instead of redundant information in our input data.
![alt text](https://miro.medium.com/max/700/1*k9RX5_kDYt2kG0u9ZREu5w.png)

##  2. Convolutional Autoencoder
Convolutional Autoencoder is a variant of Convolutional Neural Networks that are used as the tools for unsupervised learning of convolution filters. They are generally applied in the task of image reconstruction to minimize reconstruction errors by learning the optimal filters. Once they are trained in this task, they can be applied to any input in order to extract features. Convolutional Autoencoders are general-purpose feature extractors differently from general autoencoders that completely ignore the 2D image structure. In autoencoders, the image must be unrolled into a single vector and the network must be built following the constraint on the number of inputs.

![alt text](https://analyticsindiamag.com/wp-content/uploads/2020/07/The-structure-of-proposed-Convolutional-AutoEncoders-CAE-for-MNIST-In-the-middle-there.png)


## 3. Variational Autoencoder
![alt text](https://www.jeremyjordan.me/content/images/2018/03/Screen-Shot-2018-03-16-at-10.24.11-PM.png)
Variational Autoencoders (VAEs) have one fundamentally unique property that separates them from vanilla autoencoders, and it is this property that makes them so useful for generative modeling: their latent spaces are, by design, continuous, allowing easy random sampling and interpolation.
![alt text](https://magenta.tensorflow.org/assets/music_vae/sketch-attr.png)
## What i learned from  this chapter

## Author
* **Mouhamed Charfi** - [medcharfi96](https://github.com/medcharfi96)