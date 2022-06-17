class A:
    def disp(self):#defining the method
        print('method of parent class')
class B(A):
    def disp(self):#defining or args the method with same name which is overridden for parent
        print('method of child')

ob=B()
ob.disp()
oa=A()
oa.disp()