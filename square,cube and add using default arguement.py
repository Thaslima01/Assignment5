def square():
    x=int(input("enter the number"))
    s=x**2
    print(s)
    return s
def cube(y=3):
    c=y**3
    print(c)
    return c
def add():
    print(square()+cube())
add()
