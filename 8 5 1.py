n=2
m=2
A=[]
B=[]
M=0
for i in range(n):
    b=[]
    for j in range(m):
        b.append(int(input()))
    A.append(b)
print("До сортировки")
print (A)
for k in A:
    k.sort()
print ("После")
print (A)

                
        
