import sys

def get_min_beers(n, b, likes_str):
    adj_list = {i: [] for i in range(n)}
    
    for i in range(n):
        for j in range(b):
            if likes_str[i * b + j] == 'Y':
                adj_list[i].append(j)

    min_beers_count = b + 1

    def dfs(employee_idx, current_beers_set):
        nonlocal min_beers_count

        if len(current_beers_set) >= min_beers_count:
            return

        if employee_idx == n:
            min_beers_count = len(current_beers_set)
            return

        is_covered = False
        for beer in adj_list[employee_idx]:
            if beer in current_beers_set:
                is_covered = True
                break

        if is_covered:
            dfs(employee_idx + 1, current_beers_set)
        else:
            for beer in adj_list[employee_idx]:
                current_beers_set.add(beer)
                dfs(employee_idx + 1, current_beers_set)
                current_beers_set.remove(beer)

    dfs(0, set())
    return min_beers_count 

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    b = int(input_data[1])
    likes_str = "".join(input_data[2:])

    print(get_min_beers(n, b, likes_str))

if __name__ == '__main__':
    solve()