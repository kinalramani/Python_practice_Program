thistuple=("apple","banana","watermelon")
y=list(thistuple)
y[1]="kiwi"
thistuple=tuple(y)
print(thistuple)