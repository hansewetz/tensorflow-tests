#!/usr/bin/env python
import tensorflow as tf
import numpy as np

# numpy
m=2
n=3
x = np.array([1,2])
m = np.array([[0.1, 0.2, 0.3],[0.1, 0.2, 0.3]])
res = np.dot(x, m)
#print res

# tf (standard matrix multiplication)
m = tf.constant([[1, 2],[3, 4]], dtype = tf.float32)
n = tf.constant([[1, 2, 3], [4, 5, 6]], dtype = tf.float32)
with tf.Session() as sess:
  res = tf.einsum('ik,kj->ij', m, n).eval()
  print 'test1: ', res

# tf (vector inner product)
x = tf.constant([1,2,3], dtype=tf.float32)
y = tf.constant([0.1, 0.2, 0.3], dtype = tf.float32);
with tf.Session() as sess:
  res = tf.einsum('i,i->',x, y).eval()
  print 'test2: ', res

# tf (outer product)
x = tf.constant([1, 2], dtype = tf.float32)
y = tf.constant([0.1, 0.2, 0.3], dtype = tf.float32)
with tf.Session() as sess:
  res = tf.einsum('i,j->ij',x, y).eval()
  print 'test3: ', res

# tf (transpose)
m = tf.constant([[1, 2, 3], [4, 5, 6]], dtype = tf.float32)
with tf.Session() as sess:
  res = tf.einsum('ij->ji', m).eval()
  print 'test4: ', res

# tf (multiply each row in matrix with the corresponding element in a vector)
m1 = tf.constant([[0.1,0.2,0.3], [0.1,0.2,0.3]], dtype = tf.float32);
m2 = tf.constant([2,3], dtype = tf.float32);
with tf.Session() as sess:
  res = tf.einsum('ij,i->ij',m1,m2).eval()
  print res

# tf (mutiply a matrix with a vector
m1 = tf.constant([[1, 2, 3], [4, 5, 6]], dtype = tf.float32)
v = tf.constant([1,2,3], dtype=tf.float32)
with tf.Session() as sess:
  res = tf.einsum('ik,k->i',m, v).eval()
  print 'test6: ', res

