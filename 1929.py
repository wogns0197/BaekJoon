# import time
# start = time.time()
# m,n = map(int,input().split(" "))
# l = [True for i in range(n)]
# # print(l)
# l[0],l[1] = False,False
# for i in range(2,len(l)):
# 	for j in range(2,len(l)):
# 		if(i*j < len(l)):
# 			l[i*j] = False
# # for i in range(m,n):
# # 	if(l[i]==True):
# # 		print(i)
# print("time :", time.time() - start) 
m,n = map(int,input().split(" "))
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
for i in primes:
	if(i>=m):
		print(i)