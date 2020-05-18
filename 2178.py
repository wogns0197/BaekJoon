n,m = input().split(" ")
n = int(n)
m = int(m)
grd,jp8,path,tmp= [],[],[[0,0]],[]
for i in range(int(n)):
	a = input()
	for j in range(int(m)):
		jp8.append(int(a[j]))
	grd.append(jp8)
	jp8 = []

pos = [[0,1],[0,-1],[-1,0],[1,0]]
flag=0
count = 0
while(flag==0):	
	for i in path:		
		for j in pos:
			grd[i[0]][i[1]] = 0
			tx = i[0] + j[0]
			ty = i[1] + j[1]
			if([n-1,m-1] in path):
				flag+=1
			else:
				if( 0<=tx and tx<n and 0<=ty and ty <m):					
					if(grd[tx][ty] == 1 ):	
						tmp.append([tx,ty])					
	count+=1
	path = tmp
	for i in path:
		while ( i in path):
			path.remove(i)
		path.append(i)			
	tmp = []
print(count)
						
## 풀었다~!

	





