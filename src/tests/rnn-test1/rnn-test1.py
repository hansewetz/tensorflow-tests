#!/usr/bin/env python
import tensorflow as tf
import numpy as np

# parameters
n_steps = 2                # timestpes to go
n_inputs = 3               # inputs to each neuron
n_neurons = 5              # neurons in cell

# setup data
X_batch = np.array([
  [[0,1,2],[9,8,7]],   # sample: 0
  [[3,4,5],[0,0,0]],   # sampel: 1
  [[6,7,8],[6,5,4]],   # sample: 2
  [[9,0,1],[3,2,1]]    # sample: 3
])
seq_len_batch = np.array([2,1,2,2])

# build graph
X = tf.placeholder(tf.float32, [None, n_steps, n_inputs])
seq_length = tf.placeholder(tf.int32, [None])
basic_cell = tf.contrib.rnn.BasicRNNCell(num_units=n_neurons)
outputs, states = tf.nn.dynamic_rnn(basic_cell, X, dtype=tf.float32, sequence_length=seq_length)

# run it
init = tf.global_variables_initializer()
with tf.Session() as sess:
  init.run()
  outputs_val, states_val = sess.run([outputs, states], feed_dict={X: X_batch, seq_length: seq_len_batch})
  print outputs_val
  #print states_val
