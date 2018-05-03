#!/usr/bin/env python
import tensorflow as tf

# tf (simple variable initialization)
x = tf.Variable(10, name = "x")
init = tf.global_variables_initializer()
with tf.Session() as sess:
  init.run()
  res = x.eval()
  print 'res1: ', res

# tf (evaluate a function of 2 variables)
x = tf.Variable(3, "x")
y = tf.Variable(5, "y")
f = x+y
init = tf.global_variables_initializer()
with tf.Session() as sess:
  init.run()
  res = f.eval()
  print 'res2: ', res

# tf (multiply a matrix with a scalar)
x = tf.Variable(3, name = "x", dtype = tf.float32)
m = tf.constant([[1, 2, 3],[4, 5, 6]], dtype =tf.float32)
f = tf.scalar_mul(x, m)
init = tf.global_variables_initializer()
with tf.Session() as sess:
  init.run()
  res = f.eval()
  print 'res3: ', res
  
