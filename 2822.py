# [int(input()) for i in range(8)]
list1 = [20,30,50,48,33,66,0,64]
tmp=list1[:]
ans=""
tmp.sort(reverse=True)
print("list1 = " , list1)
for i in tmp[0:5]:
	print("tmp = ", tmp)
	ans = ans + str(list1.index(i)) + " "
print(str(sum(list1[0:5]))+"\n"+ans)


