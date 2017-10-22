from PIL import Image
from io import BytesIO
import numpy as np
import tensorflow as tf
import base64

from flask import render_template
from flask import request
from flask import jsonify

from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/api/predict", methods=['POST'])
def prediction():
    # Get json data from user
    data = request.get_json('img')
    img_base64 = data['img']

    # Process image from byte64 encoding -> image -> tensor
    img = Image.open(BytesIO(base64.b64decode(img_base64)))
    img = img.convert(mode='L')
    img = img.resize((28, 28), resample=Image.NEAREST)
    tensor = np.invert(np.array(img.getdata()))
    tensor = tensor.reshape((1, 784))
    img.close()

    print('tensor_shape:',tensor.shape)

    # recreating the graph
    # x = tf.placeholder(tf.float32, [None, 784])
    # W = tf.Variable(tf.zeros([784, 10]))
    # b = tf.Variable(tf.zeros([10]))
    # y = tf.nn.softmax(tf.matmul(x,W) + b)

    # Launch the graph
    with tf.Session() as sess:
        #First let's load meta graph and restore weights
        saver = tf.train.import_meta_graph('./app/model/v1.00/model.ckpt.meta')
        saver.restore(sess, "./app/model/v1.00/model.ckpt")

        # Now, let's access and create placeholders variables and
        # create feed-dict to feed new data
        graph = tf.get_default_graph()
        x = graph.get_tensor_by_name("x:0")
        y = graph.get_tensor_by_name("y:0")
        feed_dict = {x:tensor}
        # #Now, access the op that you want to run. 
        one_hot_vector = sess.run(y, feed_dict=feed_dict)
        digit = tf.argmax(one_hot_vector, axis=1)
        digit = digit.eval()[0]
        print('one_hot_vector:',one_hot_vector)
    print('Test Accuracy: {}'.format(one_hot_vector[0][digit]))
    return jsonify(status='success',
                   probabilities=float(one_hot_vector[0][digit]),
                   predicted_class=digit)

