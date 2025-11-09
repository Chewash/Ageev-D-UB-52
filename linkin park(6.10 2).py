A=[1,2,3,4,5,6,7,8,9,25,11,12,13,14,21]
n=15
print (A)
for i in range(n):
    if A[i]<10:
        A[i]=0
    if A[i]>20:
        A[i]=1
print (A)
