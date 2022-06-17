n=4
space=3
a=1
b=ord('A')
for i in range(1,n+1):
    for j in range(1,space+1):
        print(' ',end=' ')
    for k in range(1,a+1):
        print(chr(b),end=' ')
    space-=1
    a+=2
    b+=1
    print()