
def sum(num):
    result = 0
    while num != 0:
        result += int(num % 10)
        num = int(num / 10)

    return result

N = int(input())
orig = N
value = 0
for i in range(1, N+1):
    value = sum(i)
    result = i + value
    if result == N:
        print(i)
        break
    if i == N:
        print(0)
        break


