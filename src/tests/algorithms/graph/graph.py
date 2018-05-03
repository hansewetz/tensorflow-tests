#!/usr/bin/env python
import sys

def printbfs(g, nstart):
  """ print graph in bfs order """
  n=len(g)
  color=[0]*n    # 0-->white, 1-->grey, 2-->black
  q=[nstart]
  qtmp=[]
  color[nstart]=1
  parents=[-1]*n
  while len(q)>0:
    u=q.pop(0)
    sys.stdout.write(str(u)+' ')
    adj=g[u]
    for v in adj:
      if color[v]!=0: continue
      parents[v]=u
      qtmp.append(v)
      color[v]=1
    if len(q)==0:
      q,qtmp=qtmp,q
      sys.stdout.write('\n')
    color[u]=2
  return parents

def printpath(u, parents):
  """ print path to 'u """
  if u ==-1: return
  printpath(parents[u], parents)
  print '{}'.format(u)

def printgraph(g):
  n=len(g)
  for u in xrange(n):
    print '{}: {}'.format(u, g[u])
    

def bfs(g,nstart):
  """ bfs traversal as a generator """
  n=len(g)
  color=[0]*n
  q=[nstart]
  color[nstart]=1
  while len(q)!=0:
    u=q.pop(0)
    yield u
    adj=g[u]
    for v in adj:
      if color[v]!=0: continue
      q.append(v)
      color[v]=1
    color[u]=2

def dfs(g, nstart, color, ts):
  color[nstart]=1
  for v in g[nstart]:
    if color[v]!=0: continue
    dfs(g, v, color, ts)
  color[nstart]=2
  ts.append(nstart)

def topsort(g):
  ret=[]
  n=len(g)
  color=[0]*n    # all white
  for i in xrange(n):
    if color[i] == 0:
      dfs(g,i,color, ret)
  return ret[::-1]

def findcutaux(g, ustart, color, vnum, currnum, parent):
  """ find an edge that if cut will cut the graph into two disjoint graphs """
  """ (vnum-->min num array indexed by vertex, currnum-->last number) """
  color[ustart] = 1
  vnum[ustart] = currnum
  lownum = currnum
  currnum += 1
  for  v in g[ustart]:
    if v == parent: continue
    if color[v] == 0:   # new vertex found (grey --> white)
      newnum = findcutaux(g, v, color, vnum, currnum, v)
      if newnum > vnum[ustart]:
        print 'bridge from: {} to {}'.format(ustart, v)
      lownum = min(lownum, newnum)
    else:               # grey --> grey
      lownum = min(lownum, vnum[ustart])
    
  color[ustart] = 2
  return lownum

def findcut(g):
  n = len(g)
  color = [0]*n
  vnum = [-sys.maxint]*n
  currnum = 0
  for u in xrange(n):
    if color[u] == 0:
      findcutaux(g, u, color, vnum, currnum, -1)

def main():
  g=[[2, 1],
     [3],
     [4],
     [5],
     [3, 5, 6],
     [],
     []]
  findcut(g)

# run main
main()
