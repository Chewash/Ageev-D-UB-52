def f():
    n = int(input())
    if n == 0:
        return -10**9  
    return max(n, f())

print("Введите числа (0 для конца):")
print(f"Максимум: {f()}")
