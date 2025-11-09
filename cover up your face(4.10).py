n=int(input())
k=int(input())
a,b=0,1
s=0
c=0
for i in range(1,k+n):
    a,b=b,a+b
    if i>=k:
        s=s+a
        c=c+1
    if c==n:
        break
print (s)
