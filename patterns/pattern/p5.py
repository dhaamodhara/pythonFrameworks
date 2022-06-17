n=5
for i in range (1,n+1):
    a=ord('A')
    b=1
    for j in range (1,n+1):
        if i>=j:
            if j%2!=0:
                print(b,end=' ')
                b*=2
            else:
                print(chr(a),end=' ')
                a+=1
        else:
            print(' ',end=' ')
    print()