import math
x=-4.5
print ("x =", x)
y=0.75*(10**(-4))
print("y =", y)
z=-0.845*(10**2)
print ("z =", z)

a=(9+(x-y)**2)**1/3

b=(x**2)+(y**2)+2

c=(math.exp(x-y))*(math.tan(z)**3)

S=(a/b)-c

print ("S =", S)
