from collections import Counter
base = [int(input()) for i in range(10)]
print(int(sum(base)/10))
print(Counter(base).most_common()[0][0])