# Dimensionality reduction
 Dimensionality reduction, or dimension reduction, is the transformation of data from a high-dimensional space into a low-dimensional space so that the low-dimensional representation retains some meaningful properties of the original data.
 
## pca
Principal component analysis (PCA) is the process of computing the principal components and using them to perform a change of basis on the data, sometimes using only the first few principal components and ignoring the rest.
It is commonly used for dimensionality reduction by projecting each data point onto only the first few principal components to obtain lower-dimensional data while preserving as much of the data's variation as possible.

```sh
t = xw
```

## SVD
In linear algebra, the singular value decomposition (SVD) is a factorization of a real or complex matrix that generalizes the eigendecomposition of a square normal matrix to any. matrix via an extension of the polar decomposition.
![alt text](https://staging.njtrainingacademy.com/wp-content/uploads/2019/01/svd_heading_img.png)

```SH
    U, S, V = np.linalg.svd(X)
    W = V 
    T = XV = US
```
## What i learned from  this chapter


    - What is eigendecomposition?
    - What is singular value decomposition?
    - What is the difference between eig and svd?
    - What is dimensionality reduction and - what are its purposes?
    - What is principal components analysis (PCA)?
    - What is t-distributed stochastic neighbor embedding (t-SNE)?
    - What is a manifold?
    - What is the difference between linear and non-linear dimensionality reduction?
    - Which techniques are linear/non-linear?

## Author
* **Mouhamed Charfi** - [medcharfi96](https://github.com/medcharfi96)