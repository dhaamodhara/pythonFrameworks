m=4
n=5
while m!=n and m!=0 and n!=0:
    if m>n:
        m=m%n
    else:
        n=n%m
if n==0 or m==n:
    print(m)
else:
    print(n)