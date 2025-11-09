D=[1,-2,3,-4,-5,-6,-7,-8,9,10]
n=10
for i in range(n):
    if D[i]<0 and D[i+1]<0:
        print (D[i],D[i+1])
