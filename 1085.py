x,y,w,h = input().split(" ")
x,y,w,h = int(x),int(y),int(w),int(h)
if(w/2 < x):
	if(h/2 < y):
		print(min(h-y,w-x))
	else:
		print(min(y,w-x))
else:
	if(h/2 < y):
		print(min(x,h-y))
	else:
		print(min(x,y))
# 17년에는 못풀었지만 20년엔 풀었다