n=4
space=3
c=1
for i in range(1,n+1):
    a=ord('A')
    for j in range(1,space+1):
        print(' ',end=' ')
    for k in range(1,c+1):
        print(chr(a),end=' ')
        if k<(c+1)//2:
            a+=1
        else:
            a-=1
    space-=1
    c+=2
    print()