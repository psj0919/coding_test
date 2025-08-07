def largest_rectangle(hist):
    stack = []
    max_area = 0
    i = 0
    n = len(hist)

    while i < n:
        if not stack or hist[stack[-1]] <= hist[i]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, hist[top] * width)

    while stack:
        top = stack.pop()
        width = i if not stack else i - stack[-1] - 1
        max_area = max(max_area, hist[top] * width)

    return max_area


while True:
    arr = list(map(int, input().split()))
    n = arr[0]
    if n == 0:
        break
    heights = arr[1:]
    print(largest_rectangle(heights))