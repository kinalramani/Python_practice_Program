str="Hello world"

lower=0
upper=0
for i in str:
    if i.islower():
        lower+=1
    elif i.isupper():
        upper+=1
    else:
        print("special symbol")
print("UPPER CASE",lower)
print("LOWER CASE",upper)