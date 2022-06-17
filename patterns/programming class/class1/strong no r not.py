sum=0
n=145
m=n
while n!=0:
    ld=n%10
    n=n//10
    fact=1
    for i in range(1,ld+1):
        fact*=i
    sum+=fact
if m==sum:
    print('strong number')
else:
    print('not strong number')