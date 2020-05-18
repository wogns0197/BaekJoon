ans = str(int(input())*int(input())*int(input()))
list1 = [0 for i in range(10)]
for i in ans:
	list1[int(i)] += 1
for i in range(10):
	print(list1[i])