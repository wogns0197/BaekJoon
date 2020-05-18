import queue
import sys

l = int(input())
pos ,ans= [[0,1],[0,-1],[-1,0],[1,0]],[]
q = queue.Queue()
base = [[0 for xx in range(l)] for yy in range(l)]
nxt = [[0 for xx in range(l)] for yy in range(l)]

for i in range(l):
  apart = str(input())
  for j in range(l):
    base[i][j] = int(apart[j])

for ii in range(l):
  for jj in range(l):
    if (base[ii][jj] == 1 and nxt[ii][jj] != 1 ):   
      doncnt = 1     
      q.put([ii,jj])
      nxt[ii][jj] = 1
      while(q.qsize() > 0):
        tmp = q.get()
        qx = tmp[0]
        qy = tmp[1]
        for kk in pos:
          tx = qx + kk[0]
          ty = qy + kk[1]
          if( 0<=tx and tx<l and 0<=ty and ty<l):
            if( base[tx][ty] == 1 and nxt[tx][ty] != 1 ):
              q.put([tx,ty])
              nxt[tx][ty] = 1
              doncnt+=1
      ans.append(doncnt)
ans.sort()
print(len(ans))
for i in range(len(ans)):
  print(ans[i])

