'''# prime number
l=int(input("enter the lower value:"))
h=int(input("enter the higher value:"))
for i in range(l,h+1):
    if i>1:
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            print(i)
#fibb
n=int(input("enter the number of fibbonacci numbers to print"))
first=0
second=1
for i in range(n):
    print(first)
    temp=first
    first=second
    second=temp+second'''
#armstong
def isArmstrong(x):
    n=order(x)
    temp=x
    sum1=0
    while(temp!=0):
        r=temp%10
        sum1=sum1+power(r,n)
        temp=temp/10
    return (sum1==x)
x=153
print(isArmstrong(x))


