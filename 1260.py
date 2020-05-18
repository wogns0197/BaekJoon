import queue,time
def main():
	global ans2,chk2,bmap,n,m,chknum
	n,m,v = input().split(" ")
	n = int(n)
	m = int(m)
	v = int(v)
	bmap = [[0 for col in range(n)] for row in range(n)]

	for i in range(m):
		x , y = input().split(" ")
		x = int(x)
		y = int(y)
		bmap[x-1][y-1] = 1
		bmap[y-1][x-1] = 1
	# print(bmap)
	chk2 = [0 for col in range(n)]
	chknum = 0
	chk2[v-1] = 1
	ans2 = [v]
	dfs(v-1)
	for i in ans2:
		print(i,end=' ')
	print("")
	print(bfs(v))

def dfs(v):
	for i in range(n):
		if (bmap[v][i] == 1 and chk2[i] != 1):
			ans2.append(i+1)
			chk2[i] = 1
			dfs(i)
def bfs(v):
	q = queue.Queue()
	ans = str(v)
	chk = [0 for col in range(n)]
	chk[v-1] = 1
	q.put(v)
	if(m<=n):
		while(0 in chk):
			tmp = q.get()
			for i in range(n):
				if(i == tmp-1):
					for j in range(n):
						if(bmap[i][j] == 1 and chk[j] != 1):
							q.put(j+1)
							chk[j] = 1
							ans += (" "+str(j+1))
	else:
		while(chknum == n+1):
			tmp = q.get()
			for i in range(n):
				if(i == tmp-1):
					for j in range(n):
						if(bmap[i][j] == 1 and chk[j] != 1):
							q.put(j+1)
							chk[j] = 1
							chknum+=1
							ans += (" "+str(j+1))
	return ans


main()


