'''thistuple=("apple","banana","kiwi")
# y=list(thistuple)
# y.append("watermelon")
# thistuple=tuple(y)
y=("orange",)
thistuple+=y
print(thistuple)'''
 
thistuple=("apple","banana","kiwi")
y=list(thistuple)
y.remove("apple")
thistuple=tuple(y)