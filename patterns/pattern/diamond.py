n=7
space=n//2
star=1
for i in range(1,n+1):
    m=ord('A')
    for j in range(1,space+1):
        print(' ',end=' ')
    for k in range(1,star+1):
        if k==1 or k==star:
            print('*',end=' ')
        else:
            print(chr(m),end=' ')
            if k>star//2:
                m-=1
            else:
                m+=1
    if i<=n//2:
        space-=1
        star+=2
    else:
        space+=1
        star-=2
    print()