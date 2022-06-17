n=121
m=n
rev=0
while n!=0:
    ld=n%10
    n=n//10
    rev=rev*10+ld
if m==rev:
    print('the number is palindrome')
else:
    print('the number is not palindrome')