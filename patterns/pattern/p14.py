n=5
a = 2
for i in range(1,n+1):
    b=ord('A')
    for j in range(1,n+1):
        if i<=j:
            if i%2==0:
                print(chr(b),end=' ')
                b+=1
            else:
                print(a,end=' ')
        else:
            print(' ',end=' ')
    if i%2==1:
        a *= 2
    print()