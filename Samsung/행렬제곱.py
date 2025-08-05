# 지수 법칙 분할 정복
# A^B
# 짝수 ex) A^8 -> A^4 * A^4 (A^4 한번만 구하면 됨)
# 홀수 ex) A^9 -> A^4 * A^4 * A^1 (A^4를 한번 구한뒤 A를 곱하면 됨)
# 크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오. 수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.


import sys

def mat_mul(A, B, mod=1000):
    n = len(A)
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= mod
    return result


def mat_pow(A, power, mod=1000):
    if power == 1:

        return [[elem % mod for elem in row] for row in A]
    half = mat_pow(A, power // 2, mod)
    half_squared = mat_mul(half, half, mod)
    if power % 2 == 0:
        return half_squared
    else:
        return mat_mul(half_squared, A, mod)


n, b = map(int, input().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = mat_pow(board, b)

print(result)
