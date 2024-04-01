n=123
reversed=0
while(n>0):
    r=n%10
    reversed=(reversed*10)+r
    n=n//10

print(reversed)