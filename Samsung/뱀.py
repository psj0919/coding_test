# 문제: 'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
# 게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.
# 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.
# 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
# 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

# 입력: 첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)
# 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.
# 다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)
# 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데, 정수 X와 문자 C로 이루어져 있으며. 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.




n = int(input())
k = int(input())
hl = 1
h = [[1, 1]]

al = []
for i in range(k):
    x, y =  map(int, input().split())
    al.append([x, y])


l = int(input())
turn = []

for i in range(l):
    x, y = input().split()
    turn.append((int(x), y))


count = 0

turn_idx = 0

directions = [(0,1),(1,0),(0,-1),(-1,0)]
dir = 0

while 1:
    count += 1
    head_x = h[-1][0] + directions[dir][0]
    head_y = h[-1][1] + directions[dir][1]

    if head_x < 1 or head_y < 1 or head_x > n or head_y > n or [head_x, head_y] in h:
        print(count)
        break

    h.append([head_x, head_y])

    # 4. 사과 확인
    if [head_x, head_y] in al:
        al.remove([head_x, head_y])  # 사과 있으면 꼬리 그대로 (길이 증가)
    else:
        h.pop(0)  # 사과 없으면 꼬리 줄이기

    # 5. 방향 전환 확인
    if turn_idx < l and count == turn[turn_idx][0]:
        if turn[turn_idx][1] == 'D':
            dir = (dir + 1) % 4
        else:  # 왼쪽 회전
            dir = (dir - 1) % 4
        turn_idx += 1

