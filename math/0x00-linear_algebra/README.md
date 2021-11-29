# linear algebra

## numpy 

 is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. The ancestor of NumPy
## numpy.matmul
```sh


a = np.array([[1, 0],
              [0, 1]])
b = np.array([[4, 1],
              [2, 2]])
np.matmul(a, b)
array([[4, 1],
       [2, 2]])
```


## numpy.transpose
```sh


a = np.array([[1, 2], [3, 4]])
a
array([[1, 2],
       [3, 4]])
a.transpose()
array([[1, 3],
       [2, 4]])
a.transpose((1, 0))
array([[1, 3],
       [2, 4]])
a.transpose(1, 0)
array([[1, 3],
       [2, 4]])
or 
a.T       
```



## numpy.concatenate
```sh

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
np.concatenate((a, b), axis=0)
array([[1, 2],
       [3, 4],
       [5, 6]])
np.concatenate((a, b.T), axis=1)
array([[1, 2, 5],
       [3, 4, 6]])
np.concatenate((a, b), axis=None)
array([1, 2, 3, 4, 5, 6])

```


### operations



```sh
add = np.add(mat1, mat2)
    diff = np.subtract(mat1, mat2)
    mul = np.multiply(mat1, mat2)
    div = np.divide(mat1, mat2)
```
## Author
* **Mouhamed Charfi** - [medcharfi96](https://github.com/medcharfi96)