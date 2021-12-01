# 0x10. Natural Language Processing - Evaluation Metrics
***What is the Attention mechanism?***
* A method for determining which terms are most important in a sequence

***A Transformer:***
* Is a novel neural network
* Utilizes the Attention mechanism
* Utilizes dropout
* Utilizes layer normalization

***BERT was novel because:***

* It introduced self-supervised learning techniques
* It can be fine tuned for various NLP tasks
* 
***The database to use for Question-Answering is:***
* SQuAD

***Layer Normalization is different from Batch Normalization because:***
* It normalizes the layer output for each example instead of across the batch
## Attention 
The attention mechanism is a part of a neural architecture
that enables to dynamically highlight relevant features of the
input data, which, in NLP, is typically a sequence of textual
elements. It can be applied directly to the raw input or to its
higher level representation. The core idea behind attention is to
compute a weight distribution on the input sequence, assigning
higher values to more relevant elements.
## Self Attention

![alt text](https://miro.medium.com/max/700/1*1je5TwhVAwwnIeDFvww3ew.gif)
## What is a transformer?
The Transformer in NLP is a novel architecture that aims to solve sequence-to-sequence tasks while handling long-range dependencies with ease
The idea behind Transformer is to handle the dependencies between input and output with attention and recurrence completely.
## difference between transformer and rnn
Like recurrent neural networks (RNNs), transformers are designed to handle sequential input data, such as natural language, for tasks such as translation and text summarization. However, unlike RNNs, transformers do not require that the sequential data be processed in order. Rather, the attention operation provides context for any position in the input sequence. For example, if the input data is a natural language sentence, the transformer does not need to process the beginning of the sentence before the end. Rather, it identifies the context that confers meaning to a word in the sentence. Due to this feature, the transformer allows for much more parallelization than RNNs and therefore reduces training times
![alt text](https://miro.medium.com/max/700/1*Iygs9mQi4GbIJuc6fwBRKg.png)
## GPT
Generative Pre-trained Transformer 3 (GPT-3) is an autoregressive language model that uses deep learning to produce human-like text. It is the third-generation language prediction.
 we can say that the GPT-2 is basically the next word prediction feature of a keyboard app, but one that is much larger and more sophisticated than what your phone has.
 ## BERT
BERT, which stands for Bidirectional Encoder Representations from Transformers, is a neural network-based technique for natural language processing pre-training. In plain English, it can be used to help Google better discern the context of words in search queries.

For example, in the phrases “nine to five” and “a quarter to five,” the word “to” has two different meanings, which may be obvious to humans but less so to search engines. BERT is designed to distinguish between such nuances to facilitate more relevant results.
The breakthrough of BERT is in its ability to train language models based on the entire set of words in a sentence or query (bidirectional training) rather than the traditional way of training on the ordered sequence of words (left-to-right or combined left-to-right and right-to-left). BERT allows the language model to learn word context based on surrounding words rather than just the word that immediately precedes or follows it.

 ## GLUE
 The General Language Understanding Evaluation (GLUE) benchmark is a collection of resources for training, evaluating, and analyzing natural language understanding systems. GLUE consists of:
* A benchmark of nine sentence- or sentence-pair language understanding tasks built on established existing datasets and selected to cover a diverse range of dataset sizes, text genres, and degrees of difficulty,
* A diagnostic dataset designed to evaluate and analyze model performance with respect to a wide range of linguistic phenomena found in natural language, and
* A public leaderboard for tracking performance on the benchmark and a dashboard for visualizing the performance of models on the diagnostic set. 

## Author
* **Mouhamed Charfi** - [medcharfi96](https://github.com/medcharfi96)
