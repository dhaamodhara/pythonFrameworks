n=4
a=2
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            print(a,end=' ')
        else:
            print(' ',end=' ')
    a*=2
    print()