def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return iterations, arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        iterations += 1
    return iterations, arr[right] if right >= 0 else None
