
m = int(input())
num = list(map(int, input().split()))

x = m # BNP


max_BNP = 0

for i in range(len(num)):
    for j in range(i, len(num)-1):
        if x > 0:
            if x // num[j] > max_BNP:
                max_BNP += x // num[j]
                x = x - max_BNP * num[j]

y = m # timing
max_tim = 0
count_up = 0
count_down = 0

for i in range(1, len(num)):
    if num[i] > num[i-1]:
        count_up += 1
        count_down = 0
    elif num[i] < num[i-1]:
        count_down += 1
        count_up = 0
    else:
        count_up = 0
        count_down = 0

    if count_down >= 3:
        buy = y // num[i]
        max_tim += buy
        y -= buy * num[i]
    if count_up >= 3 and max_tim > 0:
        y += max_tim * num[i]
        max_tim = 0

a = x + num[-1] * max_BNP
b = y + num[-1] * max_tim
if a > b:
    print("BNP")
elif a < b:
    print("TIMING")
else:
    print("SAMESAME")

