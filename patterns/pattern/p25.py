n=5
for i in range(1,n+1):
    a=ord('A')
    for j in range(1,n+1):
        if i>=j:
            if j%2==0:
                print(chr(a),end=' ')
                a+=1
            else:
                print(j,end=' ')
        else:
            print(' ',end=' ')
    print()