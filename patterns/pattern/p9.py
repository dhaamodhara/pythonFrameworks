n=5
for i in range(1,n+1):
    a=0
    for j in range(1,n+1):
        if i+j>=n+1:
            if j%2!=0:
                print(j,end=' ')
            else:
                print(a,end=' ')
        else:
            print(' ',end=' ')
    print()