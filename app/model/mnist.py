import tensorflow as tf
# The MNIST data is split into three parts:
# 	55,000 data points of training data (mnist.train),
# 	10,000 points of test data (mnist.test),
# 	and 5,000 points of validation data (mnist.validation). 
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)


# Both the training set and test set contain images and their corresponding labels;
# for example the training images are mnist.train.images and 
# the training labels are mnist.train.labels
# 
# Each image is 28 pixels by 28 pixels. We can interpret this as a big array of numbers:
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x,W) + b)
y_ = tf.placeholder(tf.float32, [None, 10])

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

sess = tf.InteractiveSession()

tf.global_variables_initializer().run()

for _ in range(100):
	batch_xs, batch_ys = mnist.train.next_batch(100)
	sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

print('model accuracy:',sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
