# bengali-handwritten-digit-recognizer

# Intro

This repo contain all the files used for the bengali handwritten digit recognition challenge. The files are placed in folders as follows(except for the notebooks) : 

- Jupyeter notebooks for the codes
- the trained models
- the labelled csv file of the output acheived from the test set
- image of random digits from the test set with top three prediction labels

# Results 

Using Keras, a multi-layered convolutional neural network was made based on the classic LeNet architecture. It was trained on the dataset provided. And ran on only 5 epochs with the following outputs. 

- Loss: 0.3241 
- Accuracy : 0.8938 (89%)
- Validation Loss: 0.3074 
- Validation Accuracy: 0.8994

Below is the predictions made on random images on the test set using this model.


<p align="center">
  <img src="https://github.com/hasibzunair/bengali-handwritten-digit-recognizer/blob/master/results/first_keras.png">
</p>


# Competition Link 
https://www.kaggle.com/c/numta/

