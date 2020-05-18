l = int(input())
a = input().split(" ")
base,dp= [],[]
for i in range(l):
	base.append(int(a[i]))
for i in range(l):
	if i == 0 :
		dp.append(1)
	else:
		if( base[i] > base[i-1] ):
			if( max(base[:i])>base[i] )
				
			else:
				dp.append(max(dp)+1)
		else:
			if(base[i] in base[:i]):
				dp.append(dp[base[:i].index(base[i])])
			else:
				dp.append(1)
print(max(dp))
