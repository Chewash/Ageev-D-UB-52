with open("Агеев УБ-52 vvod.txt", "r") as f:
    a = f.readlines()
    b = [list(map(int, c.strip().split())) for c in a]

n = len(b)
m = len(b[0])

d = [sorted(e) for e in b]
g = []
for h in b:
    i = min(h)
    j = h.index(i)
    
    k = h.copy()
    if i % 2 == 0:
        k[j] = 0
    else:
        k[j] = 1
    g.append(k)
with open("Агеев УБ-52 vivod.txt", "w") as l:
    l.write("Отсортированные строки: ")
    for p in d:
        l.write(" ".join(map(str, p)))
    
    l.write("\nЗадание 2: Матрица с замененными минимальными элементами:\n")
    for q in g:
        l.write(" ".join(map(str, q)))
