'''print("start")
def display1(args):
    print("address of args is",args)
    print("#1")
    def inner():
        print('#2')
        args()
    print("#3")
    return inner
@display1
def display2():
    print("in display2")
print("address is display2 is",display2)
display2()
print("end")
def positive(args):
    print("inside positive")
    def inner(a,b):
        print("inside inner")
        result=args(a,b)
        return abs(result)
    return inner
@positive
def sub(a,b):
    print("inside sub")
    return a-b
print(sub(1,2))'''
a=[1,2,3,4]
for i in range(len(a)-1,-1,-2):
    print(i)

