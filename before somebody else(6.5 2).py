D=[1,2,3,4,5,6,7,8,9,10]
n=10
A=[]
for i in D:
    f=0
    for j in A:
        if i==j:
            f=1
    if f==0:
        A.append(i)
print ('Список а: ',A)
