# 문제
#폴리오미노란 크기가 1×1인 정사각형을 여러 개 이어서 붙인 도형이며, 다음과 같은 조건을 만족해야 한다.

# 정사각형은 서로 겹치면 안 된다.
# 도형은 모두 연결되어 있어야 한다.
# 정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.
# 정사각형 4개를 이어 붙인 폴리오미노는 테트로미노라고 하며, 다음과 같은 5가지가 있다.

import sys

n, m = map(int, input().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

maxm = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, tmp, cnt):
    global maxm

    if cnt == 4:
        maxm = max(maxm, tmp)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[ny][nx]:
            continue

        visited[ny][nx] = True
        dfs(nx, ny, tmp+board[ny][nx], cnt+1)
        visited[ny][nx] = False


def at_shape(x, y):
    global maxm
    arr = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=m or ny<0 or ny>=n:
            continue
        arr.append(board[ny][nx])
    length = len(arr)
    if length == 4:
        arr.sort(reverse=True)
        arr.pop()
        maxm = max(maxm, sum(arr) + board[y][x])
    elif length == 3:
        maxm = max(maxm, sum(arr) + board[y][x])
    return

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(j, i, board[i][j], 1)
        at_shape(j, i)
        visited[i][j] = False

print(maxm)

