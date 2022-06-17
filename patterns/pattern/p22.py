n=4
space=3
num=1

for i in range(1,n+1):
    a = 1
    for j in range(1,space+1):
        print(' ',end=' ')
    for k in range(1,num+1):
        print(i,end=' ')
        if k<(num+1)//2:
            i-=1
        else:
            i+=1

    space-=1
    num+=2
    print()
