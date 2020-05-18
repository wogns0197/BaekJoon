ans = [-1 for i in range(26)]
st = str(input())
for i in range(len(st)):
	for j in range(26):
		if(ord(st[i])-97 == j):
			if(ans[j] == -1):
				ans[j] = i
for i in ans:
	print(i,end=" ")