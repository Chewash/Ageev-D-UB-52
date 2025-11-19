def g(a,b):
    while b:
        a,b=b,a%b
    return a
def f():
    a=int(input()) #числитель 1
    b=int(input()) #знаменатель 1
    c=int(input()) #числитель 2
    d=int(input()) #знаменатель 2
    e=b*d
    f=a*d-c*b
    h=g(abs(f),e)
    i=f//h
    j=e//h
    print (f"Результат {i}/{j}")
f()
    
