# 0x02. Hidden Markov Models
Hidden Markov models are generative models, in which the joint distribution of observations and hidden states, or equivalently both the prior distribution of hidden states (the transition probabilities) and conditional distribution of observations given states (the emission probabilities), is modeled. 
## 0. Markov Chain
``` python
#P :the transition matrix
#S: representing the probability of starting in each state
S[i] = P * S[i-1]
```
## 1. Regular Chains
```python
s * p = s
```
## 2. Absorbing Chains
In the mathematical theory of probability, an absorbing Markov chain is a Markov chain in which every state can reach an absorbing state. An absorbing state is a state that, once entered, cannot be left.
## 3. The Forward Algorithm
![alt text](https://i.ibb.co/rp58J8X/forward.png)
## 4. The Viretbi Algorithm
![alt text](https://i.ibb.co/d2QTTr2/viterbi.png)

## What i learned from  this chapter
-    What is the Markov property?
-   What is a Markov chain?
-    What is a state?
-    What is a transition probability/matrix?
-    What is a stationary state?
-    What is a regular Markov chain?
-    How to determine if a transition matrix is regular
-    What is an absorbing state?
-    What is a transient state?
-    What is a recurrent state?
-    What is an absorbing Markov chain?
-    What is a Hidden Markov Model?
-    What is a hidden state?
-    What is an observation?
-    What is an emission probability/matrix?
-    What is a Trellis diagram?
-   What is the Forward algorithm and how do you implement it?
-    What is decoding?
-    What is the Viterbi algorithm and how do you implement it?
-    What is the Forward-Backward algorithm and how do you implement it?
-    What is the Baum-Welch algorithm and how do you implement it?


## Author
* **Mouhamed Charfi** - [medcharfi96](https://github.com/medcharfi96)