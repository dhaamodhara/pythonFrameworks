def insertion(a):
    n=len(a)
    for passno in range(1,n):
        i=passno
        while i>0 and a[i]<a[i-1]:
            a[i],a[i-1]=a[i-1],a[i]
            i-=1
    return a
if __name__=="__main__":
    new=insertion([8,6,7,1,3,2])
    print(new)