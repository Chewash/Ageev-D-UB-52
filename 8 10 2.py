M = int(input("Введите количество строк M: "))
N = int(input("Введите количество столбцов N: "))
k = int(input(f"Введите номер строки k для сортировки: "))
if k < 1 or k > M:
    print("номер строки k должен быть в диапазоне от 1 до", M)
else:
    
    D = []
    print(f"Введите элементы матрицы {M}x{N}:")
    for i in range(M):
        row = []
        for j in range(N):
            element = int(input(f"Элемент [{i+1}][{j+1}]: "))
            row.append(element)
        D.append(row)
    print("\nИсходная матрица:")
    for row in D:
        print(row)
    
    D[k-1].sort()
    print(f"\nМатрица после сортировки {k}-й строки по возрастанию:")
    for row in D:
        print(row)
