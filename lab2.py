def main(n, w, h):
    def can_fit(side):
        return (side // w) * (side // h) >= n

    left = min(w, h)
    right = n * max(w, h)
    iterations = 0 

    while left + 1 < right:
        mid = (left + right) // 2
        
        if can_fit(mid):
            right = mid
        else:
            left = mid
        iterations += 1

    print(f"Алгоритм впорався всього за {iterations} ітерацій!")
    return right


if __name__ == "__main__":
    n = int(input("Введіть кількість листків (N): "))
    w = int(input("Введіть ширину листка (W): "))
    h = int(input("Введіть висоту листка (H): "))
    
    відповідь = main(n, w, h)
    
    print(f"Мінімальний розмір квадратної дошки: {відповідь} на {відповідь}")