# 0x06-keras
Keras is an open-source software library that provides a Python interface for artificial neural networks. Keras acts as an interface for the TensorFlow library.
Keras is the most used deep learning framework among top-5 winning teams on Kaggle. Because Keras makes it easier to run new experiments, it empowers you to try more ideas than your competition, faster.


## 0. Sequential
```sh
model = k.Sequential()
 model.add(k.layers.Dense()
 model.add(k.layers.Dropout(1-keep_prob))
```
## 1. Input
```sh
k.Input(shape=(nx,))
```
## 2. Optimize
```sh
k.optimizers.Adam()
```

## 3. One Hot
```sh
k.utils.to_categorical()
```
## 4. Train 
```sh
network.fit()
```
## 5. Validate
## 6. Early Stopping
## 7. Learning Rate Decay
## 8. Save Only the Best
## 9. Save and Load Model
```sh
 network.save(filename)
 network = K.models.load_model(filename)
 ```
 ## 10. Save and Load Weights
 ```sh
 network.save_weights(filename, save_format=save_format)
 network.load_weights(filename)
 ```
 ## 11. Save and Load Configuration
 saves a model’s configuration in JSON format
 ## 12. Test
 ```sh
 network.evaluate(x=data, y=labels, verbose=verbose)
 ```
## 13. Predict
```sh
network.predict(data, verbose=verbose)
```
## What i learned from this chapter

- What is Keras?
- What is a model?
- How to instantiate a model (2 ways)
- How to build a layer
- How to add regularization to a layer
- How to add dropout to a layer
- How to add batch normalization
- How to compile a model
- How to optimize a model
- How to fit a model
- How to use validation data
- How to perform early stopping
- How to measure accuracy
- How to evaluate a model
- How to make a prediction with a model
- How to access the weights/outputs of a model
What is HDF5?
- How to save and load a model’s weights, a model’s configuration, and the entire model

## Author
* **Mouhamed Charfi** - [medcharfi96](https://github.com/medcharfi96)