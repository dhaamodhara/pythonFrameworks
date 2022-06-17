def linear_search(x,a):
    n=len(a)
    for i in range (0,n):
        if x==a[i]:
            return i
    return -1
if __name__=='__main__':
    pos=linear_search(5,[1,2,3,4])
    if pos==-1:
        print('Element not found')
    else:
        print('Element found at the position',pos)