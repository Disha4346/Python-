#for global variable
x=10
def my_function():
    print(x)

my_function()


#for non-local variable
x=12
def nl():
    x=123
    y=1+x
    return y
print(nl())
