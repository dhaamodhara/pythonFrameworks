class A:
    def __init__(self):
        print('constructor of class A')
class B(A):
    b=20
    def __init__(self):
        print('constructor of class B(A)')
class C(A):
    c=30
class D(C,B):
    d=40
oa=A()
ob=B()
oc=C()
od=D()
ob.b=30
print(ob.b)


