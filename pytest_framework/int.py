#s=[4,3,2,1,5]
s=[]
a=int(input("enter the number of elements:"))
for i in range(0,a):
      b=int(input("enter the numbers:"))
      s.append(b)
      for k in range(a):
          for j in range(len(s)-1):
              if s[j]>s[j+1]:
                  s[j],s[j+1]=s[j+1],s[j]
print(s)

# wap to find the avg for given lisy
'''n=int(input("enter the number of elements to cslculate theavg:"))
a=[]
for i in range (0,n):
    ele=int(input("enter the elelement:"))
    a.append(ele)
b=sum(a)
print(b/n)
#wap to reverse a number in p
m=int(input("enter the number:"))
rev=0
while(m>0):
    d=m%10
    rev=rev*10+d
    m=m//10
print(rev)
#wap to sum of the digits of a number
n=int(input("enter the number:"))
tot=0
while(n>0):
    d=n%10
    tot=tot+d
    n=n//10
print(tot)
#wap to check palindrome or not
n=int(input("enter the number:"))
a=n
rev=0
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10
if rev==a:
    print("palindrome")
else:
    print("not palindrome")'''