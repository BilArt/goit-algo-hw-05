def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
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

    # Якщо елемент не знайдено, то повертається верхня межа
    if right < 0:
        return iterations, arr[0]
    if left >= len(arr):
        return iterations, arr[-1]
    return iterations, arr[left]

# Відсортований масив дробових чисел
sorted_array = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
target = 4.4  # Шуканий елемент

# Викликання функції двійкового пошуку
iterations, result = binary_search(sorted_array, target)

print("Кількість ітерацій:", iterations)
if result == target:
    print("Знайдено елемент:", result)
else:
    print("Найближчий елемент, що більший або рівний заданому значенню:", result)
