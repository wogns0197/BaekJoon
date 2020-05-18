import queue

testcase = int(input())
ans = []

for x in range(testcase):
	m, n, k = input().split(" ")
	bug = 0
	bachlist = []
	flag = []
	for i in range(int(m)):
		bachlist.append([0]*int(n))
		flag.append([0]*int(n))

	# print(bachlist)
	for i in range(int(k)):
		a,b = input().split(" ")
		bachlist[int(a)][int(b)] = 1
	# print(bachlist)
	dir = [[0,1],[1,0],[-1,0],[0,-1]]
	q = queue.Queue() #put , get
	# print(bachlist)
	# print(bachlist)
	# print(flag)
	for i in range(int(m)):
		for j in range(int(n)):
			try:
				if( bachlist[i][j] == 1 and flag[i][j] == 0):
					q.put([i,j])
					flag[i][j] = 1
					while(q.qsize() != 0):
						pos = q.get()	
						for l in range(4):							
							tx = pos[0] + dir[l][0]
							ty = pos[1] + dir[l][1]
							if( 0<=tx and tx<int(m) and 0<=ty and ty<int(n) ):						
								if(bachlist[tx][ty] == 1 and flag[tx][ty] == 0):
									q.put([tx,ty])
									flag[tx][ty] = 1	
			except IndexError:
				pass			
				bug+=1
				
	ans.append(bug)
for i in range(testcase):
	print(ans[i])
##제출 시 런타임에러뜸
			







