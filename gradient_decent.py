import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf
x = tf.Variable(4.0)
print("Initial value of x:", x.numpy())
with tf.GradientTape() as tape:
  y = x**3 + 3 * x + 5
  print("Value of y:", y.numpy())
  dy_dx = tape.gradient(y, x) # calculate differential of y with respect to x
  print("Gradient of y with respect to x:", dy_dx.numpy())
  