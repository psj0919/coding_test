

n, k = map(int, input().split())
data = [0 for _ in range(n)]
for i in range(n):
    data[i] = list(map(int, input().split()))


wei = [item[0] for item in data]
val = [item[1] for item in data]

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if wei[i - 1] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wei[i - 1]] + val[i - 1])

print(dp[n][k])









