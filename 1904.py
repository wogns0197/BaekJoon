import sys
t = int(input())
ans = []
for i in range(t):
	n = int(input())
	f = 0
	s = 1
	tmp = 0
	if(n==0):
		ans.append("1 0")
	elif(n==1):
		ans.append("0 1")
	elif(n==2):
		ans.append("1 1")
	else:
		for i in range(n - 1):
		    tmp = f
		    f = s
		    s = (tmp + s)
		ans.append(str(f)+" "+str(s))
for i in range(len(ans)):
	print(ans[i])