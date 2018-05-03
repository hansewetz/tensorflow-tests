#!/usr/bin/env python
import tensorflow as tf
import numpy as np

# generate some data
nsamples = 10000
xn = 2*np.random.rand(nsamples,1)
xbn = np.c_[np.ones((nsamples, 1)), xn]          # add a column of '1'ns   (100,2)
yn = 10.0 + 3.0 * xn + np.random.rand(nsamples,1)#                         (100,1)

# params
lrate = 0.01
nepochs = 1000

# build graph
x = tf.placeholder(tf.float32, shape=[None,2], name = "x")
y = tf.placeholder(tf.float32, shape = [None,1], name = "y")
theta = tf.Variable(tf.random_uniform([2,1],-1.0,1.0), name = "theta")
ypred = tf.einsum('ik,kj->ij',x, theta, name = "ypred")
mse = tf.reduce_mean(tf.square(ypred - y), name = "mse")    # mean square error
#opt = tf.train.MomentumOptimizer(learning_rate = lrate, momentum = 0.9)
opt = tf.train.GradientDescentOptimizer(learning_rate = lrate)
trainopt = opt.minimize(mse)

init = tf.global_variables_initializer()
with tf.Session() as sess:
  init.run()
  for epoch in range(nepochs):
    sess.run(trainopt, feed_dict={x: xbn, y: yn})    # feed numpy tensors into graph
    if epoch%100==0:
      print 'epoch: ', epoch, 'theta: ', theta.eval()
