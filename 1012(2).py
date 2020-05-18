import queue
import sys

l = int(input())
pos ,ans= [[0,1],[0,-1],[-1,0],[1,0]],[]
q = queue.Queue()
for _ in range(l):
  m,n,k = input().split()
  m,n,k = int(m), int(n), int(k)
  base = [[0 for xx in range(m+1)] for yy in range(n+1)]
  nxt = [[0 for xx in range(m+1)] for yy in range(n+1)]
  for _ in range(k):
    bx,by = input().split()
    bx,by = int(bx), int(by)
    base[by][bx] = 1
  for ii in range(n):
    for jj in range(m):
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
            if( 0<=tx and tx<n and 0<=ty and ty<m):
              if( base[tx][ty] == 1 and nxt[tx][ty] != 1 ):
                q.put([tx,ty])
                nxt[tx][ty] = 1
                doncnt+=1
        ans.append(doncnt)
  print(ans)