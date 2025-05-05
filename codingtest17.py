

z = int(input())
x = []
y= []
for _ in range(z):
    t, p = map(int, input().split())
    x.append(t)
    y.append(p)


dp = [0 for i in range(z+1)]

for i in range(z):
    for j in range(i+x[i], z+1):
        if dp[j] < dp[i] + y[i]:
            dp[j] = dp[i] + y[i]

print(dp[-1])
