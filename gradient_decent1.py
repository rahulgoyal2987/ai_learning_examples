import tensorflow as tf
class SimpleModel(tf.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.w = tf.Variable(0.0, name='weight')
        self.b = tf.Variable(0.0, name='bias')

    @tf.function
    def __call__(self, x):
        return self.w * x + self.b
    
    
xdata = tf.constant([1.0, 2.0, 3.0, 4.0], dtype=tf.float32)
ydata = tf.constant([3.0, 6.0, 9.0, 12.0], dtype=tf.float32)
model = SimpleModel()
learning_rate = 0.02
for step in range(1):
    with tf.GradientTape() as tape:
        y_pred = model(xdata)
        loss = tf.reduce_mean(tf.square(y_pred - ydata))

    gradients = tape.gradient(loss, [model.w, model.b])
    model.w.assign_sub(learning_rate * gradients[0])
    model.b.assign_sub(learning_rate * gradients[1])

    #if step % 10 == 0:
    print(f"Step {step}, Loss: {loss.numpy()}, Weight: {model.w.numpy()}, Bias: {model.b.numpy()}")
