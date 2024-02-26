import timeit


# Реалізація алгоритму Боєра-Мура
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    i = 0
    comparisons = 0

    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
            comparisons += 1
        if j == -1:
            return comparisons, i  # Знайдено збіг
        else:
            # Переміщення вправо на відстань, що вказує на збіг або -1
            i += max(1, j - pattern.rfind(text[i + j]))

    return comparisons, -1  # Підрядок не знайдено
