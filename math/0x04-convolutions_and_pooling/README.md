# convolutions_and_pooling

## 1. What is CNN ?
 In deep learning, a convolutional neural network (CNN, or ConvNet) is a class of deep neural networks, most commonly applied to analyzing visual imagery
## 2. Why should we use CNN ?
 Suppose you are working with MNIST dataset, you know each image in MNIST is 28 x 28 x 1(black & white image contains only 1 channel). Total number of neurons in input layer will 28 x 28 = 784, this can be manageable. What if the size of image is 1000 x 1000 which means you need 10⁶ neurons in input layer. Oh! This seems a huge number of neurons are required for operation. It is computationally ineffective right. So here comes Convolutional Neural Network or CNN.
 >In simple word what CNN does is, it extract the feature of image and convert it into lower dimension without loosing its characteristics

![alt text](https://vernlium.github.io/2018/10/15/coursera-deeplearning-ai-c4-week1/mulit_channel_convolution.gif)
  
## Why to use Pooling Layers? 
Pooling layers are used to reduce the dimensions of the feature maps. Thus, it reduces the number of parameters to learn and the amount of computation performed in the network.
Pooling layer is used to reduce the spatial volume of input image after convolution. It is used between two convolution layer.

![alt text](https://vernlium.github.io/2018/10/15/coursera-deeplearning-ai-c4-week1/maxpool_animation.gif)

## What i learned in this chapter

- What is a convolution?
- What is max pooling? average pooling?
- What is a kernel/filter?
- What is padding?
- What is “same” padding? “valid” padding?
- What is a stride?
- What are channels?
- How to perform a convolution over an image
- How to perform max/average pooling over an image


### Done by : Mouhamed Charfi