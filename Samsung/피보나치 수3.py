# 피사노 주기 -> 피보나치 수열을 특정 수로 나눈 나머지는 주기적으로 반복됨.
# N%P번째 피보나치 수를 M으로 나눈 나머지와 같다.
# M = 10^K(k>2)일 때, 항상 15*10^(k-1)이다.



MOD = 1000000
PISANO = 1500000

n = int(input())
n %= PISANO


a, b = 0, 1
for _ in range(n):
    a, b = b, (a + b) % MOD

print(a)
