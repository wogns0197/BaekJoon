import time

def main():
	ground = []
	nextgnd = []
	for i in range(10):
		ground.append([0]*10)
		nextgnd.append([0]*10)
	
	#testcase
	ground[3][4] = 1
	ground[4][3] = 1
	ground[4][4] = 1
	ground[4][5] = 1
	ground[5][4] = 1

	# step = 0
	pos = [[-1,1],[0,1],[1,1], [-1,0],[1,0],[-1,-1],[0,-1],[1,-1]]
	while(True):
		# step+=1
		for i in range(10):
			for j in range(10):
				live =0
				for k in range(8):
					tx = i + pos[k][0]
					ty = j + pos[k][1]
					# print("tx = ",tx," ty = ",ty)
					if( 0<=tx and tx<10 and 0<=ty and ty<10 ):
						if( ground[tx][ty] == 1 ):
							live+=1
				if(live == 3):
					# print("step",step," in ",i," ",j, " live = ",live)
					nextgnd[i][j] = 1
					live = 0
				if(live == 2 and ground[i][j] == 1):
					# print("step",step," in ",i," ",j, " live = ",live)
					nextgnd[i][j] = 1
					live = 0
							
		prt(ground)
		ground = nextgnd
		nextgnd = []
		for i in range(10):
			nextgnd.append([0]*10)
		time.sleep(0.4)

def prt(list1):
	print("\n\n")
	for i in range(10):
		for j in range(10):
			if( list1[i][j] == 1):
				list1[i][j] = "⬜️"
			else :
				list1[i][j] = "⬛️"
	for i in range(10):
		for j in range(10):
			print(list1[i][j],end = ' ')
		print("")

main()

##너비우선탐색 알고리즘으로 성공!


