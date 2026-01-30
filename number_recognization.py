import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import datetime
from tensorflow.keras.utils import plot_model
mnist = tf.keras.datasets.mnist # Load MNIST dataset into the code
(x_train, y_train), (x_test, y_test) = mnist.load_data()
some_digit_image = x_train[0]
plt.imshow(some_digit_image, cmap=plt.cm.binary, interpolation="nearest")
print(np.shape(x_train))
plt.title(f"Label: {y_train[59999]}") # Optional: Display the label
plt.axis("off") # Turn off axis labels and ticks
plt.show()
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.Dense(100, activation='relu'))
model.add(tf.keras.layers.Dense(100, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()
#print(model.layers[0].get_weights()[0].shape)  # Check the shape of the weights
history=model.fit(x_train, y_train, epochs=3,batch_size=100)
loss, accuracy = model.evaluate(x_test, y_test)
print(model.layers[1].get_weights())
print(model.layers[1].output_shape)
""" for i in range(len(x_test)):
    prediction = model.predict(np.reshape(x_test[i] , (1,28,28)))
    print(f"Prediction for image {i} is {np.argmax(prediction)}")
    if np.argmax(prediction) != y_test[i]:
        print("Incorrect prediction")
        plt.imshow(x_test[i], cmap=plt.cm.binary, interpolation="nearest")
        print(np.shape(x_train))
        plt.title(f"Label: {y_test[i]}") # Optional: Display the label
        plt.axis("off") # Turn off axis labels and ticks
        plt.show() """
#print("Loss : ", loss)
#print("Accuracy : ", accuracy)
#print(f"Validation Accuracy: {accuracy * 100:.2f}%")
#plt.plot(history.history['accuracy'], label='Training Accuracy')
#plt.plot(history.history['loss'], label='Validation Loss')
#plt.legend()
#plt.show()
#plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)