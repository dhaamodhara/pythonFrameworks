n=5
for i in range(1,n+1):
    a=ord('B')
    for j in range(1,n+1):
        if i>=j:
            if j%2!=0:
                print(j,end=' ')
            else:
                print(chr(a),end=' ')
                a+=2
        else:
            print(' ',end=' ')
    print()
