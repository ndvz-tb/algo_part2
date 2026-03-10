def find_unsorted_subarray(arr):
    n = len(arr)

    if n < 2:
        return -1, -1

    left = 0
    while left < n - 1:
        if arr[left] > arr[left + 1]:
            break
        left += 1

    if left == n - 1:
        return -1, -1

    right = n - 1
    while right > 0:
        if arr[right] < arr[right - 1]:
            break
        right -= 1

    temp_min = arr[left]
    temp_max = arr[left]

    for i in range(left, right + 1):
        if arr[i] < temp_min:
            temp_min = arr[i]
        if arr[i] > temp_max:
            temp_max = arr[i]

    while left > 0:
        if arr[left - 1] > temp_min:
            left -= 1
        else:
            break

    while right < n - 1:
        if arr[right + 1] < temp_max:
            right += 1
        else:
            break

    return left, right