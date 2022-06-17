n=5
for i in range (1,n+1):
    a = ord('E')
    for j in range(1,n+1):
        if i+j>=n+1:
            print(chr(a),end=' ')
            a-= 1
        else:
            print(' ',end=' ')
            a-=1

    print()