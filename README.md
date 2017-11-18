# MNIST digit recognition demo

<img src="https://github.com/awadalaa/mnist_demo/blob/master/demo.gif" width="80%">

## Introduction
1. How to export a model and have a simple self-sufficient file for it
2. How to build a simple python server (using flask) to serve a TensorFlow model

## Installation
Clone the respository:
`git clone https://github.com/<username>/mnist_demo.git`

## Install Dependencies such as virtualenv, flask, and tensorflow
`pip install -r requirements.txt`

`virtualenv env`

`source env/bin/activate`

## Start the server
`gunicorn app:app --log-file=-`
