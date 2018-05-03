#!/usr/bin/env python

import tensorflow as tf
import numpy as np
import zipfile
import collections
#import numpy as np

def readData(filename):
  """read data from file and return as a list with each list element a word"""
  with zipfile.ZipFile(filename) as f:
    data = tf.compat.as_str(f.read(f.namelist()[0])).split()
  return data

def buildDataset(words, nwords):
  """ build dataset from a list of words"""
  count = [['UNK', -1]]
  count.extend(collections.Counter(words).most_common(nwords-1))
  dictionary = dict()
  for word, _ in count:
    dictionary[word]=len(dictionary)
  data = list()
  unkCount = 0
  for word in words:
    if word in dictionary:
      index = dictionary[word]
    else:
      index = 0
      unkCount += 1
    data.append(index)
  count[0][1] = unkCount
  reversedDictionary = dict(zip(dictionary.values(), dictionary.keys()))

  # data              - word index aligned with the input list 'word' - i.e., word[0] <--> data[0]
  #                     set to '0' (i.e. unknown) if word is not in 'dictionary'
  # count             - [[word, count], [word, count] ...]   count is for full data set
  # dictionary        - {word --> wordindex}
  # reverseDictionary - {wordindex --> word}
  return data, count, dictionary, reversedDictionary

# NOTE! Not yet done
# ...

def main():
  print 'reading words ...'
  words=readData('text8.zip')
  print 'building dataset ...'
  maxwords = 10
  data, count, dictionary, reverseDictionary = buildDataset(words, maxwords)
  print 'done'

if __name__ == '__main__':
  main()
