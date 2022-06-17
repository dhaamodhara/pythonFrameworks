n=5
for i in range (1,n+1):
    a=ord('A')
    for j in range (1,i+1):
         if i%2==0:
            print(j,end=' ')
         elif i>=j:
             print(chr(a),end=' ')
             a+=1
         else:
            print(' ',end=' ')
    print()
