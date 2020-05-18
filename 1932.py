s = int(input())
grd,ans = [],[]
for i in range(s):
	grd.append(input().split(" "))
tmp = []
for i in range(len(grd)):
	for j in range(len(grd[i])):
		if( i == 0 ):
			tmp.append(int(grd[i][j]))
		else:
			if(j==0):
				tmp.append(int(grd[i][j])+int(ans[i-1][j]))
			elif(j==len(grd[i])-1):
				tmp.append(int(grd[i][j])+int(ans[i-1][j-1]))
			else:
				if( int(grd[i][j])+int(ans[i-1][j]) > int(grd[i][j])+int(ans[i-1][j-1])):
					tmp.append(int(grd[i][j])+int(ans[i-1][j]))
				else:
					tmp.append(int(grd[i][j])+int(ans[i-1][j-1]))
	ans.append(tmp)
	tmp = []
print(max(ans[len(grd)-1]))