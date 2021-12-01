# RNN
The idea behind RNNs is to make use of sequential information. In a traditional neural network we assume that all inputs (and outputs) are independent of each other. But for many tasks that’s a very bad idea. If you want to predict the next word in a sentence you better know which words came before it. RNNs are called recurrent because they perform the same task for every element of a sequence, with the output being depended on the previous computations. Another way to think about RNNs is that they have a “memory” which captures information about what has been calculated so far.
Unlike a traditional deep neural network, which uses different parameters at each layer, a RNN shares the same parameters (U, V, W above) across all steps. This reflects the fact that we are performing the same task at each step, just with different inputs. This greatly reduces the total number of parameters we need to learn.

##  0. RNN Cell

RNN cells distinguish themselves from the regular neurons in the sense that they have a state and thus can remember information from the past. RNN cells form the backbone of recurrent networks.
On a mathematical level, a sequence of inputs are passed through an RNN cell, one at a time. The state of the cell helps it remember the past sequence and combine that information with the current input to provide an output. An easier way to look at it is by unrolling what happens during the sequence which reveals a simpler Deep Network.

![alt text](https://miro.medium.com/max/700/1*NKhwsOYNUT5xU7Pyf6Znhg.png)

## The Problem, Short-term Memory

Recurrent Neural Networks suffer from short-term memory. If a sequence is long enough, they’ll have a hard time carrying information from earlier time steps to later ones. So if you are trying to process a paragraph of text to do predictions, RNN’s may leave out important information from the beginning.
During back propagation, recurrent neural networks suffer from the vanishing gradient problem. Gradients are values used to update a neural networks weights. The vanishing gradient problem is when the gradient shrinks as it back propagates through time. If a gradient value becomes extremely small, it doesn’t contribute too much learning.

## LSTM’s and GRU’s as a solution
LSTM ’s and GRU’s were created as the solution to short-term memory. They have internal mechanisms called gates that can regulate the flow of information.

![alt text](https://miro.medium.com/max/700/1*yBXV9o5q7L_CvY7quJt3WQ.png)

These gates can learn which data in a sequence is important to keep or throw away.

## LSTM Cell

![alt text](https://miro.medium.com/max/700/1*GjehOa513_BgpDDP6Vkw2Q.gif)

**forget gate** This gate decides what information should be thrown away or kept. Information from the previous hidden state and information from the current input is passed through the sigmoid function.

**The cell state** act as a transport highway that transfers relative information all the way down the sequence chain. You can think of it as the “memory” of the network. The cell state, in theory, can carry relevant information throughout the processing of the sequence.
**the output gate** The output gate decides what the next hidden state should be.

**The hidden state** acts as the neural networks memory. It holds information on previous data the network has seen before.

## GRU

![alt text](https://miro.medium.com/max/700/1*jhi5uOm9PvZfmxvfaCektw.png)

**The update gate** acts similar to the forget and input gate of an LSTM. It decides what information to throw away and what new information to add.

**The reset gate** is another gate is used to decide how much past information to forget.

## 3-Deep Recurrent Neural Networks

![alt text](http://www.dinalherath.com/material/2019/post_12/model_image.jpeg)

## Bidirectional recurrent neural networks(RNN)

![alt text](https://miro.medium.com/max/700/1*6QnPUSv_t9BY9Fv8_aLb-Q.png)
Bidirectional recurrent neural networks(RNN) are really just putting two independent RNNs together. The input sequence is fed in normal time order for one network, and in reverse time order for another. The outputs of the two networks are usually concatenated at each time step, though there are other options, e.g. summation.
This structure allows the networks to have both backward and forward information about the sequence at every time step.

https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21

## Author
* **Mouhamed Charfi** - [medcharfi96](https://github.com/medcharfi96)