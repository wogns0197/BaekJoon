h,m=map(int,input().split(" "))
if(m < 45):
	h -=1
	if(h<0):
		h+=24
	m+=15
	print(h,m)

else:
	print(h,m-45)