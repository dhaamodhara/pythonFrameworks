n=15
flag=0
for i in range(1,n+1):
    if n==i*i:
        flag=1
        break
if flag==1:
        print('this is a perfect square')
else:
        print('this is not a perfect square')