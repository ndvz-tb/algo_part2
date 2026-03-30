import collections
import sys

def solve_knight_problem():
    input_file = "input.txt"
    output_file = "output.txt"

    try:
        with open(input_file, "r") as f:
            lines = [line.strip().split('#')[0].strip() for line in f if line.strip()]

        if len(lines) < 3:
            raise ValueError(f"Недостатньо даних у файлі {input_file}")

        # Читаємо N (розмір поля)
        n = int(lines[0])

        def parse_coords(s):
            if ',' in s:
                return tuple(int(x.strip()) for x in s.split(','))
            else:
                return tuple(int(x) for x in s.split())

        start_coords = parse_coords(lines[1])
        target_coords = parse_coords(lines[2])

        def is_inside(coords, n):
            x, y = coords
            return 0 <= x < n and 0 <= y < n

        if not is_inside(start_coords, n) or not is_inside(target_coords, n):
            raise ValueError("Стартові або кінцеві координати за межами поля.")

        print(f"Поле: {n}x{n}")
        print(f"Старт: {start_coords}")
        print(f"Ціль: {target_coords}")

    except FileNotFoundError:
        print(f"Помилка: Файл '{input_file}' не знайдено.")
        return
    except (ValueError, IndexError) as e:
        print(f"Помилка при зчитуванні вхідних даних: {e}")
        return
    except Exception as e:
        print(f"Непередбачувана помилка: {e}")
        return

    if start_coords == target_coords:
        with open(output_file, "w") as f:
            f.write("0")
        print("Результат: 0 (старт і ціль збігаються)")
        return

    knight_moves = [
        (2, -1), (2, 1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    queue = collections.deque([(start_coords[0], start_coords[1], 0)])

    visited = set()
    visited.add(start_coords)

    found_path = False
    final_moves_count = -1

    while queue:
        curr_x, curr_y, current_dist = queue.popleft()

        for dx, dy in knight_moves:
            next_x = curr_x + dx
            next_y = curr_y + dy

            if 0 <= next_x < n and 0 <= next_y < n and (next_x, next_y) not in visited:
                
                if (next_x, next_y) == target_coords:
                    final_moves_count = current_dist + 1
                    found_path = True
                    break 

                visited.add((next_x, next_y))
                queue.append((next_x, next_y, current_dist + 1))
        
        if found_path:
            break 

    with open(output_file, "w") as f:
        f.write(str(final_moves_count))

    if found_path:
        print(f"Розрахунок завершено. Найкоротший шлях: {final_moves_count}")
    else:
        print("Розрахунок завершено. Шлях неможливий.")
    print(f"Результат записано у файл '{output_file}'")

if __name__ == "__main__":
    solve_knight_problem()