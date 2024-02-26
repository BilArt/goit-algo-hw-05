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

# Реалізація алгоритму Рабіна-Карпа
def rabin_karp(text, pattern):
    comparisons = 0
    d = 256  # Розмір алфавіту ASCII
    q = 101  # Просте число
    n = len(text)
    m = len(pattern)
    p = 0
    t = 0
    h = 1

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            for j in range(m):
                if text[i + j] != pattern[j]:
                    break
                comparisons += 1
            else:
                return comparisons, i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return comparisons, -1

# Заготовковий код для вимірювання часу виконання
with open('text1.txt', 'r', encoding='latin1') as file:
    text1 = file.read()
with open('text2.txt', 'r', encoding='latin1') as file:
    text2 = file.read()

pattern1 = "ipsum"  # Паттерн для першого тексту
pattern2 = "habitat"  # Паттерн для другого тексту

print("Boyer-Moore:")
print("Pattern 1:", boyer_moore(text1, pattern1))
print("Pattern 2:", boyer_moore(text2, pattern2))

print("Knuth-Morris-Pratt:")
print("Pattern 1:", knuth_morris_pratt(text1, pattern1))
print("Pattern 2:", knuth_morris_pratt(text2, pattern2))

print("Rabin-Karp:")
print("Pattern 1:", rabin_karp(text1, pattern1))
print("Pattern 2:", rabin_karp(text2, pattern2))
