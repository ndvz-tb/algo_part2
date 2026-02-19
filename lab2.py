def can_fit(side, w, h, n):
    return (side // w) * (side // h) >= n

def main():
    n, w, h = map(int, input().split())

    left = 0
    right = 1

    while not can_fit(right, w, h, n):
        right *= 2

    while left + 1 < right:
        mid = (left + right) // 2
        if can_fit(mid, w, h, n):
            right = mid
        else:
            left = mid

    print(right)

main()