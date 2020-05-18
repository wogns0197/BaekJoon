n,m = map(int,input().split(" "))
# q = queue.Queue() #put ,get
l = [[0 for i in range(n)] for i in range(n)]
ans = []

for i in range(m):
	a,b = map(int,input().split(" "))
	l[a-1][b-1] += 1
	l[b-1][b-1] += 1
while(True):
	if(len(ans)==n): break
	for i in range(len(l)):
		if(l[i][i] == 0 and not(i+1 in ans)):
			ans.append(i+1)
			for j in range(len(l[i])):
				if(l[i][j] == 1):
					l[j][j] -= 1
	# print(l)
	# time.sleep(0.3)
for i in ans:
	print(i,end=" ")
print()

#답은 맞는데 메모리제한이 뜸.