a,b,v = input().split()
a = int(a)
b = int(b)
v = int(v)
arrive =a-b
count =(v-a)//arrive

if(a>=v):
	print(1)
else:
	if (v-a)%(a-b) == 0 :
		print (count+1)
	else:
		print (count+2)
