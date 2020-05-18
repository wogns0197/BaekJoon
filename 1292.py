l = []
k=0
for i in range(1000):
	for j in range(i):
		l.append(k)
	k+=1
a,b = map(int,input().split(" "))
print(sum(l[a-1:b]))