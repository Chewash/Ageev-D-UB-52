with open("Агеев УБ-52 vvod.txt","w" as vvod):
    n=int(input("сколько строк: "))
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
with open("Агеев УБ-52 vivod.txt","a" as vivod):
    for k in A:
        k.sort()
        i=k[0]
        print ("минимальный элемент списка: ",i)
        if i%2==0:
            A=q
        if i%2!=0:
            A=w
        print (A)

    
    
     

