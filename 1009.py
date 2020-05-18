cal = [1,4,4,2,1,1,4,4,2]
pica = [ [1],[2,4,5,6],[3,9,7,1],[4,6],[5],[6],[7,9,3,1],[8,4,2,6],[9,1] ]
ans = []
l = int(input())
for i in range(l):
	a , b = input().split(" ")
	a , b = int(a),int(b)
	if(cal[a-1] == 1):
		ans.append(a)
	else:
		if(b%len(pica[a-1])==0):
			ans.append(pica[a-1][len(pica[a-1])-1])
		else:
			ans.append( pica[a-1][ (b % len(pica[a-1])) -1])
for i in range(l):
	print(ans[i])