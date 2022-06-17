def bubble(a):
    n=len(a)
    for passno in range(1,n):
        for i in range(0,n-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
    return a
if __name__=='__main__':
    new=bubble([7,2,4,5,3,6])
    print(new)

