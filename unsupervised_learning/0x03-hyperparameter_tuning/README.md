# 0x03. Hyperparameter Tuning

## 1. Gaussian Process
In probability theory and statistics, a Gaussian process is a stochastic process (a collection of random variables indexed by time or space), such that every finite collection of those random variables has a multivariate normal distribution, i.e. every finite linear combination of them is normally distributed.
![alt text](https://www.astroml.org/_images/fig_gp_example_1.png)
##  Bayesian Optimization
This is the core question in Bayesian Optimization: “Based on what we know so far, which point should we evaluate next?” Remember that evaluating each point is expensive, so we want to pick carefully! In the active learning case, we picked the most uncertain point, exploring the function. But in Bayesian Optimization, we need to balance exploring uncertain regions, which might unexpectedly have high gold content, against focusing on regions we already know have higher gold content (a kind of exploitation).

We make this decision with something called an acquisition function. Acquisition functions are heuristics for how desirable it is to evaluate a point, based on our present model 4 . We will spend much of this section going through different options for acquisition functions.

This brings us to how Bayesian Optimization works. At every step, we determine what the best point to evaluate next is according to the acquisition function by optimizing it. We then update our model and repeat this process to determine the next point to evaluate.

You may be wondering what’s “Bayesian” about Bayesian Optimization if we’re just optimizing these acquisition functions. Well, at every step we maintain a model describing our estimates and uncertainty at each point, which we update according to Bayes’ rule

 at each step. Our acquisition functions are based on this model, and nothing would be possible without them!


  To solve this problem, we will follow the following algorithm:
 * 1-We first choose a surrogate model for modeling the true function ff and define its prior.
 *  2-Given the set of observations (function evaluations), use Bayes rule to obtain the posterior.
 * 3-Use an acquisition function α(x), which is a function of the posterior, to decide the next sample point x_t =argmaxx α(x).
 * 4-Add newly sampled data to the set of observations and goto step #2 till convergence or budget elapses.

![alt text](https://distill.pub/2020/bayesian-optimization/images/MAB_pngs/PI/0.075/2.png)
![alt text](https://distill.pub/2020/bayesian-optimization/images/MAB_pngs/PI/0.075/3.png)
![alt text](https://distill.pub/2020/bayesian-optimization/images/MAB_pngs/PI/0.075/4.png)
![alt text](https://distill.pub/2020/bayesian-optimization/images/MAB_pngs/PI/0.075/5.png)

## What i learned from  this chapter
-    What is Hyperparameter Tuning?
-    What is random search? grid search?
-    What is a Gaussian Process?
-    What is a mean function?
-    What is a Kernel function?
-    What is Gaussian Process Regression/Kriging?
-    What is Bayesian Optimization?
-    What is an Acquisition function?
-    What is Expected Improvement?
-    What is Knowledge Gradient?
-    What is Entropy Search/Predictive Entropy Search?
-    What is GPy?
-    What is GPyOpt?

## Author
* **Mouhamed Charfi** - [medcharfi96](https://github.com/medcharfi96)