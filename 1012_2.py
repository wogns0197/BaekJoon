import queue
l = int(input())
ans = []
for alal in range(l):
	count =0
	m,n,k = map(int,input().split(" "))
	pos = [[0,1],[0,-1],[-1,0],[1,0]]
	base = [[0 for i in range(m)] for i in range(n)]
	nxt = [[0 for i in range(m)] for i in range(n)]
	for j in range(k):
		bx,by = map(int,input().split(" "))
		base[by][bx] = 1
	q = queue.Queue()
	for i in range(n):
		for j in range(m):
			if (base[i][j] == 1 and nxt[i][j] != 1 ):				
				q.put([i,j])
				nxt[i][j] = 1
				while(q.qsize() >0):
					tmp = q.get()					
					qx = tmp[0]
					qy = tmp[1]
					for k in pos:
						tx = qx + k[0]
						ty = qy + k[1]
						if( 0<=tx and tx<n and 0<=ty and ty<m):
							if( base[tx][ty] == 1 and nxt[tx][ty] != 1 ):
								q.put([tx,ty])
								nxt[tx][ty] = 1
				count+=1
	ans.append(int(count))
for i in ans:
	print(i)