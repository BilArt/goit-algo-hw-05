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

# Реалізація алгоритму Кнута-Морріса-Пратта
def knuth_morris_pratt(text, pattern):
    comparisons = 0
    m = len(pattern)
    n = len(text)
    pi = compute_prefix_function(pattern)
    q = 0
    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]
            comparisons += 1
        if pattern[q] == text[i]:
            q += 1
            comparisons += 1
        if q == m:
            return comparisons, i - m + 1
    return comparisons, -1

def compute_prefix_function(pattern):
    m = len(pattern)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = pi[k - 1]
        if pattern[k] == pattern[q]:
            k += 1
        pi[q] = k
    return pi

