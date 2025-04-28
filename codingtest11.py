from itertools import combinations

A, B = map(int, input().split())
cards = [i for i in range(1, 11)] * 2
cards.remove(A)
cards.remove(B)

# 끗 결과 집계
cnt = [0] * 10
for a, b in combinations(cards, 2):
    if a == b:
        pass
    else:
        score = (a + b) % 10
        cnt[score] += 1

m = int(18 * 17 / 2)
lose = 0
result = 0

if A == B:
    lose = 10 - A
    result = ((m - lose) / m)
    print("{:.3f}".format(round(result, 3)))
else:
    y = int((A + B) % 10)
    if y == 0:
        result = 0.0
        print("{:.3f}".format(round(result, 3)))
    else:
        for i in range(y):
            lose += cnt[i]
        result = (lose / m)
        print("{:.3f}".format(round(result, 3)))