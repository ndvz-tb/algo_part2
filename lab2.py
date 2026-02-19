n, w, h = map(int, input().split())

def can_fit(side):
    return (side // w) * (side // h) >= n

left = 0
right = 1

while not can_fit(right):
    right *= 2

while left + 1 < right:
    mid = (left + right) // 2
    if can_fit(mid):
        right = mid
    else:
        left = mid

print(right)