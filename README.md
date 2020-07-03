# Hand Written Digit Recognition
Hand Written Digit Recognition using javascript library tensorflowjs
 
The original demo has been wrapped as a jupyter-server-proxy application allowing it to be used directly within a Jupyter noteobok context: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ouseful-PR/Hand-Written-Digit-Recognition/serverproxy)


See also:
- [`nb_tensorspace_server_proxy`](https://github.com/innovationOUtside/nb_tensorspace_server_proxy) which does a similar thing for a couple of smaller networks in the *TensorSpace Playground*.
- [`nb_tensorflow_playground_serverproxy`](https://github.com/innovationOUtside/nb_tensorflow_playground_serverproxy) which does a similar thing for the *Tensorflow Playground*.

 
## OriginalLive Demo
**[https://bensonruan.com/handwritten-digit-recognition-with-tensorflow-js/](https://bensonruan.com/handwritten-digit-recognition-with-tensorflow-js/)**

![handwritten-recognition](https://bensonruan.com/wp-content/uploads/2019/09/handwritten-recognition-5.gif)
 
## Installing
Clone this repository to your local computer
``` bash
git https://github.com/bensonruan/Hand-Written-Digit-Recognition.git
```
Point your localhost to the cloned root directory

Browse to http://localhost/index.html  

## Start Predicting Hand Written Digit
* Draw on the canvas with your mouse on desktop or your finger on your mobile
* Click "Predict" to get result of the hand written digit prediction
* Click "Clean" to start drawing again

## Pre-trained model 
Use MNIST dataset from Keras with CNN (Convolutional Neural Network)
```python
model = keras.Sequential([
    keras.layers.Conv2D(32, (5, 5), padding="same", input_shape=[28, 28, 1]),
    keras.layers.MaxPool2D((2,2)),
    keras.layers.Conv2D(64, (5, 5), padding="same"),    
    keras.layers.MaxPool2D((2,2)),    
    keras.layers.Flatten(),   
    keras.layers.Dense(1024, activation='relu'),    
    keras.layers.Dropout(0.2),   
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
```

## Library
* [jquery](https://code.jquery.com/jquery-3.3.1.min.js) - JQuery
* [tensorflowjs](https://github.com/tensorflow/tfjs) - JavaScript library for training and deploying machine learning models
* [Chart.js](https://github.com/chartjs/Chart.js) - JavaScript library for display charts
