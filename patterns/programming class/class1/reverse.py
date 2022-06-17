n=1234
rev=0
while n!=0:
    ld=n%10
    n=n//10
    rev=rev*10+ld
print(rev)