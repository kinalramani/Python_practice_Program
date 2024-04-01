def function_1(b):
    first=b[0]
    last=b[-1]
    if(first==last):
        return "true"
    else:
        return "false" 

list = [10, 20, 30, 40, 10]
a=function_1(list)
a()


