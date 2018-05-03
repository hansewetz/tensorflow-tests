#!/usr/bin/env python
import sys

class Node:
  """ tree node """
  def __init__(self, val, left, right):
    self._val = val
    self._left = left
    self._right = right

  def getVal(self):
    return self._val

  def getLeft(self):
    return self. _left

  def getRight(self):
    return self._right

  def setLeft(self, left):
    self._left = left

  def setRight(self, right):
    self._right = right

def treeDepth(node):
  if node == None: return 0
  return 1 + treeDepth(node.getLeft()) + treeDepth(node.getRight())

def printBfs(node):
  q = [node]
  q1 = []
  while len(q) != 0:
    n = q.pop(0)
    print n.getVal(),
    if n.getLeft() is not None:
      q1.append(n.getLeft())
    if n.getRight() is not None:
      q1.append(n.getRight())
    if len(q) == 0:
      print '\n',
      q, q1 = q1, q   # swap queues

def list2TreeBfs(l):
  n = len(l)
  if n == 0: return None
  ret = Node(l[0], None, None)
  q = [ret]
  ind = 1
  while len(q) != 0:
    node = q.pop(0)
    if ind == n: continue
    lnode = Node(l[ind], None, None)
    node.setLeft(lnode)
    q.append(lnode)
    ind += 1
    if ind >= n: continue
    rnode = Node(l[ind], None, None)
    node.setRight(rnode)
    q.append(rnode)
    ind += 1
  return ret

def main():
  l = [0,1,2,3,4,5,6,7]
  t = list2TreeBfs(l)
  printBfs(t)

# run main
main()
