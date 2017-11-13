from PIL import Image
from io import BytesIO
import numpy as np
import tensorflow as tf
import base64
from model import mnist

from flask import render_template, request, jsonify

from app import app

x = tf.placeholder("float", [None, 784])
sess = tf.Session()

# restore trained data
with tf.variable_scope("regression"):
    y1, variables = mnist.regression(x)
saver = tf.train.Saver(variables)
saver.restore(sess, "app/model/data/regression.ckpt")


with tf.variable_scope("convolutional"):
    keep_prob = tf.placeholder("float")
    y2, variables = mnist.convolutional(x, keep_prob)
saver = tf.train.Saver(variables)
saver.restore(sess, "app/model/data/convolutional.ckpt")

def regression(input):
    return sess.run(y1, feed_dict={x: input}).flatten().tolist()


def convolutional(input):
    return sess.run(y2, feed_dict={x: input, keep_prob: 1.0}).flatten().tolist()



@app.route('/api/predict', methods=['POST'])
def predict():
    input = ((255 - np.array(request.json, dtype=np.uint8)) / 255.0).reshape(1, 784)
    output1 = regression(input)
    output2 = convolutional(input)
    return jsonify(results=[output1, output2])


@app.route('/')
def index():
    return render_template('index.html')
