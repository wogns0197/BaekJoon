n,m = int(input()),int(input())
base = [[100001 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    base[start][end] = min(cost, base[start][end])

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                base[i][j] = 0 
            else:
                base[i][j] = min(base[i][j],
                                     base[i][k] + base[k][j])
for row in base[1:]:
    for col in row[1:]:
        if col == 100001:
            print(0, end = " ")
        else:
            print(col, end = " ")
    print()