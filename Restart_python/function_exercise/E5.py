def outter_fun(a,b):
    square = a ** 2
    def inner_func(a,b):
        return a+b
    add=inner_func(a,b)
    return add
o=outter_fun(5,2)
print(o)
