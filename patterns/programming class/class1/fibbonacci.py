n=10
a=0
b=1
if n==1:
    print(fib1)
elif n==2:
    print(fib2)
else:
    for i in range(3,n+1):
        c=a+b
        a=b
        b=c
    print(c)
