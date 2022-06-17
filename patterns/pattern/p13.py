n=5
a=ord('A')
for i in range (1,n+1):

    for j in range(1,n+1):
        if i>=j:
            if i%2==0:
                print(chr(a),end=' ')
                a+=1
            else:
                if i==1 or i==5:
                    print(1,end=' ')
                else:
                    print(0,end=' ')
        else:
            print(' ',end=' ')
    print()
