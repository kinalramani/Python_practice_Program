n=int(input("Entre your number"))
rev=0
temp=n
while (n!=0):
    r=n%10
    res=(rev*10)+r
    n//=10

print("reversed_number",res)