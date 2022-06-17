def partition(a,low,high):
    i=low-1
    pivot=a[high]
    for j in range (low,high):
        if a[j]<=pivot:
            i+=1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[high]=a[high],a[i+1]
    return i+1
print(partition([22,6,3,13,12,18],0,5))
def Qs(a,low,high):
    if low<high:
        pivot_pos=partition(a,low,high)
        Qs(a,low,pivot_pos-1)
        Qs(a,pivot_pos+1,high)
    return a
print(Qs([7,6,3,4,1,8,5,9,10],0,8))
