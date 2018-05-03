#!/usr/bin/env python

def part(v, l, u):
  """ partition a list """
  m=l
  for i in xrange(l+1,u+1):
    if v[i]<v[l]:
      m+=1
      v[i],v[m] = v[m],v[i]
  v[m],v[l] = v[l],v[m]
  return m

def kthsmall(v, k):
  """ get kth smallest value from a list with 'k' starting from 1"""
  n=len(v)
  k-=1
  if k<0 or k >= n:
    return -1
  l=0
  u=n-1
  while True:
    m=part(v,l,u)
    if m==k: return v[m]
    if m<k: l = m+1
    else: u=m-1

def longincseq(v):
  """ find length of longest increasing sequence"""
  n=len(v)
  if n==0: return -1
  l = 0
  u = n-1
  max2here=1
  maxsofar=1
  for i in xrange(l+1, u+1):
    if v[i]>v[i-1]: 
      max2here+=1
    else:
      max2here=1
    maxsofar = max(maxsofar, max2here)
  return maxsofar

def lowbound(v, val):
  """ find lowest index for an integer in a sorted sequence"""
  n=len(v)
  if n==0: return -1
  l=0
  u=n-1
  ret=-1
  while l<=u:
    m = (l+u)/2
    if v[m]==val:
      ret=m
      u=m-1
    elif v[m]<val:
      l=m+1
    else:
      u=m-1
  return ret

def maxsubarray(v):
  """ find maximum subarray (complexity: linear) """
  n=len(v)
  if n==0: return -1
  max2here=v[0]
  maxsofar=v[0]
  for i in xrange(0,n):
    max2here=v[i] if max2here+v[i]<v[i] else max2here+v[i]
    maxsofar=max(maxsofar, max2here)
  return maxsofar

def main():
  v = [-1,3,4,-8,5,-1,4]

# run main
main()
