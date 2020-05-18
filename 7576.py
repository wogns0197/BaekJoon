import time
def main():
	m,n = input().split(" ")
	m = int(m)
	n = int(n) 
	base,nxt ,ans,zcount,ocount, pos= [],[],0,0,0,[ [1,0],[0,-1],[-1,0],[0,1] ]
	for i in range(n):
		base.append(input().split(" "))
		nxt.append([0]*m)
	tmp = base
	chk = 1
	while (True):
		
		zcount,ocount = 0,0
		for i in range(n):
			for j in range(m):
				if (tmp[i][j] == '1'):
					nxt[i][j] = 1
					for k in pos:
						x = i + k[0]
						y = j + k[1]
						if( (0<=x and x<n and 0<=y and y<m)):							
							if( base[x][y] == "0" and nxt[x][y] != 1):								
								print(base)
								base[x][y] = "1"
								nxt[x][y] = 1


		ans+=1

		tmp = base
		for i in base:
			if( "0" in i):
				zcount+=1
			else:
				ocount+=1
		if( zcount == 0):
			print(ans)
			break;

main()

## 못품
	