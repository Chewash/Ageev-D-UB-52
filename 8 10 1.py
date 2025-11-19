n=int(input("сколко строк: "))
m=int(input("чисел в строках: "))
A=[]
q=0
w=1
for j in range(n):
    b=[]
    for i in range(m):
        
        b.append(int(input()))
    A.append(b)
    print (A)
for k in A:
    k.sort()
    i=max(max(row) for row in A)
    print ("max: ",i)
    break
