n=4
space=3
s=1
for i in range(1,n+1):
    for j in range(1,space+1):
        print(' ',end=' ')
    for k in range(1,s+1):
        print('*',end=' ')
    space-=1
    s+=2
    print()