# 문제
# 스타트링크에서 판매하는 어린이용 장난감 중에서 가장 인기가 많은 제품은 구슬 탈출이다. 구슬 탈출은 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임이다.
# 보드의 세로 크기는 N, 가로 크기는 M이고, 편의상 1×1크기의 칸으로 나누어져 있다. 가장 바깥 행과 열은 모두 막혀져 있고, 보드에는 구멍이 하나 있다. 빨간 구슬과 파란 구슬의 크기는 보드에서 1×1크기의 칸을 가득 채우는 사이즈이고, 각각 하나씩 들어가 있다. 게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다. 이때, 파란 구슬이 구멍에 들어가면 안 된다.
# 이때, 구슬을 손으로 건드릴 수는 없고, 중력을 이용해서 이리 저리 굴려야 한다. 왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능하다.
# 각각의 동작에서 공은 동시에 움직인다. 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다. 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다. 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다. 또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다. 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.
# 보드의 상태가 주어졌을 때, 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램을 작성하시오.

# 조건
#첫 번째 줄에는 보드의 세로, 가로 크기를 의미하는 두 정수 N, M (3 ≤ N, M ≤ 10)이 주어진다. 다음 N개의 줄에 보드의 모양을 나타내는 길이 M의 문자열이 주어진다. 이 문자열은 '.', '#', 'O', 'R', 'B' 로 이루어져 있다. '.'은 빈 칸을 의미하고, '#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며, 'O'는 구멍의 위치를 의미한다. 'R'은 빨간 구슬의 위치, 'B'는 파란 구슬의 위치이다.
#입력되는 모든 보드의 가장자리에는 모두 '#'이 있다. 구멍의 개수는 한 개 이며, 빨간 구슬과 파란 구슬은 항상 1개가 주어진다.


# 사용 알고리즘 BFS

from collections import deque
import sys



n, m = map(int, input().split())
board = [list(input().rstrip())for _ in range(n)]
visited = []

# dx, dy 방향 벡터 상하좌우 방향으로 구슬을 이동시키기 위해 사용되는 값.
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0

# 각각의 공의 위치를 확인하기 위해 사용되는 함수
# 빨간 구슬과 파란 구슬의 초기위치를 찾을 수 있음.
def getPos():
    rx, ry, bx, by = 0, 0, 0, 0
    for x in range(n):
        for y in range(m):
            if board[x][y] == "R":
                rx, ry = x, y
            if board[x][y] == "B":
                bx, by = x, y

    return rx, ry, bx, by

# 구슬이 해당 방향으로 굴러가서 멈출 때 까지 이동
# #에 닿으면 멈춤, 구멍(O)에 빠지면 그 자리에 멈춤
# 최종 위치(x, y)와 이동 횟수 cnt return
def move(x, y, dx, dy):
    cnt = 0
    # 이동하는 위치가 벽이 아닌, 구멍에 들어가지 않을 동안 반복
    while board[x+ dx][y+ dy] != "#" and board[x][y] != "O":
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

# bfs
# 전체 탐색 로직의 핵심
# 너비 우선 탐색(BFS)을 사용하여 4방향에 대해 모든 경우를 탐색
def bfs():
    rx, ry, bx, by = getPos()

    q = deque()
    q.append((rx, ry, bx, by, 1))
    visited.append((rx,ry,bx,by))

    while q:
        rx, ry, bx, by, result = q.popleft()

        if result > 10:
            break

        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])

            # 파란 구슬이 구멍에 들어갈 경우
            if board[nbx][nby] == "O":
                continue

            # 빨간 구슬이 들어갈 경우 성공
            if board[nrx][nry] == "O":
                print(result)
                return

            # 둘이 겹쳐있을경우 더 많이 이동한녀석을 1칸 뒤로 보낸다.
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            # 탐색하지 않은 방향 탐색
            if (nrx, nry, nbx, nby) not in visited:
                visited.append((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, result + 1))
    print(-1)


bfs()

# 알고리즘 요약
# 1. 초기상태: R, B 위치 찾기
# 2. BFS 큐에 상태를 넣고 시작
# 3. 4방향으로 구슬을 굴려봄 (move 함수 사용)
# 4. 파란 구슬이 구멍에 빠졌으면 무시
# 5. 빨간 구슬이 구멍에 빠졌으면 성공
# 6. 두 구슬이 겹치면 이동 거리가 더 큰 쪽으로 뒤로 이동.
# 7. 새로운 상태가 반문한 적 없으면 큐에 넣음
# 8. 10번 이내에 못 빠지면 실패


# BFS (Breadth-First search, 너비 우선 탐색)

# BFS는 그래프/맵에서 시작 노드로부터 가까운 노드부터 차례대로 탐색하는 알고리즘, 주로 최단 거리를 찾을 때 많이 사용됨.
# 큐(Queue)를 사용해 인접 노드를 먼저 탐색.
