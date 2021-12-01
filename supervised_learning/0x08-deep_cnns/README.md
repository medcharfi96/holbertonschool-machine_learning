# 0x08. Deep Convolutional Architectures

## Vanishing gradient problem
In machine learning, the vanishing gradient problem is encountered when training artificial neural networks with gradient-based learning methods and backpropagation. In such methods, each of the neural network's weights receives an update proportional to the partial derivative of the error function with respect to the current weight in each iteration of training. The problem is that in some cases, the gradient will be vanishingly small, effectively preventing the weight from changing its value. In the worst case, this may completely stop the neural network from further training.

 ## What is a skip connection
Basically, skip connection is a standard module in many convolutional architectures. By using a skip connection, we provide an alternative path for the gradient (with backpropagation). It is experimentally validated that these additional paths are often beneficial for the model convergence. Skip connections in deep architectures, as the name suggests, skip some layer in the neural network and feeds the output of one layer as the input to the next layers (instead of only the next one)

## 0. Inception Block

  ![alt text](https://miro.medium.com/max/1646/1*U_McJnp7Fnif-lw9iIC5Bw.png)
  
## 2. Identity Block
  

![alt text](https://www.researchgate.net/profile/Antonio_Theophilo/publication/321347448/figure/fig2/AS:565869411815424@1511925189281/Bottleneck-Blocks-for-ResNet-50-left-identity-shortcut-right-projection-shortcut.png)

 ## 3. Projection Block
![alt text](https://www.researchgate.net/profile/Antonio_Theophilo/publication/321347448/figure/fig2/AS:565869411815424@1511925189281/Bottleneck-Blocks-for-ResNet-50-left-identity-shortcut-right-projection-shortcut.png)

## 4. ResNet-50 
the first block is the projection block and the rest are identity blocks. So for ‘conv2_x’, the first block is a projection block and the other two repetitions are identity blocks.
The reason the first block is projection is to make sure, that the strides and the number of filters of the input from skip connection and the actual output of the block are the same. In the projection block, the first convolutional layer has strides=2. This means that if the input is an image, the size of the image after this layer will decrease. But the input in skip connection still has the previous image size. Adding two images of different sizes is not possible. So the skip connection also has a convolutional layer with stride=2. This makes sure that the image sizes are now the same.
## 5. Dense Block 
#### What does a bottleneck layer mean in neural networks?
A bottleneck layer is a layer that contains few nodes compared to the previous layers. It can be used to obtain a representation of the input with reduced dimensionality. An example of this is the use of autoencoders with bottleneck layers for nonlinear dimensionality reduction.
``` sh
def preact_layer(x, num_channels, l2_reg, dropout, kernel_size=3,
                 name='layer'):
    '''
    Adds a preactivation layer for the densenet. This also includes l2
    reagularization on BatchNorm learnable parameters as in the original
    implementation.
    '''

    out = BatchNormalization(gamma_regularizer=l2(l2_reg),
                             beta_regularizer=l2(l2_reg),
                             name=name + '_bn')(x)
    out = Activation('relu', name=name + '_relu')(out)
    out = Convolution2D(num_channels, kernel_size, kernel_size,
                        border_mode='same', init='he_normal',
                        W_regularizer=l2(l2_reg), bias=False,
                        name=name + '_conv')(out)
    if dropout > 0:
        out = Dropout(dropout)(out)
    return out

def bottleneck_layer(x, num_channels, l2_reg, dropout, kernel_size=3,
                     name='layer'):
    '''
    DenseNet-B: 1x1 conv bottleneck before 3x3 conv
    '''
    o = preact_layer(x, num_channels*4, l2_reg, dropout, kernel_size=1,
                     name=name+'_bottleneck')
    o = preact_layer(o, num_channels, l2_reg, dropout, kernel_size=kernel_size,
                     name=name+'_main')

    return o
```
DenseNet is one of the new discoveries in neural networks for visual object recognition. DenseNet is quite similar to ResNet with some fundamental differences. ResNet uses an additive method (+) that merges the previous layer (identity) with the future layer, whereas DenseNet concatenates .
DenseNet was developed specifically to improve the declined accuracy caused by the vanishing gradient in high-level neural networks. In simpler terms, due to the longer path between the input layer and the output layer, the information vanishes before reaching its destination.


## 6. Transition Layer
```
#compression: calculated as 1 - reduction. Reduces the number
 of feature maps in the transition block.
#Output shape
4D tensor with shape:
        (samples, nb_filter * compression, rows / 2, cols / 2)`
```
Instead of summing the residual like in ResNet, DenseNet concatenates all the feature maps.

It would be impracticable to concatenate feature maps of different sizes (although some resizing may work). Thus in each dense block, the feature maps of each layer has the same size.

However down-sampling is essential to CNN. Transition layers between two dense blocks assure this role.

A transition layer is made of:

* Batch Normalization
* 1x1 Convolution
* Average pooling
## 7. DenseNet-121
```sh
__growth_rate: number of filters to add per dense block
__nb_filter: initial number of filters. Default -1 indicates initial number
of filters is 2 * growth_rate
# compute initial nb_filter if -1, else accept users initial nb_filter
        if nb_filter <= 0:
            nb_filter = 2 * growth_rate
```
![alt text](https://pytorch.org/assets/images/densenet2.png)


## What i learned from this chapter
- What is a skip connection?
- What is a bottleneck layer?
- What is the Inception Network?
- What is ResNet? ResNeXt? DenseNet?
- How to replicate a network architecture by reading a journal article

## Author
* **Mouhamed Charfi** - [medcharfi96](https://github.com/medcharfi96)