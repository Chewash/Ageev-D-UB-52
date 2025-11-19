def p(n):
    if n < 10:
        print(n)
    else:
        print(n % 10, end=" ")
        p(n // 10)
print (p(12345))
