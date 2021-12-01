# 0x07. Convolutional Neural Networks

## CNNs have a couple of concepts called parameter sharing and local connectivity
* Parameter sharing is sharing of weights by all neurons in a particular feature map.
* Local connectivity is the concept of each neural connected only to a subset of the input image (unlike a neural network where all the neurons are fully connected)
* This helps to reduce the number of parameters in the whole system and makes the computation more efficient.
## How Convolution Works
* Step 1: Break the image into overlapping image tiles
* Step 2: Feed each image tile into a small neural network
* Step 3: Save the results from each tile into a new array
* Step 4: Downsampling
To reduce the size of the array, we downsample it using an algorithm called max pooling.just look at each 2x2 square of the array and keep the biggest number.
The idea here is that if we found something interesting in any of the four input tiles that makes up each 2x2 grid square, we’ll just keep the most interesting bit. This reduces the size of our array while keeping the most important bits.
* Final step: Make a prediction

## Pooling Back Prop
>Backward propagation of Average Pooling Layer
  ![alt text](https://lanstonchu.files.wordpress.com/2018/08/avg-pool.gif?w=825)
  
>Backward propagation of Maximum Pooling Layer
![alt text](https://lanstonchu.files.wordpress.com/2018/08/max-pool.gif?w=825)

## What i learned from this chapter
- Qu'est-ce qu'une couche convolutionnelle?
- Qu'est-ce qu'une couche de pooling?
- Propagation directe sur des couches convolutives et de mise en commun
- Propagation en retour sur les couches convolutives et de regroupement
- Comment créer un CNN à l'aide de Tensorflow et Keras

## Author
* **Mouhamed Charfi** - [medcharfi96](https://github.com/medcharfi96)