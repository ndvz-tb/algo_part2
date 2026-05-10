import math

def calculate_max_wire(w, heights):
    n = len(heights)
    if n <= 1:
        return 0.0
    
    dp_1 = 0.0
    dp_h = 0.0

    for i in range(1, n):
        h_prev = heights[i-1]
        h_curr = heights[i]

        dist_1_1 = math.sqrt(w**2 + 0)
        dist_h_1 = math.sqrt(w**2 + (h_prev - 1)**2)
        next_dp_1 = max(dp_1 + dist_1_1, dp_h + dist_h_1)

        dist_1_h = math.sqrt(w**2 + (h_curr - 1)**2)
        dist_h_h = math.sqrt(w**2 + (h_curr - h_prev)**2)
        next_dp_h = max(dp_1 + dist_1_h, dp_h + dist_h_h)

        dp_1, dp_h = next_dp_1, next_dp_h

    return round(max(dp_1, dp_h), 2)

if __name__ == "__main__":
    w = int(input())
    heights = list(map(int, input().split()))
    result = calculate_max_wire(w, heights)
    print(f"{result:.2f}")