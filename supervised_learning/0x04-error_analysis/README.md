# 0x04. Error Analysis

## Confusion matrix
a confusion matrix, also known as an error matrix, is a specific table layout that allows visualization of the performance of an algorithm, typically a supervised learning one (in unsupervised learning it is usually called a matching matrix).

![alt text](https://classeval.files.wordpress.com/2015/06/four-outcomes-of-classifier.png?w=480&h=202)

## 1. Sensitivity (Recall or True positive rate)

Sensitivity (SN) is calculated as the number of correct positive predictions divided by the total number of positives. It is also called recall (REC) or true positive rate (TPR). The best sensitivity is 1.0, whereas the worst is 0.0.

![alt text](https://classeval.files.wordpress.com/2015/06/sensitivity.png?w=440&h=155)

![alt text](https://s0.wp.com/latex.php?latex=%5Cmathrm%7BSN+%3D+%5Cdisplaystyle+%5Cfrac%7BTP%7D%7BTP+%2B+FN%7D+%3D+%5Cfrac%7BTP%7D%7BP%7D%7D&bg=ffffff&fg=333333&s=0&c=20201002)



## 2. Precision (Positive predictive value)
Precision (PREC) is calculated as the number of correct positive predictions divided by the total number of positive predictions. It is also called positive predictive value (PPV). The best precision is 1.0, whereas the worst is 0.0.

![alt text](https://classeval.files.wordpress.com/2015/06/precision.png?w=440&h=155)

![alt text](https://s0.wp.com/latex.php?latex=%5Cmathrm%7BPREC+%3D+%5Cdisplaystyle+%5Cfrac%7BTP%7D%7BTP+%2B+FP%7D%7D&bg=ffffff&fg=333333&s=0&c=20201002)



## 3. Specificity (True negative rate)
Specificity (SP) is calculated as the number of correct negative predictions divided by the total number of negatives. It is also called true negative rate (TNR). The best specificity is 1.0, whereas the worst is 0.0.

![alt text](https://classeval.files.wordpress.com/2015/06/specificity.png?w=440&h=155)

![alt text](https://s0.wp.com/latex.php?latex=%5Cmathrm%7BSP+%3D+%5Cdisplaystyle+%5Cfrac%7BTN%7D%7BTN+%2B+FP%7D+%3D+%5Cfrac%7BTN%7D%7BN%7D%7D&bg=ffffff&fg=333333&s=0&c=20201002)

## 4 . F1 score
the F-score or F-measure is a measure of a test's accuracy. It is calculated from the precision and recall of the test.

![alt text](https://wikimedia.org/api/rest_v1/media/math/render/svg/9c94f59b68f5ae0dc92185906c7ec4214fd04e1e)

## 5. Dealing with Error
1. High Bias
* Train more
* Try a different architecture
* Build a deeper network

2. High Variance
* Try a different architecture
* Get more data
* Use regularization
## What i learned from  this chapter

- What is the confusion matrix?
- What is type I error? type II?
- What is sensitivity? specificity? precision? recall?
- What is an F1 score?
- What is bias? variance?
- What is irreducible error?
- What is Bayes error?st-ce que l'erreur de Bayes?
- How can you approximate Bayes error?
- How to calculate bias and variance
- How to create a confusion matrix

### Done by :  Mouhamed charfi