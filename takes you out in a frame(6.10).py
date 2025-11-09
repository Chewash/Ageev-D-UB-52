A=[1,2,2,4,5,5,7,8,9,10]
n=10
B=[]
p=0
for i in range(n):
    if A[i] in A[i+1:] and not (A[i] in B):
        B.append(A[i])
        p=1
if p==0:
    print ("нет такого")
else:
    print (B)
