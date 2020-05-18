import time
def main():
	n,m,v = input().split(" ")
	ans = ""
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
	chk=[0 for i in range(n)]
	
	while( 0 in chk ):
		print(v)
		for i in range(4):
			if ( chk[i] == 0 and bmap[v][i]==1):
				chk[i]
				v = i
		time.sleep(0.4)
main()