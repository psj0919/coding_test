
num = int(input())
ball = {1:1, 2:0, 3:0}

for i in range(num):
    x, y = map(int, input().split())
    ball[x], ball[y] = ball[y], ball[x]

for i in range(1, 4):
    if ball[i] == 1:
        print(i)