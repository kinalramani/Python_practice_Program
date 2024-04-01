str1 = 'I am 25 years and 10 months old'
digits=''
for i in str1:
    if i.isnumeric():
        digits+=i
print(digits)