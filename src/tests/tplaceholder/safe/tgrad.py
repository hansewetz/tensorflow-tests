#!/usr/bin/env python
import tensorflow as tf
import numpy as np

# generate some data
n = 100
xn = 2 * np.random.rand(n,1)
xbn = np.c_[np.ones((n, 1)), xn]  # add a column of '1'ns
yn = 4 + 3 * xn + np.random.rand(n,1)

# params
lrate = 0.01
nepochs = 1000

# setup for tf
x = tf.constant(xbn, dtype = tf.float32, name = "x")
y = tf.constant(yn, dtype = tf.float32, name = "y")
theta = tf.Variable(tf.random_uniform([2,1],-1.0,1.0), name = "theta")
ypred = tf.einsum('ik,kj->ij',x, theta, name = "ypred")
mse = tf.reduce_mean(tf.square(ypred - y), name = "mse")    # mean square error
opt = tf.train.MomentumOptimizer(learning_rate = lrate, momentum = 0.9)
trainopt = opt.minimize(mse)

init = tf.global_variables_initializer()
with tf.Session() as sess:
  init.run()
  for epoch in range(nepochs):
    if epoch%100==0:
      print 'epoch: ', epoch, ', mse: ', mse.eval(), ', theta: ', theta.eval()
    sess.run(trainopt)
  #best_theta = theta.eval()
