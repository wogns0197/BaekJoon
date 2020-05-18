import queue
from sys import *

setrecursionlimit(10 ** 6)
def main():
	ans,comp = [],[]
	flag = 0
	n = int(input())
	ground = [[0 for i in range(n)]for i in range(n)]
	for i in range(n):
		t = input().split(" ")
		for j in range(n):
			ground[i][j] = int(t[j])
			if(not int(t[j]) in comp):
				comp.append(int(t[j]))
	if(len(comp)==1):
		print(1)
		return 1
	for i in comp:
		ans.append(bfs(n,minus(n,ground,i)))
	print(max(ans))

def minus(n,ground,num):
	base = [[1 for i in range(n)]for i in range(n)]
	for i in range(n):
		for j in range(n):
			if(ground[i][j] <= num):
				base[i][j] = 0
	return base

def bfs(n,base):
	count = 0
	nxt = [[0 for i in range(n)]for i in range(n)]
	q = queue.Queue()
	pos = [[-1,0],[1,0],[0,-1],[0,1]]
	for i in range(n):
		for j in range(n):
			if(base[i][j] == 1 and nxt[i][j]!=1):
				q.put([i,j])
				nxt[i][j] = 1
				while(q.qsize() >0):
						tmp = q.get()					
						qx = tmp[0]
						qy = tmp[1]
						for k in pos:
							tx = qx + k[0]
							ty = qy + k[1]
							if( 0<=tx and tx<n and 0<=ty and ty<n):
								if( base[tx][ty] == 1 and nxt[tx][ty] != 1 ):
									q.put([tx,ty])
									nxt[tx][ty] = 1
				count+=1
	return count
main()

#dk...이거 맞는데...시간초과....
